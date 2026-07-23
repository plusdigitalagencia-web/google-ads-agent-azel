#!/usr/bin/env python3
"""
meta_report_claude.py — Relatório Semanal Meta Ads com Claude AI (7 Módulos)
Mesmo formato/prompt do onvoix_meta_report.py, parametrizado por env vars:
  META_TOKEN, ACCOUNT_ID, CLIENT_NAME, CURRENCY, BUDGET_MONTHLY,
  REPORT_DIR, USE_MONTH_FOLDER, GH_PAT, ANTHROPIC_API_KEY
"""
import os, urllib.request, urllib.error, urllib.parse, json, datetime, base64, time
import anthropic

TOKEN         = os.environ["META_TOKEN"]
ACCOUNT       = os.environ["ACCOUNT_ID"]
CLIENT_NAME   = os.environ["CLIENT_NAME"]
_CURR_RAW     = os.environ.get("CURRENCY", "EUR")
CURRENCY      = {"EUR": "€", "BRL": "R$", "USD": "$", "GBP": "£"}.get(_CURR_RAW, _CURR_RAW)
BUDGET_EST    = int(os.environ.get("BUDGET_MONTHLY", "0"))
REPORT_DIR    = os.environ.get("REPORT_DIR", "reports/data-know")
USE_MONTH     = os.environ.get("USE_MONTH_FOLDER", "false").lower() == "true"
GITHUB_TOKEN  = os.environ["GH_PAT"]
ANTHROPIC_KEY = os.environ["ANTHROPIC_API_KEY"]
GITHUB_REPO   = "plusdigitalagencia-web/google-ads-agent-azel"
BASE          = "https://graph.facebook.com/v25.0"

today    = datetime.date.today()
p1_end   = today - datetime.timedelta(days=1)
p1_start = today - datetime.timedelta(days=7)
p2_end   = today - datetime.timedelta(days=8)
p2_start = today - datetime.timedelta(days=14)

if USE_MONTH:
    MESES = {1:'jan',2:'fev',3:'mar',4:'abr',5:'mai',6:'jun',
             7:'jul',8:'ago',9:'set',10:'out',11:'nov',12:'dez'}
    REPORT_DIR = f"{REPORT_DIR}/{MESES[today.month]}-{today.year}"

filepath = f"{REPORT_DIR}/meta-report-{today.strftime('%Y-%m-%d')}.md"

# ── Coleta de dados ──────────────────────────────────────────────────────────

def fetch(since, until, level="campaign"):
    fields = "campaign_name,adset_name,ad_name,spend,clicks,impressions,reach,cpm,ctr,frequency,actions"
    params = urllib.parse.urlencode({
        "fields": fields, "level": level,
        "time_range": json.dumps({"since": str(since), "until": str(until)}),
        "action_breakdowns": "action_type",
        "access_token": TOKEN, "limit": 200
    })
    try:
        resp = urllib.request.urlopen(f"{BASE}/{ACCOUNT}/insights?{params}", timeout=30)
        return json.loads(resp.read()).get("data", [])
    except Exception as e:
        print(f"Erro fetch {level}: {e}")
        return []

def get_leads(row):
    for x in row.get("actions", []):
        if x.get("action_type") in ("lead", "leadgen_other", "onsite_conversion.lead_grouped"):
            return float(x.get("value", 0))
    return 0.0

def calc_totals(data):
    t = dict(spend=0, leads=0, cpm_s=0, ctr_s=0, freq_s=0, n=0)
    for r in data:
        t["spend"]  += float(r.get("spend", 0))
        t["leads"]  += get_leads(r)
        t["cpm_s"]  += float(r.get("cpm", 0))
        t["ctr_s"]  += float(r.get("ctr", 0))
        t["freq_s"] += float(r.get("frequency", 0))
        t["n"]      += 1
    n = t["n"] or 1
    t["avg_cpm"]  = round(t["cpm_s"] / n, 2)
    t["avg_ctr"]  = round(t["ctr_s"] / n, 2)
    t["avg_freq"] = round(t["freq_s"] / n, 2)
    t["cpl"]      = round(t["spend"] / t["leads"], 2) if t["leads"] else None
    return t

def row_to_dict(r, level="ad"):
    l  = get_leads(r)
    sp = float(r.get("spend", 0))
    d  = {
        "name":      r.get(f"{level}_name", r.get("campaign_name", "")),
        "campaign":  r.get("campaign_name", ""),
        "spend":     round(sp, 2),
        "leads":     int(l),
        "cpl":       round(sp / l, 2) if l else None,
        "ctr":       round(float(r.get("ctr", 0)), 2),
        "cpm":       round(float(r.get("cpm", 0)), 2),
        "frequency": round(float(r.get("frequency", 0)), 2),
    }
    if level == "adset":
        d["ad_set"] = r.get("adset_name", "")
    return d

print(f"Buscando dados da Meta API — {CLIENT_NAME} ({ACCOUNT})...")
camp_curr  = fetch(p1_start, p1_end, "campaign")
camp_prev  = fetch(p2_start, p2_end, "campaign")
adset_curr = fetch(p1_start, p1_end, "adset")
ad_curr    = fetch(p1_start, p1_end, "ad")
ad_prev    = fetch(p2_start, p2_end, "ad")

curr = calc_totals(camp_curr)
prev = calc_totals(camp_prev)

# Pacing
dias_mes  = today.day
last_day  = (datetime.date(today.year, today.month % 12 + 1, 1) - datetime.timedelta(days=1)).day if today.month < 12 else 31
pct_mes   = round((dias_mes / last_day) * 100, 1)
proj_mes  = round(curr["spend"] / 7 * 30, 2)
diff_p    = round((proj_mes / BUDGET_EST * 100) - 100, 1) if BUDGET_EST else 0

# ── Montar pacote de dados para o Claude ─────────────────────────────────────

data_package = {
    "client":           CLIENT_NAME,
    "account":          ACCOUNT,
    "currency":         CURRENCY,
    "budget_monthly":   BUDGET_EST,
    "period_current":   {"start": str(p1_start), "end": str(p1_end)},
    "period_previous":  {"start": str(p2_start), "end": str(p2_end)},
    "generated_at":     str(today),
    "pacing": {
        "day_of_month":        dias_mes,
        "days_in_month":       last_day,
        "pct_month_elapsed":   pct_mes,
        "spend_week":          round(curr["spend"], 2),
        "projection_monthly":  proj_mes,
        "budget_estimated":    BUDGET_EST,
        "projection_vs_budget_pct": diff_p,
    },
    "summary": {
        "current":  {**curr, "spend": round(curr["spend"], 2), "leads": int(curr["leads"])},
        "previous": {**prev, "spend": round(prev["spend"], 2), "leads": int(prev["leads"])},
    },
    "campaigns_current":  [row_to_dict(r, "campaign") for r in camp_curr],
    "campaigns_previous": [row_to_dict(r, "campaign") for r in camp_prev],
    "ad_sets_current":    [row_to_dict(r, "adset")    for r in adset_curr],
    "ads_current":        [row_to_dict(r, "ad")        for r in ad_curr],
    "ads_previous":       [row_to_dict(r, "ad")        for r in ad_prev],
}

# ── System prompt (idêntico ao onvoix_meta_report.py) ────────────────────────

SYSTEM_PROMPT = """Você é um analista sênior de Meta Ads especializado em campanhas de geração de leads (Lead Gen).
Analisa dados brutos de Meta Ads e gera relatório semanal completo em português (Brasil).
O objetivo sempre é: mais leads com menor CPL possível.

## REGRAS OBRIGATÓRIAS — siga à risca

### CRIATIVO VENCEDOR
- Mínimo 5 leads para ser considerado "vencedor"
- Se nenhum tiver 5+, escolha o melhor CPL com pelo menos 1 lead e indique "estatisticamente cedo para conclusão"
- NUNCA escolha vencedor com 1-2 leads apenas por ter CPL baixo
- Mencione sempre o volume: "CPL $0,44 com 9 leads"

### CONSISTÊNCIA ENTRE MÓDULOS — crítico
- Criativo marcado como anomalia no Módulo 3 → NÃO recomende escalar no Módulo 6 nem no Plano de Ação
- Criativo 🔴 CRÍTICO no Módulo 1 → deve aparecer em "O que não está funcionando" no bloco Trello
- Pacing 🟡 LENTO ou 🔴 ACELERADO → obrigatório aparecer no bloco Trello com ação concreta

### THRESHOLDS DE STATUS
- 🟢 OK: leads > 0 E CPL ≤ média da conta × 1.3
- 🟡 ATENÇÃO: CPL entre 1.3x e 2x da média, OU frequência ≥ 2.5
- 🔴 CRÍTICO: CPL > 2x da média, OU 0 leads com gasto > $15, OU frequência ≥ 3.5

### SIGNIFICÂNCIA ESTATÍSTICA
- Criativos com gasto < $3: mencione mas não baseie recomendações neles
- CTR alto com poucos leads = sem significância ainda

### PACING
- Sempre calcule: projeção mensal vs budget estimado
- 🟢 dentro do ritmo: diferença ≤ 10%
- 🟡 lento: projeção abaixo do budget em mais de 10%
- 🔴 acelerado: projeção acima do budget em mais de 10%

## FORMATO DO RELATÓRIO (markdown)

# Relatorio Meta Ads - {CLIENT_NAME}
**Periodo atual:** DD/MM/YYYY a DD/MM/YYYY
**Periodo anterior:** DD/MM/YYYY a DD/MM/YYYY
**Gerado em:** DD/MM/YYYY | **Conta:** {ACCOUNT}

---

## Resumo Executivo
(tabela: Metrica | Atual | Anterior | Variacao — com emoji de tendência)

---

## Modulo 1 - Auditoria de Campanhas e Anuncios
### Campanhas (tabela)
### Anuncios por Campanha (tabela por campanha, anúncios ordenados por CPL)

---

## Modulo 2 - Diagnostico de CPL (Causa Raiz)
(por campanha: identifica causa raiz real — CPM alto? CTR baixo? Frequência? Público saturado?)

---

## Modulo 3 - Deteccao de Anomalias
(tabela: Tipo | Anuncio | Variacao | Acao — compare com semana anterior)
(se nenhuma: "Nenhuma anomalia significativa detectada.")

---

## Modulo 4 - Pacing Monitor
(dia X de Y do mês | projeção | budget | status com emoji)

---

## Modulo 5 - Fadiga de Criativos
(tabela: Anuncio | Freq | CTR | Leads | Status | Recomendacao)
(frequência < 1.8 = OK | 1.8-2.5 = Monitorar | 2.5-3.5 = Atenção | >3.5 = Fadiga)

---

## Modulo 6 - Analise de Copy e Criativos
(top vencedores com volume de leads explícito — sem contradição com Módulo 3)
(criativos para pausar com justificativa)

---

## Modulo 7 - Analise de Ad Sets e Publicos
(tabela de ad sets | observações sobre sobreposição se relevante)

---

## Plano de Acao
(tabela: Prioridade | Acao | Impacto | Prazo — sem contradições com módulos anteriores)

---

## BLOCO TRELLO

(Este bloco NÃO é um resumo de 5 linhas — é um panorama executivo completo para o gestor que não vai ler o relatório inteiro. Deve ser rico, com os principais insights de cada módulo, contextualizado e com causa raiz real. Escreva como se estivesse explicando a situação da conta para alguém que não viu os dados.)

Meta Ads {CLIENT_NAME} - DD/MM/YYYY
Gasto: $X | Leads: N | CPL: $X
Variação vs semana anterior: CPL X% emoji | Leads X% emoji
Pacing: [status emoji] — Projeção $X vs Budget $X ([X]% do mês decorrido)

---

📌 CONTEXTO DA SEMANA
[Se houve mudança relevante na conta — campanha pausada/reativada, novo criativo, mudança de budget, público saturado — explique em 2-4 linhas o que mudou e por que isso impacta os números. Se não houve nada relevante, OMITIR esta seção completamente.]

---

📊 PANORAMA DA SEMANA

🔍 Campanhas & Anúncios
[2-3 linhas: quais campanhas estão ativas, situação geral dos anúncios, o que está gerando resultado e o que não está. Cite nomes reais.]

📉 Causa Raiz do CPL
[2-4 linhas: explique por que o CPL subiu ou caiu. Seja específico — CPM melhorou mas CTR caiu? Criativo ineficiente consumindo budget? Campanha com melhor CPL foi pausada? Relate a causa real, não só o número.]

⚠️ Anomalias
[Se houver: lista com bullet dos problemas detectados — criativos com 0 leads, CPM anômalo, desaparecimento de campanha. Se não houver: "Nenhuma anomalia crítica esta semana."]

📅 Pacing
[2-3 linhas: projeção mensal vs budget + o que está causando o ritmo atual + ação concreta necessária para corrigir. Ex: "No ritmo atual, julho encerrará com $192 de $500 gastos — apenas 38% do budget aproveitado. A principal causa é o encerramento da campanha Site - México que gerava 140 leads/semana. Ação: reativar campanha ou aumentar budget diário da ativa."]

😴 Fadiga de Criativos
[1-2 linhas: status de frequência geral dos criativos. Há algum em risco de fadiga? Ou está tudo OK abaixo de 1.8?]

🎨 Criativos
Vencedor principal: [nome] — CPL $X com N leads ([formato: vídeo/imagem])
[Candidato a escalar]: [nome] se houver — CPL $X com N leads
Para pausar: [nome] — [motivo direto em 1 linha]
Dados insuficientes (aguardar): [nomes separados por vírgula]

🎯 Ad Sets & Públicos
[1-2 linhas: CPM do público, espaço para escala, risco de sobreposição se houver mais de 1 ad set.]

---

🚀 PRÓXIMOS PASSOS
- 🔴 [ação urgente P1 — hoje]
- 🔴 [ação urgente P2 se houver]
- 🟡 [ação importante P3 — 24-48h]
- 🟢 [ação de melhoria P4 se relevante]

---
"""

# ── Chamada Claude API (com retry/backoff para 429/5xx) ──────────────────────

def call_claude_with_retry(ai_client, **kwargs):
    delays = [10, 30, 60]
    for attempt, delay in enumerate(delays + [None]):
        try:
            return ai_client.messages.create(**kwargs)
        except (anthropic.RateLimitError, anthropic.APIStatusError) as e:
            status = getattr(e, "status_code", None)
            transient = isinstance(e, anthropic.RateLimitError) or status in (429, 500, 502, 503, 529)
            if delay is None or not transient:
                raise
            print(f"Erro Claude API ({status or 'rate_limit'}) — tentativa {attempt+1}/4, aguardando {delay}s...")
            time.sleep(delay)

print("Analisando com Claude AI...")
ai_client = anthropic.Anthropic(api_key=ANTHROPIC_KEY)

message = call_claude_with_retry(
    ai_client,
    model="claude-sonnet-4-6",
    max_tokens=8192,
    system=SYSTEM_PROMPT,
    messages=[{
        "role": "user",
        "content": (
            f"Analise os dados abaixo e gere o relatório semanal completo de Meta Ads.\n\n"
            f"```json\n{json.dumps(data_package, ensure_ascii=False, indent=2)}\n```\n\n"
            f"Lembre das regras: criativo vencedor precisa de mínimo 5 leads, "
            f"sem contradições entre módulos, pacing sempre no bloco Trello."
        )
    }]
)

report = message.content[0].text
print(f"Relatório gerado | Tokens: {message.usage.input_tokens} input / {message.usage.output_tokens} output")

# ── Salvar no GitHub ──────────────────────────────────────────────────────────

def save_to_github(path, content, msg):
    url     = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{path}"
    encoded = base64.b64encode(content.encode()).decode()
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Content-Type": "application/json"}
    for attempt in range(5):
        req = urllib.request.Request(url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
        try:
            sha = json.loads(urllib.request.urlopen(req).read()).get("sha", "")
        except Exception:
            sha = ""
        payload = {"message": msg, "content": encoded}
        if sha:
            payload["sha"] = sha
        req2 = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers, method="PUT")
        try:
            urllib.request.urlopen(req2)
            print(f"Salvo: https://github.com/{GITHUB_REPO}/blob/main/{path}")
            return
        except urllib.error.HTTPError as e:
            err = e.read().decode()
            if e.code == 409 and attempt < 4:
                wait = (attempt + 1) * 15
                print(f"Conflito SHA (tentativa {attempt+1}/5) — aguardando {wait}s...")
                time.sleep(wait)
            else:
                print(f"Erro ao salvar: {err}")
                raise SystemExit(1)

save_to_github(filepath, report, f"feat: relatorio Meta Ads {CLIENT_NAME} {today.strftime('%Y-%m-%d')} (Claude AI)")
