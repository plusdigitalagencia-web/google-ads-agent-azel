#!/usr/bin/env python3
"""
Dra. Fernanda Guimaraes - Relatorio Semanal Meta Ads
Conta: act_1062379715841653 | Moeda: BRL
Roda toda segunda via GitHub Actions as 07:00 BRT
"""
import os, urllib.request, urllib.error, urllib.parse
import json, datetime, base64

TOKEN        = os.environ["DUOSFERA_META_TOKEN"]
GITHUB_TOKEN = os.environ["GH_PAT"]
ACCOUNT      = "act_1062379715841653"
BASE         = "https://graph.facebook.com/v25.0"
GITHUB_REPO  = "plusdigitalagencia-web/google-ads-agent-azel"

today    = datetime.date.today()
_rs, _re, _ps, _pe = os.environ.get("REPORT_START",""), os.environ.get("REPORT_END",""), os.environ.get("REPORT_PREV_START",""), os.environ.get("REPORT_PREV_END","")
if _rs and _re and _ps and _pe:
    p1_start = datetime.date.fromisoformat(_rs)
    p1_end   = datetime.date.fromisoformat(_re)
    p2_start = datetime.date.fromisoformat(_ps)
    p2_end   = datetime.date.fromisoformat(_pe)
    mes      = p1_end.strftime("%b-%y").lower()
    suffix   = f"{p1_start.isoformat()}_a_{p1_end.isoformat()}"
else:
    p1_end   = today - datetime.timedelta(days=1)
    p1_start = today - datetime.timedelta(days=7)
    p2_end   = today - datetime.timedelta(days=8)
    p2_start = today - datetime.timedelta(days=14)
    mes      = today.strftime("%b-%y").lower()   # ex: jun-26
    suffix   = today.strftime("%Y-%m-%d")

def fetch(since, until, level="campaign"):
    fields = "campaign_name,adset_name,ad_name,spend,clicks,impressions,reach,cpm,ctr,frequency,actions,cost_per_action_type"
    params = urllib.parse.urlencode({
        "fields": fields, "level": level,
        "time_range": json.dumps({"since": str(since), "until": str(until)}),
        "action_breakdowns": "action_type",
        "access_token": TOKEN, "limit": 100
    })
    try:
        resp = urllib.request.urlopen(f"{BASE}/{ACCOUNT}/insights?{params}")
        return json.loads(resp.read()).get("data", [])
    except Exception as e:
        print(f"Erro {level}: {e}")
        return []

def conversas(row):
    for x in row.get("actions", []):
        if x.get("action_type") == "onsite_conversion.messaging_conversation_started_7d":
            return float(x.get("value", 0))
    return 0.0

def cpl_str(spend, l):
    return f"R${spend/l:.2f}" if l > 0 else "---"

def pct(a, b):
    if b == 0: return "---"
    v = ((a - b) / b) * 100
    return f"{'+'if v>0 else ''}{v:.1f}%"

def totals(data):
    t = dict(spend=0,impressions=0,clicks=0,conversas=0,cpm_s=0,ctr_s=0,freq_s=0,n=0)
    for r in data:
        t["spend"]+=float(r.get("spend",0)); t["impressions"]+=int(r.get("impressions",0))
        t["clicks"]+=int(r.get("clicks",0)); t["conversas"]+=conversas(r)
        t["cpm_s"]+=float(r.get("cpm",0)); t["ctr_s"]+=float(r.get("ctr",0))
        t["freq_s"]+=float(r.get("frequency",0)); t["n"]+=1
    n=t["n"] or 1
    t.update(avg_cpm=t["cpm_s"]/n, avg_ctr=t["ctr_s"]/n, avg_freq=t["freq_s"]/n)
    t["cpl_val"]=t["spend"]/t["conversas"] if t["conversas"] else 0
    return t

print("Buscando dados Meta Ads Dra. Fernanda...")
camp_curr=fetch(p1_start,p1_end,"campaign")
camp_prev=fetch(p2_start,p2_end,"campaign")
ad_curr  =fetch(p1_start,p1_end,"ad")
curr=totals(camp_curr); prev=totals(camp_prev)

budget_est=700  # R$ 700/mes — atualizar conforme ajuste de verba
dias_mes=today.day
last_day=(datetime.date(today.year,today.month%12+1,1)-datetime.timedelta(days=1)).day if today.month<12 else 31
pct_mes=(dias_mes/last_day)*100
pct_gasto=(curr["spend"]/budget_est*100) if budget_est else 0
diff_p=pct_gasto-pct_mes
pacing_st="NO RITMO" if abs(diff_p)<=10 else ("ACELERADO" if diff_p>10 else "LENTO")

L=[]; A=L.append
A(f"# Relatorio Meta Ads - Dra. Fernanda Guimaraes")
A(f"**Periodo atual:** {p1_start.strftime('%d/%m/%Y')} a {p1_end.strftime('%d/%m/%Y')}")
A(f"**Periodo anterior:** {p2_start.strftime('%d/%m/%Y')} a {p2_end.strftime('%d/%m/%Y')}")
A(f"**Gerado em:** {today.strftime('%d/%m/%Y')} | **Conta:** {ACCOUNT}")
A(""); A("---"); A("")

A("## Resumo Executivo"); A("")
A("| Metrica | Atual | Anterior | Variacao |")
A("|---|---|---|---|")
A(f"| Gasto | R${curr['spend']:.2f} | R${prev['spend']:.2f} | {pct(curr['spend'],prev['spend'])} |")
A(f"| Conversas | {int(curr['conversas'])} | {int(prev['conversas'])} | {pct(curr['conversas'],prev['conversas'])} |")
A(f"| C/Conv medio | {cpl_str(curr['spend'],curr['conversas'])} | {cpl_str(prev['spend'],prev['conversas'])} | {pct(curr['cpl_val'],prev['cpl_val']) if curr['conversas'] and prev['conversas'] else '---'} |")
A(f"| Impressoes | {int(curr['impressions']):,} | {int(prev['impressions']):,} | {pct(curr['impressions'],prev['impressions'])} |")
A(f"| Cliques | {int(curr['clicks'])} | {int(prev['clicks'])} | {pct(curr['clicks'],prev['clicks'])} |")
A(f"| CTR medio | {curr['avg_ctr']:.2f}% | {prev['avg_ctr']:.2f}% | {pct(curr['avg_ctr'],prev['avg_ctr'])} |")
A(f"| CPM medio | R${curr['avg_cpm']:.2f} | R${prev['avg_cpm']:.2f} | {pct(curr['avg_cpm'],prev['avg_cpm'])} |")
A(f"| Frequencia | {curr['avg_freq']:.2f} | {prev['avg_freq']:.2f} | {pct(curr['avg_freq'],prev['avg_freq'])} |")
A("")

A("---"); A("")
A("## Modulo 1 - Auditoria de Campanhas"); A("")
A("| Campanha | Gasto | CTR | CPM | Freq | Conversas | C/Conv | Status |")
A("|---|---|---|---|---|---|---|---|")
avg_cpl=curr["cpl_val"]
for r in sorted(camp_curr, key=lambda x:float(x.get("spend",0)),reverse=True):
    l=conversas(r);sp=float(r.get("spend",0));c=sp/l if l else 0
    freq=float(r.get("frequency",0))
    st="OK" if (l>0 and c<=avg_cpl*1.2) else ("ATENCAO" if l>0 else "CRITICO")
    fw=" FREQ-ALTA" if freq>=2.5 else ""
    A(f"| {r.get('campaign_name','---')} | R${sp:.2f} | {float(r.get('ctr',0)):.2f}% | R${float(r.get('cpm',0)):.2f} | {freq:.2f}{fw} | {int(l)} | {cpl_str(sp,l)} | {st} |")
A("")

A("### Analise por Anuncio"); A("")
camps_map={}
for r in ad_curr:
    camps_map.setdefault(r.get("campaign_name","Sem campanha"),[]).append(r)

for cname,ads in camps_map.items():
    A(f"#### Campanha: {cname}"); A("")
    A("| Anuncio | Gasto | CTR | CPM | Freq | Conversas | C/Conv | Status |")
    A("|---|---|---|---|---|---|---|---|")
    cs=sum(float(r.get("spend",0)) for r in ads)
    cl=sum(conversas(r) for r in ads)
    acpl=cs/cl if cl else 0
    with_l=sorted([r for r in ads if conversas(r)>0],key=lambda r:float(r.get("spend",0))/conversas(r))
    no_l=sorted([r for r in ads if conversas(r)==0],key=lambda r:float(r.get("spend",0)),reverse=True)
    best_found=False
    for r in with_l+no_l:
        l=conversas(r);sp=float(r.get("spend",0));c=sp/l if l else 0
        freq=float(r.get("frequency",0))
        star=""
        if l>0 and not best_found:
            star=" VENCEDOR"; best_found=True
        st=("OK" if c<=acpl*1.2 else ("ATENCAO" if c<=acpl*1.5 else "CRITICO")) if l>0 else ("CRITICO" if sp>20 else "SEM-GASTO")
        fw=" FREQ-ALTA" if freq>=3.0 else ""
        A(f"| {r.get('ad_name','---')[:38]}{star} | R${sp:.2f} | {float(r.get('ctr',0)):.2f}% | R${float(r.get('cpm',0)):.2f} | {freq:.2f}{fw} | {int(l)} | {cpl_str(sp,l)} | {st} |")
    A("")

A("---"); A("")
A("## Modulo 4 - Pacing Monitor"); A("")
A(f"Dia {dias_mes} de {last_day} ({pct_mes:.0f}% do mes). Gasto semanal: R${curr['spend']:.2f}")
A(f"Projecao mensal: R${curr['spend']/7*30:.0f} | Budget: R${budget_est}")
A(f"Status: {pacing_st}"); A("")

A("---"); A("")
A("## Modulo 5 - Fadiga de Criativos"); A("")
A("| Anuncio | Freq | CTR | Status | Recomendacao |")
A("|---|---|---|---|---|")
for r in sorted(ad_curr,key=lambda x:float(x.get("frequency",0)),reverse=True):
    sp=float(r.get("spend",0));freq=float(r.get("frequency",0))
    if sp<1: continue
    st="FADIGA" if freq>=3.5 else ("ATENCAO" if freq>=2.5 else "OK")
    rec="Pausar" if freq>=3.5 else ("Novo criativo" if freq>=2.5 else "Manter")
    A(f"| {r.get('ad_name','---')[:35]} | {freq:.2f} | {float(r.get('ctr',0)):.2f}% | {st} | {rec} |")
A("")

A("---"); A("")
A("## Plano de Acao"); A("")
A("| Pri | Acao | Impacto | Prazo |")
A("|---|---|---|---|")
acts=[]
nm=today+datetime.timedelta(days=(7-today.weekday()))
for r in ad_curr:
    sp=float(r.get("spend",0));l=conversas(r)
    if sp>30 and l==0:
        acts.append(f"| CRITICO | Pausar '{r.get('ad_name','?')[:28]}' (R${sp:.0f}, 0 conversas) | Liberar budget | Imediato |")
for r in ad_curr:
    l=conversas(r);sp=float(r.get("spend",0))
    if l>0:
        c=sp/l
        if c>avg_cpl*2 and sp>50:
            acts.append(f"| ATENCAO | Revisar '{r.get('ad_name','?')[:26]}' (C/Conv R${c:.0f} vs media R${avg_cpl:.0f}) | Reduzir C/Conv | {nm.strftime('%d/%m')} |")
for r in ad_curr:
    freq=float(r.get("frequency",0));sp=float(r.get("spend",0))
    if freq>=3.5 and sp>5:
        acts.append(f"| CRITICO | Pausar por fadiga: '{r.get('ad_name','?')[:26]}' (freq {freq:.1f}) | Evitar CPM alto | Imediato |")
    elif freq>=2.5 and sp>5:
        acts.append(f"| ATENCAO | Novo criativo em '{r.get('campaign_name','?')[:20]}' | Prevenir fadiga | {nm.strftime('%d/%m')} |")
if not acts:
    acts.append("| 1 | Monitorar - sem acoes criticas identificadas | --- | --- |")
for i,a in enumerate(acts[:5],1):
    A(a)
A("")

A("---"); A("")
A("## RESUMO FINAL PARA TRELLO"); A("")
A(f"Meta Ads Dra. Fernanda Guimaraes - {today.strftime('%d/%m/%Y')}")
A(f"Gasto: R${curr['spend']:.2f} | Conversas: {int(curr['conversas'])} | C/Conv: {cpl_str(curr['spend'],curr['conversas'])} ({pct(curr['cpl_val'],prev['cpl_val']) if curr['conversas'] and prev['conversas'] else '---'} vs semana anterior)")
A("")

for camp in camp_curr:
    cn=camp.get("campaign_name","Campanha")
    sp=float(camp.get("spend",0));l=conversas(camp);freq=float(camp.get("frequency",0))
    camp_ads=[r for r in ad_curr if r.get("campaign_name")==cn]
    ads_wl=sorted([r for r in camp_ads if conversas(r)>0],key=lambda r:float(r.get("spend",0))/conversas(r))
    ads_nl=[r for r in camp_ads if conversas(r)==0 and float(r.get("spend",0))>20]
    best=ads_wl[0] if ads_wl else None
    A(f"---"); A("")
    A(f"CAMPANHA: {cn}"); A("")
    A("O QUE ESTA FUNCIONANDO:")
    if best:
        bl=conversas(best);bc=float(best.get("spend",0))/bl
        A(f"- Criativo \"{best.get('ad_name','?')[:40]}\" - CTR {float(best.get('ctr',0)):.2f}% | C/Conv R${bc:.2f}")
    else:
        A(f"- {int(l)} conversas geradas no periodo")
    if freq<2.0: A(f"- Frequencia em {freq:.2f} - publico sem saturacao")
    A("")
    A("O QUE NAO ESTA FUNCIONANDO:")
    if ads_nl:
        for bad in ads_nl[:2]:
            A(f"- \"{bad.get('ad_name','?')[:40]}\" - R${float(bad.get('spend',0)):.2f} gastos com 0 conversas")
    if freq>=2.5: A(f"- Frequencia em {freq:.2f} - risco de fadiga")
    if not ads_nl and freq<2.5: A("- Sem problemas criticos identificados")
    A("")
    A("CRIATIVO VENCEDOR:")
    if best:
        bl=conversas(best);bc=float(best.get("spend",0))/bl
        A(f"- {best.get('ad_name','?')[:40]} - CTR {float(best.get('ctr',0)):.2f}% | C/Conv R${bc:.2f}")
    else: A("- A definir")
    A("")
    A("O QUE PRECISA SER FEITO:")
    if ads_nl: A("- Pausar criativos sem resultado que consomem budget")
    if best: A("- Dar mais budget para o criativo vencedor escalar")
    if freq>=2.5: A("- Criar novo criativo antes da frequencia atingir 3.5")
    A("")

A("---")

report="\n".join(L)
filepath=f"reports/DUOSFERA/dra-fernanda/{mes}/meta-dra-fernanda-report-{suffix}.md"
api_url=f"https://api.github.com/repos/{GITHUB_REPO}/contents/{filepath}"
req=urllib.request.Request(api_url,headers={"Authorization":f"token {GITHUB_TOKEN}"})
try:
    sha=json.loads(urllib.request.urlopen(req).read()).get("sha","")
except: sha=""
payload={"message":f"feat: relatorio Meta Ads Dra Fernanda {today.strftime('%Y-%m-%d')}","content":base64.b64encode(report.encode()).decode()}
if sha: payload["sha"]=sha
req=urllib.request.Request(api_url,data=json.dumps(payload).encode(),
    headers={"Authorization":f"token {GITHUB_TOKEN}","Content-Type":"application/json"},method="PUT")
try:
    urllib.request.urlopen(req)
    print(f"Relatorio salvo: https://github.com/{GITHUB_REPO}/blob/main/{filepath}")
except urllib.error.HTTPError as e:
    print(f"Erro ao salvar: {e.read().decode()}")
