#!/usr/bin/env python3
"""
Hoteligy - Relatorio Semanal Meta Ads (7 Modulos)
SOP: data-know/SOP-analise-meta-ads.md
Conta: act_51307638 | Moeda: EUR | Global (Espanha, Portugal, LATAM)
Roda toda segunda via GitHub Actions as 07:10 BRT
Token: HOTELIGY_META_TOKEN | App Meta: 687818438366946
"""
import os, urllib.request, urllib.error, urllib.parse
import json, datetime, base64, time

TOKEN        = os.environ["HOTELIGY_META_TOKEN"]
GITHUB_TOKEN = os.environ["GH_PAT"]
ACCOUNT      = "act_51307638"
BASE         = "https://graph.facebook.com/v25.0"
GITHUB_REPO  = "plusdigitalagencia-web/google-ads-agent-azel"
CLIENT_NAME  = "Hoteligy"
CURRENCY     = "€"
BUDGET_EST   = 0  # EUR/mes — a definir com o cliente

today    = datetime.date.today()
p1_end   = today - datetime.timedelta(days=1)
p1_start = today - datetime.timedelta(days=7)
p2_end   = today - datetime.timedelta(days=8)
p2_start = today - datetime.timedelta(days=14)

def fetch(since, until, level="campaign"):
    fields = "campaign_name,adset_name,ad_name,spend,clicks,impressions,reach,cpm,ctr,frequency,actions,cost_per_action_type"
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
        print(f"Erro {level}: {e}")
        return []

def leads(row):
    for x in row.get("actions", []):
        if x.get("action_type") in ("lead", "leadgen_other", "onsite_conversion.lead_grouped"):
            return float(x.get("value", 0))
    return 0.0

def cur(v):
    return f"{CURRENCY}{v:.2f}"

def cpl_str(spend, l):
    return cur(spend/l) if l > 0 else "---"

def pct(a, b):
    if b == 0: return "---"
    v = ((a - b) / b) * 100
    return f"{'+'if v>0 else ''}{v:.1f}%"

def pct_num(a, b):
    if b == 0: return None
    return ((a - b) / b) * 100

def totals(data):
    t = dict(spend=0, impressions=0, clicks=0, leads=0, cpm_s=0, ctr_s=0, freq_s=0, n=0)
    for r in data:
        t["spend"] += float(r.get("spend", 0))
        t["impressions"] += int(r.get("impressions", 0))
        t["clicks"] += int(r.get("clicks", 0))
        t["leads"] += leads(r)
        t["cpm_s"] += float(r.get("cpm", 0))
        t["ctr_s"] += float(r.get("ctr", 0))
        t["freq_s"] += float(r.get("frequency", 0))
        t["n"] += 1
    n = t["n"] or 1
    t.update(avg_cpm=t["cpm_s"]/n, avg_ctr=t["ctr_s"]/n, avg_freq=t["freq_s"]/n)
    t["cpl_val"] = t["spend"]/t["leads"] if t["leads"] else 0
    return t

def status(l, cpl_val, avg_cpl):
    if l == 0: return "🔴 CRITICO"
    if avg_cpl == 0: return "🟢 OK"
    if cpl_val <= avg_cpl * 1.2: return "🟢 OK"
    if cpl_val <= avg_cpl * 1.8: return "🟡 ATENCAO"
    return "🔴 CRITICO"

print(f"Buscando dados {CLIENT_NAME}...")
camp_curr  = fetch(p1_start, p1_end, "campaign")
camp_prev  = fetch(p2_start, p2_end, "campaign")
adset_curr = fetch(p1_start, p1_end, "adset")
ad_curr    = fetch(p1_start, p1_end, "ad")
ad_prev    = fetch(p2_start, p2_end, "ad")
curr = totals(camp_curr)
prev = totals(camp_prev)

dias_mes = today.day
if today.month < 12:
    last_day = (datetime.date(today.year, today.month + 1, 1) - datetime.timedelta(days=1)).day
else:
    last_day = 31
pct_mes = (dias_mes / last_day) * 100

if BUDGET_EST > 0:
    diff_p = (curr["spend"] / BUDGET_EST * 100) - pct_mes
    if abs(diff_p) <= 10: pacing_st = "NO RITMO"; pacing_icon = "🟢"
    elif diff_p > 10:     pacing_st = "ACELERADO"; pacing_icon = "🔴"
    else:                 pacing_st = "LENTO";     pacing_icon = "🟡"
else:
    diff_p = 0; pacing_st = "SEM BUDGET"; pacing_icon = "⚪"

ad_prev_map   = {r.get("ad_name", ""): r for r in ad_prev}
avg_cpl       = curr["cpl_val"]
ad_curr_names = {r.get("ad_name","") for r in ad_curr}

L = []; A = L.append

A(f"# Relatorio Meta Ads - {CLIENT_NAME}")
A(f"**Periodo atual:** {p1_start.strftime('%d/%m/%Y')} a {p1_end.strftime('%d/%m/%Y')}")
A(f"**Periodo anterior:** {p2_start.strftime('%d/%m/%Y')} a {p2_end.strftime('%d/%m/%Y')}")
A(f"**Gerado em:** {today.strftime('%d/%m/%Y')} | **Conta:** {ACCOUNT}")
A(""); A("---"); A("")

A("## Resumo Executivo"); A("")
A("| Metrica | Atual | Anterior | Variacao |")
A("|---|---|---|---|")
A(f"| Gasto | {cur(curr['spend'])} | {cur(prev['spend'])} | {pct(curr['spend'],prev['spend'])} |")
A(f"| Leads | {int(curr['leads'])} | {int(prev['leads'])} | {pct(curr['leads'],prev['leads'])} |")
cpl_var = pct(curr['cpl_val'],prev['cpl_val']) if curr['leads'] and prev['leads'] else "---"
A(f"| CPL medio | {cpl_str(curr['spend'],curr['leads'])} | {cpl_str(prev['spend'],prev['leads'])} | {cpl_var} |")
A(f"| CTR medio | {curr['avg_ctr']:.2f}% | {prev['avg_ctr']:.2f}% | {pct(curr['avg_ctr'],prev['avg_ctr'])} |")
A(f"| CPM medio | {cur(curr['avg_cpm'])} | {cur(prev['avg_cpm'])} | {pct(curr['avg_cpm'],prev['avg_cpm'])} |")
A(f"| Frequencia | {curr['avg_freq']:.2f} | {prev['avg_freq']:.2f} | {pct(curr['avg_freq'],prev['avg_freq'])} |")
A(""); A("---"); A("")

A("## Modulo 1 - Auditoria de Campanhas e Anuncios"); A("")
A("### Campanhas"); A("")
A("| Campanha | Gasto | CTR | CPM | Freq | Leads | CPL | Status |")
A("|---|---|---|---|---|---|---|---|")
for r in sorted(camp_curr, key=lambda x: float(x.get("spend", 0)), reverse=True):
    l = leads(r); sp = float(r.get("spend", 0)); c = sp/l if l else 0
    freq = float(r.get("frequency", 0))
    freq_tag = " FREQ" if freq >= 2.5 else ""
    st = status(l, c, avg_cpl)
    if freq >= 3.5 and st == "🟢 OK": st = "🟡 ATENCAO"
    A(f"| {r.get('campaign_name','---')} | {cur(sp)} | {float(r.get('ctr',0)):.2f}% | {cur(float(r.get('cpm',0)))} | {freq:.2f}{freq_tag} | {int(l)} | {cpl_str(sp,l)} | {st} |")
A("")

A("### Anuncios por Campanha"); A("")
camps_map = {}
for r in ad_curr:
    camps_map.setdefault(r.get("campaign_name", "Sem campanha"), []).append(r)
for cname, ads in camps_map.items():
    A(f"#### Campanha: {cname}"); A("")
    A("| Anuncio | Gasto | CTR | CPM | Freq | Leads | CPL | Status |")
    A("|---|---|---|---|---|---|---|---|")
    cs = sum(float(r.get("spend", 0)) for r in ads)
    cl = sum(leads(r) for r in ads)
    acpl = cs/cl if cl else 0
    with_l = sorted([r for r in ads if leads(r)>0], key=lambda r: float(r.get("spend",0))/leads(r))
    no_l   = sorted([r for r in ads if leads(r)==0], key=lambda r: float(r.get("spend",0)), reverse=True)
    best_found = False
    for r in with_l + no_l:
        l = leads(r); sp = float(r.get("spend", 0)); c = sp/l if l else 0
        freq = float(r.get("frequency", 0))
        star = ""
        if l > 0 and not best_found:
            star = " VENCEDOR"; best_found = True
        st = status(l, c, acpl)
        fw = " FREQ" if freq >= 3.0 else ""
        A(f"| {r.get('ad_name','---')[:38]}{star} | {cur(sp)} | {float(r.get('ctr',0)):.2f}% | {cur(float(r.get('cpm',0)))} | {freq:.2f}{fw} | {int(l)} | {cpl_str(sp,l)} | {st} |")
    A("")
A("---"); A("")

A("## Modulo 2 - Diagnostico de CPL (Causa Raiz)"); A("")
for r in sorted(camp_curr, key=lambda x: float(x.get("spend", 0)), reverse=True):
    l = leads(r); sp = float(r.get("spend", 0))
    if sp < 5: continue
    ctr  = float(r.get("ctr", 0))
    cpm  = float(r.get("cpm", 0))
    freq = float(r.get("frequency", 0))
    cn   = r.get("campaign_name", "Campanha")
    A(f"**{cn}**")
    if l == 0:
        A(f"- 🔴 {cur(sp)} investidos com 0 leads")
        if ctr < 0.8:
            A("- Causa raiz: CTR muito baixo -> criativo nao gera interesse no publico B2B hoteleiro")
            A("- Acao: testar novo criativo com angulo de pain point (filas, papel, staff)")
        else:
            A("- Causa raiz: CTR adequado mas sem conversao -> verificar formulario ou qualidade do publico")
            A("- Acao: revisar formulario e segmentacao do ad set")
    else:
        c = sp/l
        if c > avg_cpl * 1.8:
            pct_above = int((c/avg_cpl-1)*100)
            A(f"- 🔴 CPL {cpl_str(sp,l)} = {pct_above}% acima da media da conta ({cpl_str(curr['spend'],curr['leads'])})")
        elif c > avg_cpl * 1.2:
            A(f"- 🟡 CPL {cpl_str(sp,l)} acima da media ({cpl_str(curr['spend'],curr['leads'])})")
        else:
            A(f"- 🟢 CPL {cpl_str(sp,l)} dentro do esperado")
        causes = []
        if freq >= 2.5:
            causes.append(f"frequencia {freq:.2f} -> publico saturado")
        if curr["avg_cpm"] > 0 and cpm > curr["avg_cpm"] * 1.5:
            pct_cpm = int((cpm/curr["avg_cpm"]-1)*100)
            causes.append(f"CPM {cur(cpm)} ({pct_cpm}% acima da media) -> audience competitiva")
        if ctr < 0.8:
            causes.append(f"CTR {ctr:.2f}% baixo -> criativo fraco")
        if causes:
            A(f"- Causa raiz: {' | '.join(causes)}")
    A("")
A("---"); A("")

A("## Modulo 3 - Deteccao de Anomalias"); A("")
anomalies = []
for r in ad_curr:
    aname = r.get("ad_name", "")
    sp    = float(r.get("spend", 0))
    if sp < 3: continue
    l   = leads(r)
    ctr = float(r.get("ctr", 0))
    cpm = float(r.get("cpm", 0))
    prev_r = ad_prev_map.get(aname)
    if prev_r:
        prev_l   = leads(prev_r)
        prev_ctr = float(prev_r.get("ctr", 0))
        prev_cpm = float(prev_r.get("cpm", 0))
        d_ctr = pct_num(ctr, prev_ctr)
        d_cpm = pct_num(cpm, prev_cpm)
        if d_ctr is not None and d_ctr < -30:
            anomalies.append(f"| QUEDA DE CTR | {aname[:35]} | {prev_ctr:.2f}% -> {ctr:.2f}% ({d_ctr:.0f}%) | Verificar criativo |")
        if d_cpm is not None and d_cpm > 40:
            anomalies.append(f"| CPM SUBIU | {aname[:35]} | {cur(prev_cpm)} -> {cur(cpm)} ({d_cpm:+.0f}%) | Audience competitiva |")
        if prev_l > 2 and l == 0 and sp > 15:
            anomalies.append(f"| LEADS ZERADOS | {aname[:35]} | {int(prev_l)} leads -> 0 leads | Investigar urgente |")
    else:
        if sp > 20:
            anomalies.append(f"| NOVO ATIVO | {aname[:35]} | Sem historico anterior | Monitorar primeiros resultados |")
for r in ad_prev:
    aname = r.get("ad_name","")
    if aname and aname not in ad_curr_names and leads(r) > 0:
        anomalies.append(f"| DESAPARECEU | {aname[:35]} | Tinha {int(leads(r))} leads - nao aparece mais | Confirmar se foi pausado |")
if anomalies:
    A("| Tipo | Anuncio | Variacao | Acao |")
    A("|---|---|---|---|")
    for a in anomalies:
        A(a)
else:
    A("Nenhuma anomalia significativa detectada esta semana.")
A(""); A("---"); A("")

A("## Modulo 4 - Pacing Monitor"); A("")
A(f"Dia **{dias_mes}** de {last_day} do mes ({pct_mes:.0f}% do periodo).")
A(f"- Gasto semanal: **{cur(curr['spend'])}**")
A(f"- Projecao mensal (ritmo atual): **{cur(curr['spend']/7*30)}**")
if BUDGET_EST > 0:
    A(f"- Budget estimado: {cur(BUDGET_EST)}")
    if pacing_st == "NO RITMO":
        A(f"- Status: {pacing_icon} NO RITMO - gasto alinhado com o periodo do mes")
    elif pacing_st == "ACELERADO":
        A(f"- Status: {pacing_icon} ACELERADO (+{int(diff_p)}% acima do esperado) - risco de esgotar budget antes do fim do mes")
    else:
        A(f"- Status: {pacing_icon} LENTO ({int(diff_p)}% abaixo do esperado) - pode faltar entrega no fim do mes")
else:
    A("- Budget: a definir com o cliente — pacing nao calculado")
A(""); A("---"); A("")

A("## Modulo 5 - Fadiga de Criativos"); A("")
A("| Anuncio | Freq | CTR | Leads | Status | Recomendacao |")
A("|---|---|---|---|---|---|")
fadiga_found = False
for r in sorted(ad_curr, key=lambda x: float(x.get("frequency", 0)), reverse=True):
    sp   = float(r.get("spend", 0))
    freq = float(r.get("frequency", 0))
    if sp < 1: continue
    fadiga_found = True
    l = leads(r)
    if freq >= 3.5:   st2 = "FADIGA";    rec = "Pausar imediatamente"
    elif freq >= 2.5: st2 = "ATENCAO";   rec = "Criar novo criativo urgente"
    elif freq >= 1.8: st2 = "MONITORAR"; rec = "Preparar variacao"
    else:             st2 = "OK";        rec = "Manter"
    A(f"| {r.get('ad_name','---')[:35]} | {freq:.2f} | {float(r.get('ctr',0)):.2f}% | {int(l)} | {st2} | {rec} |")
if not fadiga_found:
    A("| Sem dados com gasto suficiente | --- | --- | --- | --- | --- |")
A(""); A("---"); A("")

A("## Modulo 6 - Analise de Copy e Criativos"); A("")
all_with_l = sorted([r for r in ad_curr if leads(r)>0 and float(r.get("spend",0))>2], key=lambda r: float(r.get("spend",0))/leads(r))
winners = all_with_l[:3]
losers  = sorted([r for r in ad_curr if leads(r)==0 and float(r.get("spend",0))>15], key=lambda r: float(r.get("spend",0)), reverse=True)[:3]
A("**Top criativos vencedores (menor CPL)**"); A("")
if winners:
    for i, r in enumerate(winners, 1):
        l = leads(r); sp = float(r.get("spend",0))
        A(f"{i}. **{r.get('ad_name','?')}** - CPL {cpl_str(sp,l)} | CTR {float(r.get('ctr',0)):.2f}% | {int(l)} leads")
    A("")
    A("**Acoes recomendadas:**")
    bn = winners[0].get("ad_name","?")
    A(f"- Escalar budget no criativo {bn} - melhor CPL da conta")
    A(f"- Testar variacao do hook de {bn} com angulo diferente (ex: etiquetas digitais vs. check-in online)")
    total_leads = int(curr["leads"])
    if total_leads < 100:
        A(f"- Continuar acumulando leads ({total_leads}/100) para ativar lookalike de hoteleiros")
    else:
        A(f"- {total_leads} leads acumulados - criar lookalike baseado nos convertidos")
else:
    A("- Nenhum criativo com leads no periodo - revisar criativos e targeting B2B hoteleiro")
A("")
if losers:
    A("**Criativos para pausar (gasto sem resultado)**"); A("")
    for r in losers:
        sp = float(r.get("spend",0))
        A(f"- {r.get('ad_name','?')} - {cur(sp)} gastos, 0 leads -> PAUSAR e redirecionar budget")
    A("")
A("---"); A("")

A("## Modulo 7 - Analise de Ad Sets e Publicos"); A("")
if adset_curr:
    A("| Ad Set | Gasto | Leads | CPL | CTR | CPM | Status |")
    A("|---|---|---|---|---|---|---|")
    as_total_l  = sum(leads(r) for r in adset_curr)
    as_total_sp = sum(float(r.get("spend",0)) for r in adset_curr)
    as_avg_cpl  = as_total_sp/as_total_l if as_total_l else 0
    for r in sorted(adset_curr, key=lambda x: float(x.get("spend",0)), reverse=True):
        sp = float(r.get("spend",0)); l = leads(r)
        if sp < 2: continue
        c   = sp/l if l else 0
        st3 = status(l, c, as_avg_cpl)
        A(f"| {r.get('adset_name','---')[:35]} | {cur(sp)} | {int(l)} | {cpl_str(sp,l)} | {float(r.get('ctr',0)):.2f}% | {cur(float(r.get('cpm',0)))} | {st3} |")
    A("")
    camp_adsets = {}
    for r in adset_curr:
        camp_adsets.setdefault(r.get("campaign_name",""), []).append(r.get("adset_name",""))
    for cn, asets in camp_adsets.items():
        if len(asets) > 2:
            A(f"- Campanha {cn} com {len(asets)} ad sets simultaneos - verificar sobreposicao de publico hoteleiro")
    A("")
else:
    A("Sem dados de ad sets disponiveis."); A("")
A("---"); A("")

A("## Plano de Acao"); A("")
A("| Prioridade | Acao | Impacto | Prazo |")
A("|---|---|---|---|")
acts = []
nm = today + datetime.timedelta(days=(7-today.weekday()))
nm_str = nm.strftime("%d/%m")
for r in ad_curr:
    sp = float(r.get("spend",0)); l = leads(r)
    if sp > 30 and l == 0:
        aname = r.get("ad_name","?")[:30]
        acts.append(f"| CRITICO | Pausar {aname} ({cur(sp)}, 0 leads) | Liberar budget | Imediato |")
for r in ad_curr:
    freq = float(r.get("frequency",0)); sp = float(r.get("spend",0))
    if freq >= 3.5 and sp > 5:
        aname = r.get("ad_name","?")[:28]
        acts.append(f"| CRITICO | Pausar fadiga: {aname} (freq {freq:.1f}) | Evitar CPM alto | Imediato |")
for r in ad_curr:
    l = leads(r); sp = float(r.get("spend",0))
    if l > 0 and avg_cpl > 0:
        c = sp/l
        if c > avg_cpl * 2 and sp > 50:
            aname = r.get("ad_name","?")[:26]
            acts.append(f"| ATENCAO | Revisar {aname} (CPL {cpl_str(sp,l)} vs media {cpl_str(curr['spend'],curr['leads'])}) | Reduzir CPL | {nm_str} |")
for r in ad_curr:
    freq = float(r.get("frequency",0)); sp = float(r.get("spend",0))
    if 2.5 <= freq < 3.5 and sp > 5:
        cname = r.get("campaign_name","?")[:20]
        acts.append(f"| ATENCAO | Criar novo criativo em {cname} (freq {freq:.1f}) | Prevenir fadiga | {nm_str} |")
if winners:
    bn = winners[0].get("ad_name","?")[:30]
    acts.append(f"| ESCALAR | Aumentar budget em {bn} | Reduzir CPL geral | {nm_str} |")
if not acts:
    acts.append("| OK | Manter atual - sem acoes criticas identificadas | --- | --- |")
for a in acts[:6]:
    A(a)
A(""); A("---"); A("")

A("## RESUMO FINAL PARA TRELLO - copie e cole quando quiser postar"); A("")
A(f"Meta Ads {CLIENT_NAME} - {today.strftime('%d/%m/%Y')}")
A(f"Gasto: {cur(curr['spend'])} | Leads: {int(curr['leads'])} | CPL: {cpl_str(curr['spend'],curr['leads'])}")
if curr['leads'] and prev['leads']:
    A(f"Variacao vs semana anterior: CPL {pct(curr['cpl_val'],prev['cpl_val'])} | Leads {pct(curr['leads'],prev['leads'])}")
A("")
for camp in camp_curr:
    cn = camp.get("campaign_name","Campanha")
    sp = float(camp.get("spend",0))
    if sp < 3: continue
    l    = leads(camp)
    freq = float(camp.get("frequency",0))
    camp_ads = [r for r in ad_curr if r.get("campaign_name")==cn]
    ads_wl   = sorted([r for r in camp_ads if leads(r)>0], key=lambda r: float(r.get("spend",0))/leads(r))
    ads_nl   = [r for r in camp_ads if leads(r)==0 and float(r.get("spend",0))>15]
    best     = ads_wl[0] if ads_wl else None
    A("---"); A("")
    A(f"Campanha: {cn}"); A("")
    A("O que esta funcionando:")
    if best:
        bl = leads(best); bc = float(best.get("spend",0))/bl
        A(f"- {best.get('ad_name','?')} - CTR {float(best.get('ctr',0)):.2f}% | CPL {cpl_str(float(best.get('spend',0)),bl)}")
    else:
        A(f"- {int(l)} leads gerados no periodo")
    if freq < 1.8:
        A(f"- Frequencia em {freq:.2f} - publico sem saturacao")
    A("")
    A("O que nao esta funcionando:")
    if ads_nl:
        for bad in ads_nl[:2]:
            A(f"- {bad.get('ad_name','?')} - {cur(float(bad.get('spend',0)))} gastos com 0 leads")
    elif freq >= 2.5:
        A(f"- Frequencia em {freq:.2f} - risco de saturacao do publico")
    else:
        A("- Sem problemas criticos identificados nesta campanha")
    A("")
    if best:
        bl = leads(best); bc = float(best.get("spend",0))/bl
        A(f"Criativo vencedor: {best.get('ad_name','?')} - CTR {float(best.get('ctr',0)):.2f}% | CPL {cpl_str(float(best.get('spend',0)),bl)}")
    else:
        A("Criativo vencedor: a definir - nenhum com leads no periodo")
    A("")
    A("O que precisa ser feito:")
    if ads_nl:
        A("- Pausar criativos sem resultado que consomem budget")
    if best:
        A(f"- Escalar budget no criativo {best.get('ad_name','?')}")
    if freq >= 2.5:
        A("- Criar novo criativo antes da frequencia atingir 3.5")
    if not ads_nl and not best and freq < 2.5:
        A("- Monitorar - sem acoes urgentes")
    A("")
A("---")

MESES = {1:'jan',2:'fev',3:'mar',4:'abr',5:'mai',6:'jun',7:'jul',8:'ago',9:'set',10:'out',11:'nov',12:'dez'}
mes_pasta = f"{MESES[today.month]}-{today.year}"
filepath = f"reports/data-know/hoteligy/{mes_pasta}/meta-report-{today.strftime('%Y-%m-%d')}.md"

report = "\n".join(L)

def save_to_github(filepath, content_str, commit_msg):
    api_url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/{filepath}"
    encoded = base64.b64encode(content_str.encode()).decode()
    for attempt in range(5):
        req = urllib.request.Request(api_url, headers={"Authorization": f"token {GITHUB_TOKEN}"})
        try:
            sha = json.loads(urllib.request.urlopen(req).read()).get("sha", "")
        except:
            sha = ""
        payload = {"message": commit_msg, "content": encoded}
        if sha:
            payload["sha"] = sha
        req = urllib.request.Request(api_url, data=json.dumps(payload).encode(),
            headers={"Authorization": f"token {GITHUB_TOKEN}", "Content-Type": "application/json"}, method="PUT")
        try:
            urllib.request.urlopen(req)
            print(f"Relatorio salvo: https://github.com/{GITHUB_REPO}/blob/main/{filepath}")
            return
        except urllib.error.HTTPError as e:
            err = e.read().decode()
            if e.code == 409 and attempt < 4:
                wait = (attempt + 1) * 15
                print(f"Conflito SHA (tentativa {attempt+1}/5) - aguardando {wait}s...")
                time.sleep(wait)
            else:
                print(f"Erro ao salvar: {err}")
                raise SystemExit(1)

save_to_github(filepath, report, f"feat: relatorio Meta Ads Hoteligy {today.strftime('%Y-%m-%d')}")
