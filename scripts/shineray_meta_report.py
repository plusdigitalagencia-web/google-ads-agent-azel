import os, json, urllib.request
from datetime import datetime, timezone, timedelta

TOKEN = os.environ["META_ACCESS_TOKEN"]
APP_ID = os.environ["META_APP_ID"]
APP_SECRET = os.environ["META_APP_SECRET"]
ACCOUNT = "act_1057721942577752"
BASE = "https://graph.facebook.com/v25.0"

def refresh_token():
    url = (f"{BASE}/oauth/access_token?grant_type=fb_exchange_token"
           f"&client_id={APP_ID}&client_secret={APP_SECRET}&fb_exchange_token={TOKEN}")
    return json.loads(urllib.request.urlopen(url).read()).get("access_token", TOKEN)

def fetch(token, preset):
    fields = "campaign_name,spend,actions,cost_per_action_type,impressions,cpm,reach,frequency"
    url = (f"{BASE}/{ACCOUNT}/insights?fields={fields}&level=campaign"
           f"&date_preset={preset}&action_breakdowns=action_type&access_token={token}")
    return json.loads(urllib.request.urlopen(url).read())

def val(lst, key, field="action_type"):
    for x in lst or []:
        if x[field] == key:
            return float(x["value"])
    return 0.0

def status(cpr):
    if cpr <= 0: return "⚪ Sem dados"
    if cpr < 3:  return "🟢 Ideal"
    if cpr <= 6: return "🟡 Atenção"
    return "🔴 Crítico"

BRT = timezone(timedelta(hours=-3))
now = datetime.now(BRT)
today = now.strftime("%Y-%m-%d")

try:
    token = refresh_token()
except:
    token = TOKEN

d7  = fetch(token, "last_7d")
dt  = fetch(token, "today")

def parse(data, min_spend=0):
    rows, ts, tc = [], 0.0, 0
    for c in data.get("data", []):
        spend = float(c.get("spend", 0))
        if spend <= min_spend: continue
        ac = c.get("actions", [])
        cp = c.get("cost_per_action_type", [])
        conv  = int(val(ac, "onsite_conversion.messaging_conversation_started_7d"))
        conn  = int(val(ac, "onsite_conversion.total_messaging_connection"))
        reply = int(val(ac, "onsite_conversion.messaging_first_reply"))
        cpr   = val(cp, "onsite_conversion.messaging_conversation_started_7d")
        cpm   = float(c.get("cpm", 0))
        rows.append(dict(name=c["campaign_name"], spend=spend,
                         conv=conv, conn=conn, reply=reply,
                         cpr=cpr, cpm=cpm, st=status(cpr)))
        ts += spend; tc += conv
    cpr_g = ts / tc if tc else 0
    return rows, ts, tc, cpr_g

r7, ts7, tc7, cpr7 = parse(d7)
rt, tst, tct, cprt = parse(dt)

def tbl_today(rows, ts, tc, cpr):
    h = "| Campanha | Investimento | Conversas | CPR | Andromeda |\n|---|---|---|---|---|\n"
    body = "".join(f"| {r['name']} | R${r['spend']:.2f} | {r['conv']} | R${r['cpr']:.2f} | {r['st']} |\n" for r in rows)
    foot = f"| **TOTAL** | **R${ts:.2f}** | **{tc}** | **R${cpr:.2f}** | {status(cpr)} |\n" if rows else "| — | Sem dados ainda | — | — | — |\n"
    return h + body + foot

def tbl_7d(rows, ts, tc, cpr):
    h = "| Campanha | Investimento | Conversas | CPR | CPM | Andromeda |\n|---|---|---|---|---|---|\n"
    body = "".join(f"| {r['name']} | R${r['spend']:.2f} | {r['conv']} | R${r['cpr']:.2f} | R${r['cpm']:.2f} | {r['st']} |\n" for r in rows)
    foot = f"| **TOTAL** | **R${ts:.2f}** | **{tc}** | **R${cpr:.2f}** | — | {status(cpr)} |\n"
    return h + body + foot

report = f"""# Relatorio Meta Ads — Shineray Maranhao (Leao XIII)
**Data:** {now.strftime("%d/%m/%Y %H:%M")} (BRT) | **Conta:** 1057721942577752 | Plus Digital

---

## Hoje ({now.strftime("%d/%m/%Y")}) — Parcial

{tbl_today(rt, tst, tct, cprt)}

---

## Ultimos 7 Dias

{tbl_7d(r7, ts7, tc7, cpr7)}

---

## Diagnostico — Filosofia Andromeda

| CPR | Status |
|---|---|
| Abaixo de R$3,00 | 🟢 Ideal |
| R$3,00 – R$6,00 | 🟡 Atencao |
| Acima de R$6,00 | 🔴 Critico |

**CPR Geral 7 dias: R${cpr7:.2f}** — {status(cpr7)}

---
*Gerado automaticamente via Graph API Meta | Plus Digital*
"""

path = f"reports/shineray/meta-report-{today}.md"
os.makedirs("reports/shineray", exist_ok=True)
with open(path, "w", encoding="utf-8") as f:
    f.write(report)

print(f"Relatorio salvo: {path}")
print(f"7d: R${ts7:.2f} | {tc7} conversas | CPR R${cpr7:.2f}")
