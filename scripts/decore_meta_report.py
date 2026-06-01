import os, json, urllib.request
from datetime import datetime

TOKEN   = os.environ["DECORE_META_ACCESS_TOKEN"]
ACCOUNT = "act_386946248899004"
BASE    = "https://graph.facebook.com/v25.0"

def api_get(path, extra=""):
    url = f"{BASE}{path}?access_token={TOKEN}{extra}"
    try:
        res = urllib.request.urlopen(url)
        return json.loads(res.read())
    except urllib.error.HTTPError as e:
        print(f"  API error {e.code} em {path}: {e.read().decode()[:150]}")
        return {}

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

today       = datetime.now()
# Período atual: mês corrente (1 até ontem)
year        = today.year
month       = today.month
since       = f"{year}-{month:02d}-01"
until       = (today).strftime("%Y-%m-%d")
# Mês anterior
if month == 1:
    prev_year, prev_month = year - 1, 12
else:
    prev_year, prev_month = year, month - 1
import calendar
last_day_prev = calendar.monthrange(prev_year, prev_month)[1]
since_prev  = f"{prev_year}-{prev_month:02d}-01"
until_prev  = f"{prev_year}-{prev_month:02d}-{last_day_prev:02d}"
report_date = today.strftime("%Y-%m-%d")

data      = fetch_insights(since, until, "campaign")
data_prev = fetch_insights(since_prev, until_prev, "campaign")
data_ads  = fetch_insights(since, until, "ad", ",ad_name,adset_name,quality_ranking,engagement_rate_ranking,conversion_rate_ranking")
prev_by_name = {c.get("campaign_name"): c for c in data_prev.get("data", [])}

RANKING = {
    "ABOVE_AVERAGE": "🟢 Acima", "AVERAGE": "🟡 Médio",
    "BELOW_AVERAGE_10": "🔴 Baixo (10%)", "BELOW_AVERAGE_20": "🔴 Baixo (20%)",
    "BELOW_AVERAGE_35": "🔴 Baixo (35%)", "UNKNOWN": "⚪ —",
}

lines = [
    "# Relatório Meta Ads — Decore",
    f"**Período:** {since} a {until}  |  Plus Digital",
    "**Foco:** Captação de Leads (Revendedores) | Pixel: Lead",
    "",
]

total_spend = 0.0
total_leads = 0
camp_meta   = []

for camp in data.get("data", []):
    name    = camp.get("campaign_name", "—")
    spend   = float(camp.get("spend", 0))
    clicks  = int(camp.get("clicks", 0))
    impr    = int(camp.get("impressions", 0))
    cpm     = float(camp.get("cpm", 0))
    ctr     = float(camp.get("ctr", 0))
    freq    = float(camp.get("frequency", 0))
    reach   = int(camp.get("reach", 0))
    leads   = val_lead(camp.get("actions", []))
    cpl     = spend / leads if leads > 0 else 0.0
    status  = "🟢" if cpl > 0 and cpl < 20 else ("🟡" if cpl < 35 else "🔴")

    total_spend += spend
    total_leads += int(leads)

    prev = prev_by_name.get(name, {})
    camp_meta.append({
        "name": name, "spend": spend, "cpm": cpm, "ctr": ctr,
        "freq": freq, "leads": int(leads), "cpl": cpl,
        "prev_cpm": float(prev.get("cpm", 0)),
        "prev_ctr": float(prev.get("ctr", 0)),
        "prev_leads": val_lead(prev.get("actions", [])),
        "prev_spend": float(prev.get("spend", 0)),
    })

    lines += [
        f"## 🟢 {name}",
        "| Métrica | Valor |", "|---|---|",
        f"| Status CPL | {status} R${cpl:.2f} |",
        f"| Gasto | R${spend:.2f} |",
        f"| Leads | {int(leads)} |",
        f"| CPL | R${cpl:.2f} |",
        f"| Impressões | {impr:,} |",
        f"| Cliques | {clicks:,} |",
        f"| CTR | {ctr:.2f}% |",
        f"| CPM | R${cpm:.2f} |",
        f"| Alcance | {reach:,} |",
        f"| Frequência | {freq:.1f} |",
        "",
    ]

cpl_total = total_spend / total_leads if total_leads > 0 else 0.0
lines += [
    "---",
    f"**Total investido:** R${total_spend:.2f}  |  **Leads totais:** {total_leads}  |  **CPL médio:** R${cpl_total:.2f}",
    "",
]

# ── Comparativo Mês Anterior ───────────────────────────────────────────────────
lines += ["---", "## 📊 Comparativo com Mês Anterior", "",
    f"| Campanha | Leads ({prev_month:02d}/{prev_year}) | Leads ({month:02d}/{year}) | Δ Leads | CPL anterior | CPL atual | Δ CPL |",
    "|---|---|---|---|---|---|---|"]
for c in camp_meta:
    prev_l = int(c["prev_leads"])
    curr_l = c["leads"]
    delta_l = curr_l - prev_l
    delta_l_pct = f"{delta_l:+d} ({((curr_l-prev_l)/prev_l*100):+.0f}%)" if prev_l > 0 else f"{delta_l:+d}"
    prev_cpl = c["prev_spend"] / prev_l if prev_l > 0 else 0.0
    curr_cpl = c["cpl"]
    delta_cpl = f"R${curr_cpl-prev_cpl:+.2f} ({((curr_cpl-prev_cpl)/prev_cpl*100):+.0f}%)" if prev_cpl > 0 else "—"
    lines.append(f"| {c['name'][:40]} | {prev_l} | {curr_l} | {delta_l_pct} | R${prev_cpl:.2f} | R${curr_cpl:.2f} | {delta_cpl} |")
lines.append("")

# ── Audit criativo ─────────────────────────────────────────────────────────────
lines += ["---", "## 🔍 Audit de Criativos", ""]
health = 100; alerts = []
for c in camp_meta:
    if c["freq"] > 4:
        health -= 10; alerts.append(f"🔴 **{c['name'][:40]}** — Frequência {c['freq']:.1f} — trocar criativo")
    elif c["freq"] > 3:
        health -= 5; alerts.append(f"🟡 **{c['name'][:40]}** — Frequência {c['freq']:.1f} — preparar novo criativo")
    if c["prev_cpm"] > 0:
        d = (c["cpm"] - c["prev_cpm"]) / c["prev_cpm"]
        if d > 0.30: health -= 10; alerts.append(f"🔴 **{c['name'][:40]}** — CPM subiu {d*100:.0f}%")
        elif d > 0.15: health -= 5; alerts.append(f"🟡 **{c['name'][:40]}** — CPM subiu {d*100:.0f}%")
    if c["prev_ctr"] > 0:
        d = (c["ctr"] - c["prev_ctr"]) / c["prev_ctr"]
        if d < -0.20: health -= 10; alerts.append(f"🔴 **{c['name'][:40]}** — CTR caiu {abs(d)*100:.0f}%")
        elif d < -0.15: health -= 5; alerts.append(f"🟡 **{c['name'][:40]}** — CTR caiu {abs(d)*100:.0f}%")
health = max(0, health)
h_e = "🟢" if health >= 80 else ("🟡" if health >= 60 else "🔴")
lines += [f"**Score de Saúde:** {h_e} {health}/100", ""]
lines += ["| Campanha | Freq | CTR atual | CTR anterior | Δ CTR | CPM atual | Δ CPM | Status |",
           "|---|---|---|---|---|---|---|---|"]
for c in camp_meta:
    ctr_v = f"{((c['ctr']-c['prev_ctr'])/c['prev_ctr']*100):+.0f}%" if c["prev_ctr"] > 0 else "—"
    cpm_v = f"{((c['cpm']-c['prev_cpm'])/c['prev_cpm']*100):+.0f}%" if c["prev_cpm"] > 0 else "—"
    fs = "🔴 Crítico" if c["freq"] > 4 else ("🟡 Atenção" if c["freq"] > 3 else "🟢 OK")
    lines.append(f"| {c['name'][:35]} | {c['freq']:.1f} | {c['ctr']:.2f}% | {c['prev_ctr']:.2f}% | {ctr_v} | R${c['cpm']:.2f} | {cpm_v} | {fs} |")
lines.append("")
if alerts:
    lines += ["### ⚠️ Alertas", ""]
    for a in alerts: lines.append(f"- {a}")
    lines.append("")
if data_ads.get("data"):
    lines += ["### Rankings de Qualidade dos Anúncios", "",
               "| Anúncio | Qualidade | Engajamento | Conversão | Gasto |",
               "|---|---|---|---|---|"]
    for ad in data_ads["data"]:
        lines.append(f"| {ad.get('ad_name','—')[:40]} | {RANKING.get(ad.get('quality_ranking','UNKNOWN'),'⚪')} | {RANKING.get(ad.get('engagement_rate_ranking','UNKNOWN'),'⚪')} | {RANKING.get(ad.get('conversion_rate_ranking','UNKNOWN'),'⚪')} | R${float(ad.get('spend',0)):.2f} |")
    lines.append("")

lines += [
    "---",
    f"**Total investido:** R${total_spend:.2f}  |  **Leads:** {total_leads}  |  **CPL:** R${cpl_total:.2f}",
    f"*Gerado automaticamente | Plus Digital | {today.strftime('%d/%m/%Y')}*",
]

os.makedirs("reports/decore", exist_ok=True)
path = f"reports/decore/meta-report-{report_date}.md"
with open(path, "w") as f:
    f.write("\n".join(lines))
print(f"Relatório salvo: {path}")
