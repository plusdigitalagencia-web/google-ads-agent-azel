import os, json, urllib.request
from datetime import datetime, timedelta

TOKEN   = os.environ["DELIKATA_META_ACCESS_TOKEN"]
ACCOUNT = "act_532861400590268"
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
    fields = f"campaign_name,spend,clicks,impressions,cpm,ctr,frequency,reach,actions,action_values,purchase_roas{extra_fields}"
    tr = f'{{"since":"{since}","until":"{until}"}}'
    url = (f"{BASE}/{ACCOUNT}/insights?fields={fields}&level={level}"
           f"&time_range={tr}&action_breakdowns=action_type&access_token={TOKEN}")
    try:
        res = urllib.request.urlopen(url)
        return json.loads(res.read())
    except urllib.error.HTTPError as e:
        print(f"  Insights error {e.code} level={level}: {e.read().decode()[:150]}")
        return {"data": []}

def val(lst, key):
    for x in (lst or []):
        if x.get("action_type") == key:
            return float(x["value"])
    return 0.0

# ── Períodos ──────────────────────────────────────────────────────────────────
today      = datetime.now()
until      = (today - timedelta(days=1)).strftime("%Y-%m-%d")
since      = (today - timedelta(days=7)).strftime("%Y-%m-%d")
until_prev = (today - timedelta(days=8)).strftime("%Y-%m-%d")
since_prev = (today - timedelta(days=14)).strftime("%Y-%m-%d")
report_date = today.strftime("%Y-%m-%d")

# ── Fetch de dados ────────────────────────────────────────────────────────────
data         = fetch_insights(since, until, "campaign")
data_prev    = fetch_insights(since_prev, until_prev, "campaign")
data_ads     = fetch_insights(since, until, "ad",
                              ",ad_name,adset_name,quality_ranking,engagement_rate_ranking,conversion_rate_ranking")
data_adsets  = fetch_insights(since, until, "adset", ",adset_name,reach")
adsets_mgmt  = api_get(f"/{ACCOUNT}/adsets",
                       "&fields=name,targeting,status,effective_status")

prev_by_name = {c.get("campaign_name"): c for c in data_prev.get("data", [])}

RANKING = {
    "ABOVE_AVERAGE":     "🟢 Acima",
    "AVERAGE":           "🟡 Médio",
    "BELOW_AVERAGE_10":  "🔴 Baixo (10%)",
    "BELOW_AVERAGE_20":  "🔴 Baixo (20%)",
    "BELOW_AVERAGE_35":  "🔴 Baixo (35%)",
    "UNKNOWN":           "⚪ —",
}

# ── Cabeçalho ─────────────────────────────────────────────────────────────────
lines = [
    "# Relatório Meta Ads — Delikata",
    f"**Período:** {since} a {until} | Plus Digital",
    "**Foco:** Compras (ROAS) | Pixel: Compra",
    "",
]

total_spend     = 0.0
total_purchases = 0
total_revenue   = 0.0
camp_meta       = []   # guarda dados para as seções de audit

# ── Seção 1: Campanhas ────────────────────────────────────────────────────────
for camp in data.get("data", []):
    name          = camp.get("campaign_name", "—")
    spend         = float(camp.get("spend", 0))
    clicks        = int(camp.get("clicks", 0))
    impr          = int(camp.get("impressions", 0))
    cpm           = float(camp.get("cpm", 0))
    ctr           = float(camp.get("ctr", 0))
    freq          = float(camp.get("frequency", 0))
    actions       = camp.get("actions", [])
    action_values = camp.get("action_values", [])
    purchases     = val(actions, "offsite_conversion.fb_pixel_purchase")
    revenue       = val(action_values, "offsite_conversion.fb_pixel_purchase")

    roas_raw = camp.get("purchase_roas", [])
    if roas_raw and isinstance(roas_raw, list):
        roas = float(roas_raw[0].get("value", 0))
    elif revenue > 0 and spend > 0:
        roas = revenue / spend
    else:
        roas = 0.0

    cpa    = spend / purchases if purchases > 0 else 0.0
    status = "🟢" if roas >= 3.0 else ("🟡" if roas >= 1.0 else "🔴")

    total_spend     += spend
    total_purchases += int(purchases)
    total_revenue   += revenue

    prev = prev_by_name.get(name, {})
    camp_meta.append({
        "name": name, "spend": spend, "cpm": cpm, "ctr": ctr,
        "freq": freq, "roas": roas, "purchases": int(purchases),
        "prev_cpm": float(prev.get("cpm", 0)),
        "prev_ctr": float(prev.get("ctr", 0)),
    })

    lines += [
        f"## 🟢 {name}",
        "| Métrica | Valor |",
        "|---|---|",
        f"| Status | {status} ROAS {roas:.2f}x |",
        f"| Gasto | R${spend:.2f} |",
        f"| Receita | R${revenue:.2f} |",
        f"| Compras | {int(purchases)} |",
        f"| CPA | R${cpa:.2f} |",
        f"| Impressões | {impr:,} |",
        f"| Cliques | {clicks:,} |",
        f"| CTR | {ctr:.2f}% |",
        f"| CPM | R${cpm:.2f} |",
        f"| Frequência | {freq:.1f} |",
        "",
    ]

total_roas = total_revenue / total_spend if total_spend > 0 else 0.0
lines += [
    "---",
    f"**Total investido:** R${total_spend:.2f} | **Total receita:** R${total_revenue:.2f} | "
    f"**ROAS geral:** {total_roas:.2f}x | **Compras:** {total_purchases}",
    "",
]

# ── Seção 2: Audit de Criativos ───────────────────────────────────────────────
lines += ["---", "## 🔍 Audit de Criativos — Meta Ads", ""]

health_score  = 100
health_alerts = []

for c in camp_meta:
    name      = c["name"]
    name_s    = name[:35]
    freq      = c["freq"]
    cpm       = c["cpm"]
    ctr       = c["ctr"]
    prev_cpm  = c["prev_cpm"]
    prev_ctr  = c["prev_ctr"]

    if freq > 4:
        health_score -= 10
        health_alerts.append(f"🔴 **{name_s}** — Frequência {freq:.1f} (> 4 = fadiga crítica — trocar criativo)")
    elif freq > 3:
        health_score -= 5
        health_alerts.append(f"🟡 **{name_s}** — Frequência {freq:.1f} (3–4 = atenção — preparar novo criativo)")

    if prev_cpm > 0:
        delta = (cpm - prev_cpm) / prev_cpm
        if delta > 0.30:
            health_score -= 10
            health_alerts.append(f"🔴 **{name_s}** — CPM subiu {delta*100:.0f}% vs período anterior")
        elif delta > 0.15:
            health_score -= 5
            health_alerts.append(f"🟡 **{name_s}** — CPM subiu {delta*100:.0f}% vs período anterior")

    if prev_ctr > 0:
        delta = (ctr - prev_ctr) / prev_ctr
        if delta < -0.20:
            health_score -= 10
            health_alerts.append(f"🔴 **{name_s}** — CTR caiu {abs(delta)*100:.0f}% vs período anterior")
        elif delta < -0.15:
            health_score -= 5
            health_alerts.append(f"🟡 **{name_s}** — CTR caiu {abs(delta)*100:.0f}% vs período anterior")

    if c["roas"] < 1.0 and c["spend"] > 50:
        health_score -= 10
        health_alerts.append(f"🔴 **{name_s}** — ROAS abaixo de 1x com gasto relevante")

health_score = max(0, health_score)
h_emoji = "🟢" if health_score >= 80 else ("🟡" if health_score >= 60 else "🔴")

lines += [
    f"**Score de Saúde da Conta:** {h_emoji} {health_score}/100",
    f"**Comparativo:** {since} a {until}  vs  {since_prev} a {until_prev}",
    "",
    "### Fadiga Criativa por Campanha",
    "",
    "| Campanha | Freq | CTR atual | CTR anterior | Δ CTR | CPM atual | Δ CPM | Status |",
    "|---|---|---|---|---|---|---|---|",
]

for c in camp_meta:
    freq     = c["freq"]
    ctr      = c["ctr"]
    prev_ctr = c["prev_ctr"]
    cpm      = c["cpm"]
    prev_cpm = c["prev_cpm"]

    ctr_var = f"{((ctr-prev_ctr)/prev_ctr*100):+.0f}%" if prev_ctr > 0 else "—"
    cpm_var = f"{((cpm-prev_cpm)/prev_cpm*100):+.0f}%" if prev_cpm > 0 else "—"
    f_status = "🔴 Crítico" if freq > 4 else ("🟡 Atenção" if freq > 3 else "🟢 OK")

    lines.append(
        f"| {c['name'][:35]} | {freq:.1f} | {ctr:.2f}% | {prev_ctr:.2f}% | "
        f"{ctr_var} | R${cpm:.2f} | {cpm_var} | {f_status} |"
    )

lines.append("")

if health_alerts:
    lines += ["### ⚠️ Alertas", ""]
    for alert in health_alerts:
        lines.append(f"- {alert}")
    lines.append("")

# Rankings de qualidade por anúncio
ads_data = data_ads.get("data", [])
if ads_data:
    lines += [
        "### Rankings de Qualidade dos Anúncios",
        "",
        "| Anúncio | Qualidade | Engajamento | Conversão | Gasto |",
        "|---|---|---|---|---|",
    ]
    for ad in ads_data:
        ad_name = ad.get("ad_name", "—")[:40]
        spend   = float(ad.get("spend", 0))
        qual    = RANKING.get(ad.get("quality_ranking", "UNKNOWN"), "⚪ —")
        eng     = RANKING.get(ad.get("engagement_rate_ranking", "UNKNOWN"), "⚪ —")
        conv    = RANKING.get(ad.get("conversion_rate_ranking", "UNKNOWN"), "⚪ —")
        lines.append(f"| {ad_name} | {qual} | {eng} | {conv} | R${spend:.2f} |")
    lines.append("")

# ── Seção 3: Sobreposição de Públicos ─────────────────────────────────────────
lines += ["---", "## 👥 Análise de Sobreposição de Públicos", ""]

adsets_list    = adsets_mgmt.get("data", [])
active_adsets  = [a for a in adsets_list if a.get("effective_status") in ("ACTIVE", "PAUSED")]
adsets_insight = {a.get("adset_name"): a for a in data_adsets.get("data", [])}

if data_adsets.get("data"):
    lines += [
        "### CPM por Conjunto de Anúncios",
        "",
        "*CPMs similares entre conjuntos com mesmo público = sinal de competição interna*",
        "",
        "| Conjunto | Campanha | CPM | Frequência | Alcance |",
        "|---|---|---|---|---|",
    ]
    adset_cpms = []
    for adset in data_adsets.get("data", []):
        aname = adset.get("adset_name", "—")[:35]
        cname = adset.get("campaign_name", "—")[:25]
        cpm   = float(adset.get("cpm", 0))
        freq  = float(adset.get("frequency", 0))
        reach = int(adset.get("reach", 0))
        adset_cpms.append(cpm)
        lines.append(f"| {aname} | {cname} | R${cpm:.2f} | {freq:.1f} | {reach:,} |")
    lines.append("")

    if len(adset_cpms) > 1:
        avg_cpm    = sum(adset_cpms) / len(adset_cpms)
        cpm_spread = (max(adset_cpms) - min(adset_cpms)) / avg_cpm * 100 if avg_cpm > 0 else 0
        if cpm_spread > 40:
            lines.append(f"🔴 Variação de CPM entre conjuntos: {cpm_spread:.0f}% — possível competição interna.")
        elif cpm_spread > 20:
            lines.append(f"🟡 Variação de CPM: {cpm_spread:.0f}% — monitorar.")
        else:
            lines.append(f"🟢 CPMs equilibrados entre conjuntos ({cpm_spread:.0f}% de variação) — sem sinal de competição interna.")
        lines.append("")

if active_adsets:
    lines += ["### Targeting por Conjunto de Anúncios", ""]

    overlap_data = []
    for adset in active_adsets:
        aname     = adset.get("name", "—")
        targeting = adset.get("targeting", {})
        geo       = targeting.get("geo_locations", {})
        cities    = [c.get("name", "") for c in geo.get("cities", [])]
        countries = geo.get("countries", [])
        age_min   = targeting.get("age_min", "—")
        age_max   = targeting.get("age_max", "—")
        interests = []
        for spec in targeting.get("flexible_spec", []):
            for i in spec.get("interests", []):
                interests.append(i.get("name", ""))
        custom_aud = [a.get("name", a.get("id", "")) for a in targeting.get("custom_audiences", [])]
        status_str = adset.get("effective_status", "")

        geo_str = ", ".join(cities) if cities else (", ".join(countries) if countries else "—")
        age_str = f"{age_min}–{age_max}" if age_min != "—" else "—"
        int_str = (", ".join(interests[:3]) + ("…" if len(interests) > 3 else "")) if interests else "—"
        aud_str = ", ".join(custom_aud[:2]) if custom_aud else "Interesse/Broad"

        lines += [
            f"**{aname}** ({status_str})",
            f"- Geo: {geo_str} | Idade: {age_str}",
            f"- Interesses: {int_str}",
            f"- Públicos: {aud_str}",
            "",
        ]
        overlap_data.append({
            "name": aname, "geo": geo_str, "age": age_str,
            "interests": set(interests), "custom": set(custom_aud),
        })

    lines += ["### Diagnóstico de Sobreposição", ""]
    found = False
    for i in range(len(overlap_data)):
        for j in range(i + 1, len(overlap_data)):
            a, b = overlap_data[i], overlap_data[j]
            shared_int    = a["interests"] & b["interests"]
            shared_custom = a["custom"] & b["custom"]
            same_geo      = a["geo"] == b["geo"] and a["geo"] != "—"
            if shared_int or shared_custom or same_geo:
                found = True
                lines.append(f"⚠️ **{a['name'][:30]}** ↔ **{b['name'][:30]}**")
                if same_geo:
                    lines.append(f"  - Mesma localização: {a['geo']}")
                if shared_int:
                    lines.append(f"  - Interesses compartilhados: {', '.join(list(shared_int)[:3])}")
                if shared_custom:
                    lines.append(f"  - Públicos custom compartilhados: {', '.join(list(shared_custom)[:2])}")
                lines.append("  - **Ação:** Adicionar exclusão de audiência ou consolidar em CBO")
                lines.append("")
    if not found:
        lines += ["🟢 Nenhuma sobreposição detectada nos parâmetros de targeting.", ""]

lines += [
    "### ✅ Checklist Manual (verificar no Gerenciador)",
    "",
    "- [ ] Ferramenta de Sobreposição de Público no Ads Manager (percentual exato)",
    "- [ ] Públicos de remarketing excluem prospecting",
    "- [ ] Event Match Quality ≥ 6 no Events Manager",
    "- [ ] Pixel instalado corretamente (Pixel Helper Chrome)",
    "",
]

# ── Rodapé ───────────────────────────────────────────────────────────────────
lines += [
    "---",
    f"**Total investido:** R${total_spend:.2f} | **Total receita:** R${total_revenue:.2f} | "
    f"**ROAS geral:** {total_roas:.2f}x | **Compras:** {total_purchases}",
    f"*Gerado automaticamente | Plus Digital | {today.strftime('%d/%m/%Y')}*",
]

os.makedirs("reports/delikata", exist_ok=True)
path = f"reports/delikata/meta-report-{report_date}.md"
with open(path, "w") as f:
    f.write("\n".join(lines))
print(f"Relatório salvo: {path}")
