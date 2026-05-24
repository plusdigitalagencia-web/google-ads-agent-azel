import os, json, urllib.request
from datetime import datetime, timedelta

TOKEN   = os.environ["META_ACCESS_TOKEN"]
ACCOUNT = "act_1258930228369219"
BASE    = "https://graph.facebook.com/v25.0"

def fetch(since, until, level="campaign"):
    fields = "campaign_name,adset_name,spend,clicks,impressions,reach,cpm,ctr,frequency,actions,cost_per_action_type"
    tr = f'{{"since":"{since}","until":"{until}"}}'
    url = (f"{BASE}/{ACCOUNT}/insights?fields={fields}&level={level}"
           f"&time_range={tr}&action_breakdowns=action_type&access_token={TOKEN}")
    res = urllib.request.urlopen(url)
    return json.loads(res.read())

def val(lst, key):
    for x in (lst or []):
        if x["action_type"] == key:
            return float(x["value"])
    return 0.0

today     = datetime.now()
until     = (today - timedelta(days=1)).strftime("%Y-%m-%d")
since     = (today - timedelta(days=7)).strftime("%Y-%m-%d")
since_ant = (today - timedelta(days=14)).strftime("%Y-%m-%d")
until_ant = (today - timedelta(days=8)).strftime("%Y-%m-%d")

data     = fetch(since, until)
data_ant = fetch(since_ant, until_ant)

report_date = today.strftime("%Y-%m-%d")
lines = [f"# Relatório Meta Ads — Dra. Cejana", f"**Período:** {since} a {until} | Plus Digital
"]

total_spend = 0
total_conv  = 0

for camp in data.get("data", []):
    name    = camp.get("campaign_name", "—")
    spend   = float(camp.get("spend", 0))
    clicks  = int(camp.get("clicks", 0))
    impr    = int(camp.get("impressions", 0))
    cpm     = float(camp.get("cpm", 0))
    ctr     = float(camp.get("ctr", 0))
    freq    = float(camp.get("frequency", 0))
    actions = camp.get("actions", [])
    conv    = val(actions, "onsite_conversion.messaging_conversation_started_7d")
    leads   = val(actions, "onsite_conversion.lead")
    total_spend += spend
    total_conv  += conv
    cpr = spend / conv if conv > 0 else 0
    status = "🟢" if cpr < 15 else ("🟡" if cpr < 30 else "🔴")
    lines.append(f"## 🟢 {name}")
    lines.append(f"| Métrica | Valor |")
    lines.append(f"|---|---|")
    lines.append(f"| Gasto | R${spend:.2f} |")
    lines.append(f"| Impressões | {impr:,} |")
    lines.append(f"| Cliques | {clicks:,} |")
    lines.append(f"| CTR | {ctr:.2f}% |")
    lines.append(f"| CPM | R${cpm:.2f} |")
    lines.append(f"| Frequência | {freq:.1f} |")
    lines.append(f"| Conversas WPP | {int(conv)} |")
    lines.append(f"| Leads | {int(leads)} |")
    lines.append(f"| CPR | R${cpr:.2f} {status} |")
    lines.append("")

lines.append(f"---")
lines.append(f"**Total investido:** R${total_spend:.2f} | **Total conversas:** {int(total_conv)}")
lines.append(f"*Gerado automaticamente | Plus Digital | {today.strftime('%d/%m/%Y')}*")

os.makedirs("reports/cejana", exist_ok=True)
path = f"reports/cejana/meta-report-{report_date}.md"
with open(path, "w") as f:
    f.write("
".join(lines))
print(f"Relatório salvo: {path}")
