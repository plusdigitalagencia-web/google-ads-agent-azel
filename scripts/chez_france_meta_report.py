import os, json, urllib.request, calendar
from datetime import datetime

TOKEN   = os.environ["CHEZ_FRANCE_META_ACCESS_TOKEN"]
ACCOUNT = "act_1929564697284378"
BASE    = "https://graph.facebook.com/v25.0"

MESES_PT = {1:"janeiro",2:"fevereiro",3:"março",4:"abril",5:"maio",6:"junho",
            7:"julho",8:"agosto",9:"setembro",10:"outubro",11:"novembro",12:"dezembro"}

def fetch_insights(since, until, level, extra_fields=""):
    fields = f"campaign_name,spend,clicks,impressions,cpm,ctr,frequency,reach,actions,action_values{extra_fields}"
    tr = f'{{"since":"{since}","until":"{until}"}}'
    url = (f"{BASE}/{ACCOUNT}/insights?fields={fields}&level={level}"
           f"&time_range={tr}&action_breakdowns=action_type&access_token={TOKEN}")
    try:
        res = urllib.request.urlopen(url)
        return json.loads(res.read())
    except urllib.error.HTTPError as e:
        print(f"  Insights error {e.code}: {e.read().decode()[:150]}")
        return {"data": []}

def val_purchase(actions):
    for x in (actions or []):
        if x.get("action_type") == "offsite_conversion.fb_pixel_purchase":
            return float(x["value"])
    return 0.0

def val_revenue(action_values):
    for x in (action_values or []):
        if x.get("action_type") == "offsite_conversion.fb_pixel_purchase":
            return float(x["value"])
    return 0.0

today       = datetime.now()
year, month = today.year, today.month
since       = f"{year}-{month:02d}-01"
until       = os.environ.get("UNTIL_DATE") or today.strftime("%Y-%m-%d")
until_dt    = datetime.strptime(until, "%Y-%m-%d")
mes_folder  = MESES_PT[until_dt.month]

if month == 1:
    prev_year, prev_month = year - 1, 12
else:
    prev_year, prev_month = year, month - 1
last_day_prev = calendar.monthrange(prev_year, prev_month)[1]
since_prev = f"{prev_year}-{prev_month:02d}-01"
until_prev = f"{prev_year}-{prev_month:02d}-{last_day_prev:02d}"
report_date = today.strftime("%Y-%m-%d")

data      = fetch_insights(since, until, "campaign")
data_prev = fetch_insights(since_prev, until_prev, "campaign")
data_ads  = fetch_insights(since, until, "ad",
                           ",ad_name,quality_ranking,engagement_rate_ranking,conversion_rate_ranking")
prev_by_name = {c.get("campaign_name"): c for c in data_prev.get("data", [])}

RANKING = {
    "ABOVE_AVERAGE": "🟢 Acima", "AVERAGE": "🟡 Médio",
    "BELOW_AVERAGE_10": "🔴 Baixo (10%)", "BELOW_AVERAGE_20": "🔴 Baixo (20%)",
    "BELOW_AVERAGE_35": "🔴 Baixo (35%)", "UNKNOWN": "⚪ —",
}

total_spend = 0.0; total_purchases = 0; total_revenue = 0.0
camp_meta = []

for camp in data.get("data", []):
    name      = camp.get("campaign_name", "—")
    spend     = float(camp.get("spend", 0))
    clicks    = int(camp.get("clicks", 0))
    impr      = int(camp.get("impressions", 0))
    cpm       = float(camp.get("cpm", 0))
    ctr       = float(camp.get("ctr", 0))
    freq      = float(camp.get("frequency", 0))
    reach     = int(camp.get("reach", 0))
    purchases = val_purchase(camp.get("actions", []))
    revenue   = val_revenue(camp.get("action_values", []))
    roas      = revenue / spend if spend > 0 else 0.0
    cpp       = spend / purchases if purchases > 0 else 0.0
    prev      = prev_by_name.get(name, {})
    prev_p    = val_purchase(prev.get("actions", []))
    prev_rev  = val_revenue(prev.get("action_values", []))
    prev_roas = prev_rev / float(prev.get("spend", 1)) if float(prev.get("spend", 0)) > 0 else 0.0
    total_spend += spend; total_purchases += int(purchases); total_revenue += revenue
    camp_meta.append({
        "name": name, "spend": spend, "clicks": clicks, "impr": impr,
        "cpm": cpm, "ctr": ctr, "freq": freq, "reach": reach,
        "purchases": int(purchases), "revenue": revenue, "roas": roas, "cpp": cpp,
        "prev_cpm": float(prev.get("cpm", 0)), "prev_ctr": float(prev.get("ctr", 0)),
        "prev_purchases": int(prev_p), "prev_spend": float(prev.get("spend", 0)),
        "prev_roas": prev_roas,
    })

roas_total     = total_revenue / total_spend if total_spend > 0 else 0.0
cpp_total      = total_spend / total_purchases if total_purchases > 0 else 0.0
prev_tot_purch = sum(c["prev_purchases"] for c in camp_meta)
prev_tot_spend = sum(c["prev_spend"] for c in camp_meta)
prev_tot_rev   = sum(c["prev_roas"] * c["prev_spend"] for c in camp_meta)
prev_roas_tot  = prev_tot_rev / prev_tot_spend if prev_tot_spend > 0 else 0.0

# ── Diagnóstico automático ────────────────────────────────────────────────────
deu_certo = []; nao_deu = []; melhorias = []

if camp_meta:
    best = max(camp_meta, key=lambda c: c["roas"])
    if best["roas"] > 0:
        deu_certo.append(f"**{best['name'][:50]}** entregou o melhor ROAS: {best['roas']:.2f}x.")

for c in camp_meta:
    if c["prev_ctr"] > 0 and c["ctr"] > c["prev_ctr"]:
        d = (c["ctr"] - c["prev_ctr"]) / c["prev_ctr"] * 100
        if d > 5:
            deu_certo.append(f"CTR de **{c['name'][:40]}** subiu {d:.0f}% — criativo funcionando.")

if prev_tot_purch > 0:
    delta = total_purchases - prev_tot_purch
    if delta >= 0:
        deu_certo.append(f"Compras mantidas ou crescendo: {prev_tot_purch} → {total_purchases} ({delta:+d}).")
    else:
        nao_deu.append(f"Compras caíram {abs(delta)}: {prev_tot_purch} → {total_purchases}.")

if prev_roas_tot > 0 and roas_total < prev_roas_tot:
    d = (roas_total - prev_roas_tot) / prev_roas_tot * 100
    if d < -5:
        nao_deu.append(f"ROAS médio caiu {abs(d):.0f}%: {prev_roas_tot:.2f}x → {roas_total:.2f}x.")

for c in camp_meta:
    if c["prev_ctr"] > 0 and (c["ctr"] - c["prev_ctr"]) / c["prev_ctr"] < -0.10:
        nao_deu.append(f"CTR de **{c['name'][:40]}** caiu — sinal de fadiga criativa.")
    if c["prev_cpm"] > 0 and (c["cpm"] - c["prev_cpm"]) / c["prev_cpm"] > 0.15:
        nao_deu.append(f"CPM de **{c['name'][:40]}** subiu — leilão mais caro.")

if camp_meta and best["roas"] >= 3:
    melhorias.append(f"**Escalar {best['name'][:40]}:** ROAS {best['roas']:.2f}x justifica aumento de budget.")
melhorias.append("**Testar criativos para Le Club:** assinatura recorrente tem LTV alto — vale budget específico.")
melhorias.append("**Criar público LookAlike** a partir dos compradores para reduzir CPP.")

# ── Relatório ─────────────────────────────────────────────────────────────────
roas_icon = lambda r: "🟢" if r >= 3 else ("🟡" if r >= 1 else "🔴")

lines = [
    "# Relatório Meta Ads — Chez France",
    f"**Período:** {since} a {until}  |  Plus Digital",
    "**Foco:** Vendas e-commerce (Compras) + Le Club (assinatura)",
    "",
    "---",
    "",
    "## 🧭 Resumo Executivo",
    "",
    "### ✅ O que deu certo", "",
]
for item in deu_certo:
    lines.append(f"- {item}")
lines += ["", "### ❌ O que não deu certo", ""]
for item in nao_deu:
    lines.append(f"- {item}")
lines += ["", "### 🚀 O que podemos fazer para melhorar", ""]
for i, item in enumerate(melhorias, 1):
    lines.append(f"{i}. {item}")

lines += ["", "---", "", "## 📋 Campanhas Ativas", ""]

for c in camp_meta:
    ri = roas_icon(c["roas"])
    lines += [
        f"### {ri} {c['name']}",
        "| Métrica | Valor |", "|---|---|",
        f"| ROAS | {ri} {c['roas']:.2f}x |",
        f"| Receita | R${c['revenue']:.2f} |",
        f"| Gasto | R${c['spend']:.2f} |",
        f"| Compras | {c['purchases']} |",
        f"| Custo por Compra | R${c['cpp']:.2f} |",
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
    f"**Total investido:** R${total_spend:.2f}  |  **Receita:** R${total_revenue:.2f}  |  **ROAS:** {roas_icon(roas_total)} {roas_total:.2f}x  |  **Compras:** {total_purchases}  |  **CPP:** R${cpp_total:.2f}",
    "",
    "---",
    "## 📊 Comparativo com Mês Anterior",
    "",
    f"| Métrica | {prev_month:02d}/{prev_year} | {month:02d}/{year} | Variação |",
    "|---|---|---|---|",
    f"| Gasto total | R${prev_tot_spend:.2f} | R${total_spend:.2f} | {(total_spend-prev_tot_spend)/prev_tot_spend*100:+.1f}% |" if prev_tot_spend > 0 else f"| Gasto total | — | R${total_spend:.2f} | — |",
    f"| Receita | R${prev_tot_rev:.2f} | R${total_revenue:.2f} | {'🟢' if total_revenue >= prev_tot_rev else '🔴'} {(total_revenue-prev_tot_rev)/prev_tot_rev*100:+.1f}% |" if prev_tot_rev > 0 else f"| Receita | — | R${total_revenue:.2f} | — |",
    f"| ROAS | {prev_roas_tot:.2f}x | {roas_total:.2f}x | {'🟢' if roas_total >= prev_roas_tot else '🔴'} |" if prev_roas_tot > 0 else f"| ROAS | — | {roas_total:.2f}x | — |",
    f"| Compras | {prev_tot_purch} | {total_purchases} | **{total_purchases-prev_tot_purch:+d}** |",
    "",
    "### Por campanha",
    "",
    f"| Campanha | Compras {prev_month:02d}/{prev_year} | Compras {month:02d}/{year} | Δ | ROAS anterior | ROAS atual |",
    "|---|---|---|---|---|---|",
]
for c in camp_meta:
    dp = c["purchases"] - c["prev_purchases"]
    lines.append(f"| {c['name'][:40]} | {c['prev_purchases']} | {c['purchases']} | **{dp:+d}** | {c['prev_roas']:.2f}x | {c['roas']:.2f}x |")

# Audit
lines += ["", "---", "## 🔍 Audit de Criativos", ""]
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
lines += [f"**Score de Saúde:** {h_e} {health}/100", "",
    "| Campanha | CTR ant. | CTR atual | Δ CTR | CPM ant. | CPM atual | Δ CPM | Frequência |",
    "|---|---|---|---|---|---|---|---|"]
for c in camp_meta:
    ctv = f"{(c['ctr']-c['prev_ctr'])/c['prev_ctr']*100:+.1f}%" if c["prev_ctr"] > 0 else "—"
    cpv = f"{(c['cpm']-c['prev_cpm'])/c['prev_cpm']*100:+.1f}%" if c["prev_cpm"] > 0 else "—"
    fs  = "🔴 Crítico" if c["freq"] > 4 else ("🟡 Atenção" if c["freq"] > 3 else "🟢 OK")
    lines.append(f"| {c['name'][:35]} | {c['prev_ctr']:.2f}% | {c['ctr']:.2f}% | {ctv} | R${c['prev_cpm']:.2f} | R${c['cpm']:.2f} | {cpv} | {fs} |")

lines.append("")
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
    f"**Total investido:** R${total_spend:.2f}  |  **Receita:** R${total_revenue:.2f}  |  **ROAS:** {roas_total:.2f}x  |  **Compras:** {total_purchases}",
    f"*Gerado automaticamente | Plus Digital | {today.strftime('%d/%m/%Y')}*",
]

os.makedirs(f"reports/ASSUCAR/chez-france/meta/{mes_folder}", exist_ok=True)
path = f"reports/ASSUCAR/chez-france/meta/{mes_folder}/meta-report-{report_date}.md"
with open(path, "w") as f:
    f.write("\n".join(lines))
print(f"Relatório salvo: {path}")
