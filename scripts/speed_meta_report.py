import os, json, urllib.request, calendar
from datetime import datetime

TOKEN   = os.environ["META_ACCESS_TOKEN"]
ACCOUNT = "act_870928146781077"
BASE    = "https://graph.facebook.com/v25.0"

def fetch_insights(since, until, level, extra_fields=""):
    fields = f"campaign_name,spend,clicks,impressions,cpm,ctr,frequency,reach,actions{extra_fields}"
    tr = f'{{"since":"{since}","until":"{until}"}}'
    url = (f"{BASE}/{ACCOUNT}/insights?fields={fields}&level={level}"
           f"&time_range={tr}&action_breakdowns=action_type&access_token={TOKEN}")
    try:
        res = urllib.request.urlopen(url)
        return json.loads(res.read())
    except urllib.error.HTTPError as e:
        print(f"  Insights error {e.code}: {e.read().decode()[:150]}")
        return {"data": []}

def val_lead(actions):
    for x in (actions or []):
        if x.get("action_type") in ("offsite_conversion.fb_pixel_lead", "lead"):
            return float(x["value"])
    return 0.0

today      = datetime.now()
year, month = today.year, today.month
until      = os.environ.get("UNTIL_DATE") or today.strftime("%Y-%m-%d")
since      = os.environ.get("SINCE_DATE") or f"{year}-{month:02d}-01"
# If since is from a different month than today, use that month for prev comparison
_since_dt  = datetime.strptime(since, "%Y-%m-%d")
year, month = _since_dt.year, _since_dt.month
if month == 1:
    prev_year, prev_month = year - 1, 12
else:
    prev_year, prev_month = year, month - 1
last_day_prev = calendar.monthrange(prev_year, prev_month)[1]
since_prev = f"{prev_year}-{prev_month:02d}-01"
until_prev = f"{prev_year}-{prev_month:02d}-{last_day_prev:02d}"
report_date = today.strftime("%Y-%m-%d")

data         = fetch_insights(since, until, "campaign")
data_prev    = fetch_insights(since_prev, until_prev, "campaign")
data_ads     = fetch_insights(since, until, "ad",
                              ",ad_name,quality_ranking,engagement_rate_ranking,conversion_rate_ranking")
prev_by_name = {c.get("campaign_name"): c for c in data_prev.get("data", [])}

RANKING = {
    "ABOVE_AVERAGE": "🟢 Acima", "AVERAGE": "🟡 Médio",
    "BELOW_AVERAGE_10": "🔴 Baixo (10%)", "BELOW_AVERAGE_20": "🔴 Baixo (20%)",
    "BELOW_AVERAGE_35": "🔴 Baixo (35%)", "UNKNOWN": "⚪ —",
}

total_spend = 0.0; total_leads = 0
camp_meta   = []

for camp in data.get("data", []):
    name   = camp.get("campaign_name", "—")
    spend  = float(camp.get("spend", 0))
    clicks = int(camp.get("clicks", 0))
    impr   = int(camp.get("impressions", 0))
    cpm    = float(camp.get("cpm", 0))
    ctr    = float(camp.get("ctr", 0))
    freq   = float(camp.get("frequency", 0))
    reach  = int(camp.get("reach", 0))
    leads  = val_lead(camp.get("actions", []))
    cpl    = spend / leads if leads > 0 else 0.0
    prev   = prev_by_name.get(name, {})
    prev_l = val_lead(prev.get("actions", []))
    total_spend += spend; total_leads += int(leads)
    camp_meta.append({
        "name": name, "spend": spend, "clicks": clicks, "impr": impr,
        "cpm": cpm, "ctr": ctr, "freq": freq, "reach": reach,
        "leads": int(leads), "cpl": cpl,
        "prev_cpm": float(prev.get("cpm", 0)),
        "prev_ctr": float(prev.get("ctr", 0)),
        "prev_leads": int(prev_l),
        "prev_spend": float(prev.get("spend", 0)),
    })

cpl_total = total_spend / total_leads if total_leads > 0 else 0.0
prev_total_leads = sum(c["prev_leads"] for c in camp_meta)
prev_total_spend = sum(c["prev_spend"] for c in camp_meta)
prev_cpl_total   = prev_total_spend / prev_total_leads if prev_total_leads > 0 else 0.0

deu_certo = []
nao_deu   = []
melhorias = []

if camp_meta:
    best = min(camp_meta, key=lambda c: c["cpl"] if c["cpl"] > 0 else 9999)
    if best["cpl"] > 0:
        deu_certo.append(f"**{best['name'][:50]}** entregou o melhor CPL da conta: R${best['cpl']:.2f} por lead.")

for c in camp_meta:
    if c["prev_ctr"] > 0 and c["ctr"] > c["prev_ctr"]:
        d = (c["ctr"] - c["prev_ctr"]) / c["prev_ctr"] * 100
        if d > 5:
            deu_certo.append(f"CTR de **{c['name'][:40]}** subiu {d:.0f}% — criativo funcionando bem.")

if prev_total_leads > 0:
    delta_leads = total_leads - prev_total_leads
    if delta_leads >= 0:
        deu_certo.append(f"Volume de leads mantido ou crescendo: {prev_total_leads} → {total_leads} ({delta_leads:+d}).")
    else:
        nao_deu.append(f"Volume de leads caiu {abs(delta_leads)} ({delta_leads/prev_total_leads*100:.0f}%): {prev_total_leads} → {total_leads} com orçamento similar.")

if prev_cpl_total > 0 and cpl_total > prev_cpl_total:
    d = (cpl_total - prev_cpl_total) / prev_cpl_total * 100
    if d > 5:
        nao_deu.append(f"CPL médio subiu {d:.0f}%: R${prev_cpl_total:.2f} → R${cpl_total:.2f}. Tendência de alta que precisa ser revertida.")

for c in camp_meta:
    if c["prev_ctr"] > 0:
        d = (c["ctr"] - c["prev_ctr"]) / c["prev_ctr"] * 100
        if d < -10:
            nao_deu.append(f"CTR de **{c['name'][:40]}** caiu {abs(d):.0f}% — sinal de início de fadiga criativa.")

for c in camp_meta:
    if c["prev_cpm"] > 0:
        d = (c["cpm"] - c["prev_cpm"]) / c["prev_cpm"] * 100
        if d > 15:
            nao_deu.append(f"CPM de **{c['name'][:40]}** subiu {d:.0f}% — leilão mais caro.")

if camp_meta and best["cpl"] > 0 and best["cpl"] < 20:
    melhorias.append(f"**Escalar {best['name'][:40]}:** CPL de R${best['cpl']:.2f} justifica aumento de budget.")
for c in camp_meta:
    if c["prev_ctr"] > 0 and (c["ctr"] - c["prev_ctr"]) / c["prev_ctr"] < -0.10:
        melhorias.append(f"**Renovar criativo de {c['name'][:40]}:** CTR em queda — novo hook pode recuperar a performance.")
melhorias.append("**Testar público LookAlike** a partir dos leads já convertidos para melhorar qualidade e reduzir CPL.")
melhorias.append("**Testar novo ângulo de copy** (delivery, e-commerce, alimentício) fora do ângulo atual de Cartuchos.")

lines = [
    "# Relatório Meta Ads — SpeedMais Gráfica",
    f"**Período:** {since} a {until}  |  Plus Digital",
    "**Foco:** Captação de Leads (Formulário/Pixel) | Pixel: offsite_conversion.fb_pixel_lead",
    "",
    "---",
    "",
    "## 🧭 Resumo Executivo",
    "",
    "### ✅ O que deu certo",
    "",
]
for item in deu_certo:
    lines.append(f"- {item}")
lines += [
    "",
    "### ❌ O que não deu certo",
    "",
]
for item in nao_deu:
    lines.append(f"- {item}")
lines += [
    "",
    "### 🚀 O que podemos fazer para melhorar",
    "",
]
for i, item in enumerate(melhorias, 1):
    lines.append(f"{i}. {item}")

lines += ["", "---", "", "## 📋 Campanhas Ativas", ""]

for c in camp_meta:
    cpl_s = "🟢" if c["cpl"] < 20 else ("🟡" if c["cpl"] < 35 else "🔴")
    lines += [
        f"## 🟢 {c['name']}",
        "| Métrica | Valor |", "|---|---|",
        f"| Status CPL | {cpl_s} R${c['cpl']:.2f} |",
        f"| Gasto | R${c['spend']:.2f} |",
        f"| Leads | {c['leads']} |",
        f"| CPL | R${c['cpl']:.2f} |",
        f"| Impressões | {c['impr']:,} |",
        f"| Cliques | {c['clicks']:,} |",
        f"| CTR | {c['ctr']:.2f}% |",
        f"| CPM | R${c['cpm']:.2f} |",
        f"| Alcance | {c['reach']:,} |",
        f"| Frequência | {c['freq']:.1f} |",
        "",
    ]

lines += [
    "---",
    f"**Total investido:** R${total_spend:.2f}  |  **Leads totais:** {total_leads}  |  **CPL médio:** R${cpl_total:.2f}",
    "",
    "---",
    "## 📊 Comparativo com Mês Anterior",
    "",
    f"| Métrica | {prev_month:02d}/{prev_year} | {month:02d}/{year} | Variação |",
    "|---|---|---|---|",
    f"| Gasto total | R${prev_total_spend:.2f} | R${total_spend:.2f} | {(total_spend-prev_total_spend)/prev_total_spend*100:+.1f}% {'🟢' if total_spend <= prev_total_spend*1.05 else '🟡'} |" if prev_total_spend > 0 else "| Gasto total | — | R${:.2f} | — |".format(total_spend),
    f"| Leads totais | {prev_total_leads} | {total_leads} | **{total_leads-prev_total_leads:+d} ({(total_leads-prev_total_leads)/prev_total_leads*100:+.1f}%) {'🟢' if total_leads >= prev_total_leads else '🔴'}** |" if prev_total_leads > 0 else f"| Leads totais | — | {total_leads} | — |",
    f"| CPL médio | R${prev_cpl_total:.2f} | R${cpl_total:.2f} | **{(cpl_total-prev_cpl_total)/prev_cpl_total*100:+.1f}% {'🟢' if cpl_total <= prev_cpl_total else '🔴'}** |" if prev_cpl_total > 0 else f"| CPL médio | — | R${cpl_total:.2f} | — |",
    "",
]

lines += ["---", "## 🔍 Audit de Criativos", ""]
health = 100; alerts = []
for c in camp_meta:
    if c["freq"] > 4:   health -= 10; alerts.append(f"🔴 **{c['name'][:40]}** — Frequência {c['freq']:.1f} — trocar criativo")
    elif c["freq"] > 3: health -= 5;  alerts.append(f"🟡 **{c['name'][:40]}** — Frequência {c['freq']:.1f} — preparar novo criativo")
    if c["prev_cpm"] > 0:
        d = (c["cpm"] - c["prev_cpm"]) / c["prev_cpm"]
        if d > 0.30:   health -= 10; alerts.append(f"🔴 **{c['name'][:40]}** — CPM subiu {d*100:.0f}%")
        elif d > 0.15: health -= 5;  alerts.append(f"🟡 **{c['name'][:40]}** — CPM subiu {d*100:.0f}%")
    if c["prev_ctr"] > 0:
        d = (c["ctr"] - c["prev_ctr"]) / c["prev_ctr"]
        if d < -0.20:   health -= 10; alerts.append(f"🔴 **{c['name'][:40]}** — CTR caiu {abs(d)*100:.0f}%")
        elif d < -0.10: health -= 5;  alerts.append(f"🟡 **{c['name'][:40]}** — CTR caiu {abs(d)*100:.0f}%")
health = max(0, health)
h_e = "🟢" if health >= 80 else ("🟡" if health >= 60 else "🔴")
lines += [f"**Score de Saúde:** {h_e} {health}/100", ""]
if alerts:
    lines += ["### ⚠️ Alertas", ""]
    for a in alerts: lines.append(f"- {a}")
    lines.append("")

if data_ads.get("data"):
    lines += ["### Rankings de Qualidade", "",
               "| Anúncio | Qualidade | Engajamento | Conversão | Gasto |", "|---|---|---|---|---|"]
    for ad in data_ads["data"]:
        lines.append(f"| {ad.get('ad_name','—')[:40]} | {RANKING.get(ad.get('quality_ranking','UNKNOWN'),'⚪')} | {RANKING.get(ad.get('engagement_rate_ranking','UNKNOWN'),'⚪')} | {RANKING.get(ad.get('conversion_rate_ranking','UNKNOWN'),'⚪')} | R${float(ad.get('spend',0)):.2f} |")
    lines.append("")

lines += [
    "---",
    f"**Total investido:** R${total_spend:.2f}  |  **Leads:** {total_leads}  |  **CPL:** R${cpl_total:.2f}",
    f"*Gerado automaticamente | Plus Digital | {today.strftime('%d/%m/%Y')}*",
]

output_file = os.environ.get("OUTPUT_FILE", f"reports/ASSUCAR/speed/meta-speed-report-{report_date}.md")
os.makedirs(os.path.dirname(output_file), exist_ok=True)
with open(output_file, "w") as f:
    f.write("\n".join(lines))
print(f"Relatório salvo: {output_file}")
