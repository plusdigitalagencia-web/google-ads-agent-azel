#!/usr/bin/env python3
"""
meta_report_ai.py — Relatório Semanal Meta Ads (7 Módulos)
Meta Graph API apenas — sem dependência de Claude/Anthropic API.
Configurado por env vars: META_TOKEN, ACCOUNT_ID, CLIENT_NAME,
  CURRENCY, BUDGET_MONTHLY, REPORT_DIR, USE_MONTH_FOLDER, GH_PAT
"""
import os, json, datetime, base64, time, urllib.request, urllib.error, urllib.parse

TOKEN          = os.environ["META_TOKEN"]
ACCOUNT        = os.environ["ACCOUNT_ID"]
CLIENT_NAME    = os.environ["CLIENT_NAME"]
_CURR_RAW      = os.environ.get("CURRENCY", "€")
CURRENCY       = {"EUR": "€", "BRL": "R$", "USD": "$", "GBP": "£"}.get(_CURR_RAW, _CURR_RAW)
BUDGET_EST     = int(os.environ.get("BUDGET_MONTHLY", "0"))
REPORT_DIR     = os.environ.get("REPORT_DIR", "reports/data-know")
USE_MONTH      = os.environ.get("USE_MONTH_FOLDER", "false").lower() == "true"
GITHUB_TOKEN   = os.environ["GH_PAT"]
GITHUB_REPO    = "plusdigitalagencia-web/google-ads-agent-azel"
BASE           = "https://graph.facebook.com/v25.0"

today    = datetime.date.today()
p1_end   = today - datetime.timedelta(days=1)
p1_start = today - datetime.timedelta(days=7)
p2_end   = today - datetime.timedelta(days=8)
p2_start = today - datetime.timedelta(days=14)

if USE_MONTH:
    MESES = {1:'jan',2:'fev',3:'mar',4:'abr',5:'mai',6:'jun',
             7:'jul',8:'ago',9:'set',10:'out',11:'nov',12:'dez'}
    mes_pasta = f"{MESES[today.month]}-{today.year}"
    REPORT_DIR = f"{REPORT_DIR}/{mes_pasta}"

filepath = f"{REPORT_DIR}/meta-report-{today.strftime('%Y-%m-%d')}.md"

# ── helpers ──────────────────────────────────────────────────────────────────
def cur(v):
    return f"{CURRENCY}{v:.2f}"

def cpl_str(spend, l):
    return cur(spend / l) if l > 0 else "---"

def pct(a, b):
    if b == 0: return "---"
    v = ((a - b) / b) * 100
    return f"{'+'if v>0 else ''}{v:.1f}%"

def pct_num(a, b):
    if b == 0: return None
    return ((a - b) / b) * 100

def leads(row):
    for x in row.get("actions", []):
        if x.get("action_type") in ("lead","leadgen_other","onsite_conversion.lead_grouped"):
            return float(x.get("value", 0))
    return 0.0

def status(l, cpl_val, avg_cpl):
    if l == 0: return "🔴 CRÍTICO"
    if avg_cpl == 0: return "🟢 OK"
    if cpl_val <= avg_cpl * 1.2: return "🟢 OK"
    if cpl_val <= avg_cpl * 1.8: return "🟡 ATENÇÃO"
    return "🔴 CRÍTICO"

def totals(data):
    t = dict(spend=0, impressions=0, clicks=0, leads=0,
             cpm_s=0, ctr_s=0, freq_s=0, n=0)
    for r in data:
        t["spend"]       += float(r.get("spend", 0))
        t["impressions"] += int(r.get("impressions", 0))
        t["clicks"]      += int(r.get("clicks", 0))
        t["leads"]       += leads(r)
        t["cpm_s"]       += float(r.get("cpm", 0))
        t["ctr_s"]       += float(r.get("ctr", 0))
        t["freq_s"]      += float(r.get("frequency", 0))
        t["n"]           += 1
    n = t["n"] or 1
    t.update(avg_cpm=t["cpm_s"]/n, avg_ctr=t["ctr_s"]/n, avg_freq=t["freq_s"]/n)
    t["cpl_val"] = t["spend"]/t["leads"] if t["leads"] else 0
    return t

# ── fetch ────────────────────────────────────────────────────────────────────
def fetch(since, until, level="campaign"):
    fields = ("campaign_name,adset_name,ad_name,spend,clicks,impressions,"
              "reach,cpm,ctr,frequency,actions,cost_per_action_type")
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

print(f"Buscando dados da Meta API — {CLIENT_NAME} ({ACCOUNT})...")
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
pct_mes  = (dias_mes / last_day) * 100
proj_mes = (curr["spend"] / 7 * 30) if curr["spend"] else 0

diff_p = (proj_mes / BUDGET_EST * 100 - pct_mes) if BUDGET_EST else 0
if BUDGET_EST == 0:
    pacing_st, pacing_icon = "SEM META", "⚠️"
elif abs(diff_p) <= 10:
    pacing_st, pacing_icon = "NO RITMO", "🟢"
elif diff_p > 10:
    pacing_st, pacing_icon = "ACELERADO", "🔴"
else:
    pacing_st, pacing_icon = "LENTO", "🟡"

ad_prev_map   = {r.get("ad_name", ""): r for r in ad_prev}
avg_cpl       = curr["cpl_val"]
ad_curr_names = {r.get("ad_name","") for r in ad_curr}

# ── build report ─────────────────────────────────────────────────────────────
L = []; A = L.append

A(f"# Relatório Meta Ads - {CLIENT_NAME}")
A(f"**Período atual:** {p1_start.strftime('%d/%m/%Y')} a {p1_end.strftime('%d/%m/%Y')}")
A(f"**Período anterior:** {p2_start.strftime('%d/%m/%Y')} a {p2_end.strftime('%d/%m/%Y')}")
A(f"**Gerado em:** {today.strftime('%d/%m/%Y')} | **Conta:** {ACCOUNT}")
A(""); A("---"); A("")

# ── RESUMO ───────────────────────────────────────────────────────────────────
A("## Resumo Executivo"); A("")
A("| Métrica | Atual | Anterior | Variação |")
A("|---|---|---|---|")
A(f"| Gasto | {cur(curr['spend'])} | {cur(prev['spend'])} | {pct(curr['spend'],prev['spend'])} |")
A(f"| Leads | {int(curr['leads'])} | {int(prev['leads'])} | {pct(curr['leads'],prev['leads'])} |")
cpl_var = pct(curr['cpl_val'],prev['cpl_val']) if curr['leads'] and prev['leads'] else "---"
A(f"| CPL médio | {cpl_str(curr['spend'],curr['leads'])} | {cpl_str(prev['spend'],prev['leads'])} | {cpl_var} |")
A(f"| CTR médio | {curr['avg_ctr']:.2f}% | {prev['avg_ctr']:.2f}% | {pct(curr['avg_ctr'],prev['avg_ctr'])} |")
A(f"| CPM médio | {cur(curr['avg_cpm'])} | {cur(prev['avg_cpm'])} | {pct(curr['avg_cpm'],prev['avg_cpm'])} |")
A(f"| Frequência | {curr['avg_freq']:.2f} | {prev['avg_freq']:.2f} | {pct(curr['avg_freq'],prev['avg_freq'])} |")
A(""); A("---"); A("")

# ── MÓDULO 1 ─────────────────────────────────────────────────────────────────
A("## Módulo 1 — Auditoria de Campanhas e Anúncios"); A("")
A("### Campanhas"); A("")
A("| Campanha | Gasto | CTR | CPM | Freq | Leads | CPL | Status |")
A("|---|---|---|---|---|---|---|---|")
for r in sorted(camp_curr, key=lambda x: float(x.get("spend",0)), reverse=True):
    l=leads(r); sp=float(r.get("spend",0)); c=sp/l if l else 0
    freq=float(r.get("frequency",0))
    freq_tag=" ⚠️FREQ" if freq>=2.5 else ""
    st=status(l,c,avg_cpl)
    if freq>=3.5 and "🟢" in st: st="🟡 ATENÇÃO"
    A(f"| {r.get('campaign_name','---')} | {cur(sp)} | {float(r.get('ctr',0)):.2f}% | {cur(float(r.get('cpm',0)))} | {freq:.2f}{freq_tag} | {int(l)} | {cpl_str(sp,l)} | {st} |")
if not camp_curr:
    A("| *(nenhuma campanha ativa encontrada)* | — | — | — | — | — | — | — |")
A("")

A("### Anúncios por Campanha"); A("")
camps_map = {}
for r in ad_curr:
    camps_map.setdefault(r.get("campaign_name","Sem campanha"), []).append(r)
for cname, ads in camps_map.items():
    A(f"#### Campanha: {cname}"); A("")
    A("| Anúncio | Gasto | CTR | CPM | Freq | Leads | CPL | Status |")
    A("|---|---|---|---|---|---|---|---|")
    cs=sum(float(r.get("spend",0)) for r in ads)
    cl=sum(leads(r) for r in ads)
    acpl=cs/cl if cl else 0
    with_l=sorted([r for r in ads if leads(r)>0], key=lambda r: float(r.get("spend",0))/leads(r))
    no_l  =sorted([r for r in ads if leads(r)==0], key=lambda r: float(r.get("spend",0)), reverse=True)
    best_found=False
    for r in with_l+no_l:
        l=leads(r); sp=float(r.get("spend",0)); c=sp/l if l else 0
        freq=float(r.get("frequency",0))
        star=""
        if l>=5 and not best_found: star=" ⭐VENCEDOR"; best_found=True
        elif l>0 and l<5 and not best_found: star=" (candidato)"
        st=status(l,c,acpl)
        fw=" ⚠️FREQ" if freq>=3.0 else ""
        A(f"| {r.get('ad_name','---')[:40]}{star} | {cur(sp)} | {float(r.get('ctr',0)):.2f}% | {cur(float(r.get('cpm',0)))} | {freq:.2f}{fw} | {int(l)} | {cpl_str(sp,l)} | {st} |")
    A("")
A("---"); A("")

# ── MÓDULO 2 ─────────────────────────────────────────────────────────────────
A("## Módulo 2 — Diagnóstico de CPL (Causa Raiz)"); A("")
for r in sorted(camp_curr, key=lambda x: float(x.get("spend",0)), reverse=True):
    l=leads(r); sp=float(r.get("spend",0))
    if sp<5: continue
    ctr=float(r.get("ctr",0)); cpm=float(r.get("cpm",0)); freq=float(r.get("frequency",0))
    cn=r.get("campaign_name","Campanha")
    A(f"**{cn}**")
    if l==0:
        A(f"- 🔴 {cur(sp)} investidos com 0 leads")
        if ctr<0.8: A("- Causa raiz: CTR baixo → criativo não gera interesse")
        else:       A("- Causa raiz: CTR adequado mas sem conversão → formulário com atrito ou público desqualificado")
    else:
        c=sp/l
        if c>avg_cpl*1.8:
            pct_above=int((c/avg_cpl-1)*100)
            A(f"- 🔴 CPL {cpl_str(sp,l)} = {pct_above}% acima da média ({cpl_str(curr['spend'],curr['leads'])})")
        elif c>avg_cpl*1.2:
            A(f"- 🟡 CPL {cpl_str(sp,l)} acima da média ({cpl_str(curr['spend'],curr['leads'])})")
        else:
            A(f"- 🟢 CPL {cpl_str(sp,l)} dentro do esperado")
        causes=[]
        if freq>=2.5: causes.append(f"frequência {freq:.2f} → público saturado")
        if curr["avg_cpm"]>0 and cpm>curr["avg_cpm"]*1.5:
            causes.append(f"CPM {cur(cpm)} ({int((cpm/curr['avg_cpm']-1)*100)}% acima da média) → audience cara")
        if ctr<0.8: causes.append(f"CTR {ctr:.2f}% baixo → criativo fraco")
        if causes: A(f"- Causa raiz: {' | '.join(causes)}")
        else:       A("- Sem causa raiz clara — performance dentro do esperado")
    A("")
if not camp_curr: A("Nenhuma campanha ativa para diagnosticar."); A("")
A("---"); A("")

# ── MÓDULO 3 ─────────────────────────────────────────────────────────────────
A("## Módulo 3 — Detecção de Anomalias"); A("")
anomalies=[]
for r in ad_curr:
    aname=r.get("ad_name",""); sp=float(r.get("spend",0))
    if sp<3: continue
    l=leads(r); ctr=float(r.get("ctr",0)); cpm=float(r.get("cpm",0))
    prev_r=ad_prev_map.get(aname)
    if prev_r:
        prev_l=leads(prev_r); prev_ctr=float(prev_r.get("ctr",0)); prev_cpm=float(prev_r.get("cpm",0))
        d_ctr=pct_num(ctr,prev_ctr); d_cpm=pct_num(cpm,prev_cpm)
        if d_ctr is not None and d_ctr<-30:
            anomalies.append(f"| ⚠️ QUEDA DE CTR | {aname[:35]} | {prev_ctr:.2f}%→{ctr:.2f}% ({d_ctr:.0f}%) | Verificar criativo |")
        if d_cpm is not None and d_cpm>40:
            anomalies.append(f"| ⚠️ SPIKE CPM | {aname[:35]} | {cur(prev_cpm)}→{cur(cpm)} ({d_cpm:+.0f}%) | Audience mais competitiva |")
        if prev_l>2 and l==0 and sp>15:
            anomalies.append(f"| 🔴 LEADS ZERADOS | {aname[:35]} | {int(prev_l)} leads → 0 leads | Investigar urgente |")
    else:
        if sp>20: anomalies.append(f"| 🆕 NOVO ATIVO | {aname[:35]} | Sem histórico anterior | Monitorar |")
for r in ad_prev:
    aname=r.get("ad_name","")
    if aname and aname not in ad_curr_names and leads(r)>0:
        anomalies.append(f"| ⚠️ DESAPARECEU | {aname[:35]} | Tinha {int(leads(r))} leads — ausente | Confirmar se pausado |")
if anomalies:
    A("| Tipo | Anúncio | Variação | Ação |"); A("|---|---|---|---|")
    for a in anomalies: A(a)
else:
    A("✅ Nenhuma anomalia significativa detectada esta semana.")
A(""); A("---"); A("")

# ── MÓDULO 4 ─────────────────────────────────────────────────────────────────
A("## Módulo 4 — Pacing Monitor"); A("")
A(f"Dia **{dias_mes}** de {last_day} do mês ({pct_mes:.0f}% do período).")
A(f"- Gasto semanal: **{cur(curr['spend'])}**")
A(f"- Projeção mensal (ritmo atual): **{cur(proj_mes)}**")
if BUDGET_EST:
    A(f"- Budget mensal estimado: {cur(BUDGET_EST)}")
    A(f"- Status: {pacing_icon} {pacing_st}")
    if pacing_st=="LENTO":    A(f"  → Projeção {int(100-proj_mes/BUDGET_EST*100)}% abaixo do budget — revisar limites de gasto diário")
    elif pacing_st=="ACELERADO": A(f"  → Projeção {int(proj_mes/BUDGET_EST*100-100)}% acima do budget — risco de esgotar antes do fim do mês")
else:
    A("- Status: ⚠️ Budget mensal não definido — definir para habilitar pacing correto")
A(""); A("---"); A("")

# ── MÓDULO 5 ─────────────────────────────────────────────────────────────────
A("## Módulo 5 — Fadiga de Criativos"); A("")
A("| Anúncio | Freq | CTR | Leads | Status | Recomendação |")
A("|---|---|---|---|---|---|")
fadiga_found=False
for r in sorted(ad_curr, key=lambda x: float(x.get("frequency",0)), reverse=True):
    sp=float(r.get("spend",0)); freq=float(r.get("frequency",0))
    if sp<1: continue
    fadiga_found=True
    l=leads(r)
    if freq>=3.5:   st2="🔴 FADIGA";    rec="Pausar imediatamente"
    elif freq>=2.5: st2="🟡 ATENÇÃO";   rec="Criar novo criativo urgente"
    elif freq>=1.8: st2="🟡 MONITORAR"; rec="Preparar variação"
    else:           st2="🟢 OK";        rec="Manter"
    A(f"| {r.get('ad_name','---')[:38]} | {freq:.2f} | {float(r.get('ctr',0)):.2f}% | {int(l)} | {st2} | {rec} |")
if not fadiga_found:
    A("| Sem criativos com gasto suficiente | — | — | — | — | — |")
A(""); A("---"); A("")

# ── MÓDULO 6 ─────────────────────────────────────────────────────────────────
A("## Módulo 6 — Análise de Copy e Criativos"); A("")
all_with_l=sorted([r for r in ad_curr if leads(r)>=5 and float(r.get("spend",0))>2],
                  key=lambda r: float(r.get("spend",0))/leads(r))
candidates=sorted([r for r in ad_curr if 0<leads(r)<5 and float(r.get("spend",0))>2],
                  key=lambda r: float(r.get("spend",0))/leads(r))
losers    =sorted([r for r in ad_curr if leads(r)==0 and float(r.get("spend",0))>15],
                  key=lambda r: float(r.get("spend",0)), reverse=True)
A("**Criativos vencedores (≥5 leads, menor CPL)**"); A("")
if all_with_l:
    for i,r in enumerate(all_with_l[:3],1):
        l=leads(r); sp=float(r.get("spend",0))
        A(f"{i}. **{r.get('ad_name','?')}** — CPL {cpl_str(sp,l)} | CTR {float(r.get('ctr',0)):.2f}% | {int(l)} leads")
else:
    A("- Nenhum criativo atingiu 5 leads no período")
A("")
if candidates:
    A("**Candidatos (1–4 leads — aguardar volume)**"); A("")
    for r in candidates[:3]:
        l=leads(r); sp=float(r.get("spend",0))
        A(f"- {r.get('ad_name','?')} — CPL {cpl_str(sp,l)} | {int(l)} leads | aguardar mínimo 5 para conclusão")
    A("")
if losers:
    A("**Para pausar (gasto >15 sem leads)**"); A("")
    for r in losers[:4]:
        sp=float(r.get("spend",0))
        A(f"- 🔴 {r.get('ad_name','?')} — {cur(sp)} gastos, 0 leads → PAUSAR")
    A("")
A("---"); A("")

# ── MÓDULO 7 ─────────────────────────────────────────────────────────────────
A("## Módulo 7 — Análise de Ad Sets e Públicos"); A("")
if adset_curr:
    A("| Ad Set | Gasto | Leads | CPL | CTR | CPM | Freq | Status |")
    A("|---|---|---|---|---|---|---|---|")
    as_total_l =sum(leads(r) for r in adset_curr)
    as_total_sp=sum(float(r.get("spend",0)) for r in adset_curr)
    as_avg_cpl =as_total_sp/as_total_l if as_total_l else 0
    for r in sorted(adset_curr, key=lambda x: float(x.get("spend",0)), reverse=True):
        sp=float(r.get("spend",0)); l=leads(r)
        if sp<2: continue
        c=sp/l if l else 0
        st3=status(l,c,as_avg_cpl)
        A(f"| {r.get('adset_name','---')[:38]} | {cur(sp)} | {int(l)} | {cpl_str(sp,l)} | {float(r.get('ctr',0)):.2f}% | {cur(float(r.get('cpm',0)))} | {float(r.get('frequency',0)):.2f} | {st3} |")
    A("")
    camp_adsets={}
    for r in adset_curr:
        camp_adsets.setdefault(r.get("campaign_name",""),[]).append(r.get("adset_name",""))
    for cn,asets in camp_adsets.items():
        if len(asets)>2:
            A(f"- ⚠️ Campanha **{cn}** com {len(asets)} ad sets simultâneos — verificar sobreposição de público")
else:
    A("Sem dados de ad sets disponíveis.")
A(""); A("---"); A("")

# ── PLANO DE AÇÃO ─────────────────────────────────────────────────────────────
A("## Plano de Ação"); A("")
A("| Prioridade | Ação | Impacto | Prazo |"); A("|---|---|---|---|")
acts=[]
nm=today+datetime.timedelta(days=(7-today.weekday())%7 or 7)
nm_str=nm.strftime("%d/%m")
for r in ad_curr:
    sp=float(r.get("spend",0)); l=leads(r)
    if sp>30 and l==0:
        acts.append(f"| 🔴 CRÍTICO | Pausar {r.get('ad_name','?')[:28]} ({cur(sp)}, 0 leads) | Liberar budget | Imediato |")
for r in ad_curr:
    freq=float(r.get("frequency",0)); sp=float(r.get("spend",0))
    if freq>=3.5 and sp>5:
        acts.append(f"| 🔴 CRÍTICO | Pausar fadiga: {r.get('ad_name','?')[:26]} (freq {freq:.1f}) | Evitar CPM alto | Imediato |")
for r in ad_curr:
    l=leads(r); sp=float(r.get("spend",0))
    if l>0 and avg_cpl>0:
        c=sp/l
        if c>avg_cpl*2 and sp>50:
            acts.append(f"| 🟡 ATENÇÃO | Revisar {r.get('ad_name','?')[:24]} (CPL {cpl_str(sp,l)} vs média {cpl_str(curr['spend'],curr['leads'])}) | Reduzir CPL | {nm_str} |")
for r in ad_curr:
    freq=float(r.get("frequency",0)); sp=float(r.get("spend",0))
    if 2.5<=freq<3.5 and sp>5:
        acts.append(f"| 🟡 ATENÇÃO | Criar criativo para {r.get('campaign_name','?')[:22]} (freq {freq:.1f}) | Prevenir fadiga | {nm_str} |")
if all_with_l:
    bn=all_with_l[0].get("ad_name","?")[:30]
    acts.append(f"| 🟢 ESCALAR | Aumentar budget em {bn} | Reduzir CPL geral | {nm_str} |")
if BUDGET_EST and pacing_st=="LENTO":
    acts.append(f"| 🟡 ATENÇÃO | Pacing lento — projeção {cur(proj_mes)} vs budget {cur(BUDGET_EST)} | Ajustar limites de gasto diário | Imediato |")
if not acts:
    acts.append("| 🟢 OK | Sem ações críticas identificadas — manter e monitorar | — | — |")
for a in acts[:6]: A(a)
A(""); A("---"); A("")

# ── BLOCO TRELLO (formato SOP) ────────────────────────────────────────────────
A("---"); A("")
A("## 🟦 RESUMO FINAL PARA TRELLO — copie e cole quando quiser postar"); A("")
A(f"📊 Meta Ads {CLIENT_NAME} — {today.strftime('%d/%m/%Y')}")
A(f"💰 Gasto: {cur(curr['spend'])} | 🎯 Leads: {int(curr['leads'])} | 📉 CPL: {cpl_str(curr['spend'],curr['leads'])}")
if curr['leads'] and prev['leads']:
    A(f"Variação vs semana anterior: CPL {pct(curr['cpl_val'],prev['cpl_val'])} | Leads {pct(curr['leads'],prev['leads'])}")
if BUDGET_EST:
    A(f"Pacing: {pacing_icon} {pacing_st} — Projeção {cur(proj_mes)} vs Budget {cur(BUDGET_EST)} ({pct_mes:.0f}% do mês decorrido)")
A("")
for camp in camp_curr:
    cn=camp.get("campaign_name","Campanha"); sp=float(camp.get("spend",0))
    if sp<3: continue
    l=leads(camp); freq=float(camp.get("frequency",0))
    camp_ads=[r for r in ad_curr if r.get("campaign_name")==cn]
    ads_wl=sorted([r for r in camp_ads if leads(r)>0], key=lambda r: float(r.get("spend",0))/leads(r))
    ads_nl=[r for r in camp_ads if leads(r)==0 and float(r.get("spend",0))>15]
    best=ads_wl[0] if ads_wl else None
    A("---"); A("")
    A(f"📌 Campanha: {cn}"); A("")
    A("✅ O que está funcionando:")
    if best:
        bl=leads(best)
        A(f"- {best.get('ad_name','?')} — CTR {float(best.get('ctr',0)):.2f}% | CPL {cpl_str(float(best.get('spend',0)),bl)}")
    elif l>0: A(f"- {int(l)} leads gerados no período")
    else: A("- Nenhum criativo com resultado positivo")
    if freq<1.8: A(f"- Frequência em {freq:.2f} — público sem saturação")
    A(""); A("❌ O que não está funcionando:")
    if ads_nl:
        for bad in ads_nl[:2]: A(f"- {bad.get('ad_name','?')} — {cur(float(bad.get('spend',0)))} gastos, 0 leads")
    elif freq>=2.5: A(f"- Frequência em {freq:.2f} — risco de saturação")
    else: A("- Sem problemas críticos nesta campanha")
    A("")
    if best:
        bl=leads(best)
        A(f"⭐ Criativo vencedor: {best.get('ad_name','?')} — CTR {float(best.get('ctr',0)):.2f}% | CPL {cpl_str(float(best.get('spend',0)),bl)}")
    else: A("⭐ Criativo vencedor: a definir — nenhum com volume suficiente no período")
    A(""); A("🔧 O que precisa ser feito:")
    if ads_nl: A(f"- Pausar criativos sem resultado que consomem budget ({', '.join(b.get('ad_name','?')[:25] for b in ads_nl[:2])})")
    if best:   A(f"- Escalar budget no criativo {best.get('ad_name','?')}")
    if freq>=2.5: A("- Criar novo criativo antes da frequência atingir 3,5")
    if not ads_nl and not best and freq<2.5: A("- Monitorar — sem ações urgentes")
    A("")
A("---")

# ── SAVE TO GITHUB ────────────────────────────────────────────────────────────
report="\n".join(L)

def save_to_github(fp, content_str, commit_msg):
    api_url=f"https://api.github.com/repos/{GITHUB_REPO}/contents/{fp}"
    encoded=base64.b64encode(content_str.encode()).decode()
    for attempt in range(5):
        req=urllib.request.Request(api_url, headers={"Authorization":f"token {GITHUB_TOKEN}"})
        try: sha=json.loads(urllib.request.urlopen(req).read()).get("sha","")
        except: sha=""
        payload={"message":commit_msg,"content":encoded}
        if sha: payload["sha"]=sha
        req=urllib.request.Request(api_url, data=json.dumps(payload).encode(),
            headers={"Authorization":f"token {GITHUB_TOKEN}","Content-Type":"application/json"}, method="PUT")
        try:
            urllib.request.urlopen(req)
            print(f"Salvo: https://github.com/{GITHUB_REPO}/blob/main/{fp}")
            return
        except urllib.error.HTTPError as e:
            err=e.read().decode()
            if e.code==409 and attempt<4:
                wait=(attempt+1)*15
                print(f"Conflito SHA (tentativa {attempt+1}/5) — aguardando {wait}s...")
                time.sleep(wait)
            else:
                print(f"Erro ao salvar: {err}"); raise SystemExit(1)

save_to_github(filepath, report, f"feat: relatorio Meta Ads {CLIENT_NAME} {today.strftime('%Y-%m-%d')}")
