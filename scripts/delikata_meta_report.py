import os, json, urllib.request
from datetime import datetime, timedelta

TOKEN   = os.environ["DELIKATA_META_ACCESS_TOKEN"]
ACCOUNT = "act_532861400590268"
BASE    = "https://graph.facebook.com/v25.0"

def fetch(since, until, level="campaign"):
    fields = "campaign_name,spend,clicks,impressions,reach,cpm,ctr,frequency,actions,action_values,purchase_roas"
    tr = f'{{"since":"{since}","until":"{until}"}}'
    url = (f"{BASE}/{ACCOUNT}/insights?fields={fields}&level={level}"
           f"&time_range={tr}&action_breakdowns=action_type&access_token={TOKEN}")
    res = urllib.request.urlopen(url)
    return json.loads(res.read())

def val(lst, key):
    for x in (lst or []):
        if x.get("action_type") == key:
            return float(x["value"])
    return 0.0

today = datetime.now()
until = (today - timedelta(days=1)).strftime("%Y-%m-%d")
since = (today - timedelta(days=7)).strftime("%Y-%m-%d")

data = fetch(since, until)

report_date = today.strftime("%Y-%m-%d")
lines = [
    f"# Relatório Meta Ads — Delikata",
    f"**Período:** {since} a {until} | Plus Digital",
    f"**Foco:** Compras (ROAS) | Pixel: Compra",
    "",
]

total_spend    = 0.0
total_purchases = 0
total_revenue  = 0.0

for camp in data.get("data", []):
    name    = camp.get("campaign_name", "—")
    spend   = float(camp.get("spend", 0))
    clicks  = int(camp.get("clicks", 0))
    impr    = int(camp.get("impressions", 0))
    cpm     = float(camp.get("cpm", 0))
    ctr     = float(camp.get("ctr", 0))
    freq    = float(camp.get("frequency", 0))
    actions = camp.get("actions", [])
    action_values = camp.get("action_values", [])

    purchases = val(actions, "offsite_conversion.fb_pixel_purchase")
    revenue   = val(action_values, "offsite_conversion.fb_pixel_purchase")

    # ROAS: pode vir direto do campo purchase_roas ou calculado
    roas_raw = camp.get("purchase_roas", [])
    if roas_raw and isinstance(roas_raw, list):
        roas = float(roas_raw[0].get("value", 0))
    elif revenue > 0 and spend > 0:
        roas = revenue / spend
    else:
        roas = 0.0

    cpa = spend / purchases if purchases > 0 else 0.0

    if roas >= 3.0:
        status = "🟢"
    elif roas >= 1.0:
        status = "🟡"
    else:
        status = "🔴"

    total_spend     += spend
    total_purchases += int(purchases)
    total_revenue   += revenue

    lines.append(f"## 🟢 {name}")
    lines.append(f"| Métrica | Valor |")
    lines.append(f"|---|---|")
    lines.append(f"| Status | {status} ROAS {roas:.2f}x |")
    lines.append(f"| Gasto | R${spend:.2f} |")
    lines.append(f"| Receita | R${revenue:.2f} |")
    lines.append(f"| Compras | {int(purchases)} |")
    lines.append(f"| CPA | R${cpa:.2f} |")
    lines.append(f"| Impressões | {impr:,} |")
    lines.append(f"| Cliques | {clicks:,} |")
    lines.append(f"| CTR | {ctr:.2f}% |")
    lines.append(f"| CPM | R${cpm:.2f} |")
    lines.append(f"| Frequência | {freq:.1f} |")
    lines.append("")

total_roas = total_revenue / total_spend if total_spend > 0 else 0.0
lines.append(f"---")
lines.append(f"**Total investido:** R${total_spend:.2f} | **Total receita:** R${total_revenue:.2f} | **ROAS geral:** {total_roas:.2f}x | **Compras:** {total_purchases}")
lines.append(f"*Gerado automaticamente | Plus Digital | {today.strftime('%d/%m/%Y')}*")

os.makedirs("reports/delikata", exist_ok=True)
path = f"reports/delikata/meta-report-{report_date}.md"
with open(path, "w") as f:
    f.write("\n".join(lines))
print(f"Relatório salvo: {path}")
