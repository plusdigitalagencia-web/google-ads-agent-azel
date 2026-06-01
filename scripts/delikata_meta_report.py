import os, json, urllib.request
from datetime import datetime, timedelta

TOKEN      = os.environ["DELIKATA_META_ACCESS_TOKEN"]
APP_ID     = os.environ["DELIKATA_META_APP_ID"]
APP_SECRET = os.environ["DELIKATA_META_APP_SECRET"]
ACCOUNT    = "act_532861400590268"
BASE       = "https://graph.facebook.com/v25.0"

def refresh_token(token):
    url = (f"{BASE}/oauth/access_token?grant_type=fb_exchange_token"
           f"&client_id={APP_ID}&client_secret={APP_SECRET}&fb_exchange_token={token}")
    try:
        res = urllib.request.urlopen(url)
        return json.loads(res.read()).get("access_token", token)
    except Exception as e:
        print(f"  Token refresh falhou ({e}), usando token original")
        return token

TOKEN = refresh_token(TOKEN)

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

today      = datetime.now()
until      = (today - timedelta(days=1)).strftime("%Y-%m-%d")
since      = (today - timedelta(days=7)).strftime("%Y-%m-%d")
until_prev = (today - timedelta(days=8)).strftime("%Y-%m-%d")
since_prev = (today - timedelta(days=14)).strftime("%Y-%m-%d")
report_date = today.strftime("%Y-%m-%d")

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

# ── Coleta de métricas ────────────────────────────────────────────────────────
total_spend     = 0.0
total_purchases = 0
total_revenue   = 0.0
camp_meta       = []

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
    roas_raw      = camp.get("purchase_roas", [])
    roas          = float(roas_raw[0].get("value", 0)) if roas_raw else (revenue / spend if spend > 0 else 0.0)
    cpa           = spend / purchases if purchases > 0 else 0.0

    total_spend     += spend
    total_purchases += int(purchases)
    total_revenue   += revenue

    prev = prev_by_name.get(name, {})
    prev_purchases = val(prev.get("actions", []), "offsite_conversion.fb_pixel_purchase")
    prev_revenue   = val(prev.get("action_values", []) if prev.get("action_values") else [], "offsite_conversion.fb_pixel_purchase")
    camp_meta.append({
        "name": name, "spend": spend, "clicks": clicks, "impr": impr,
        "cpm": cpm, "ctr": ctr, "freq": freq, "roas": roas,
        "purchases": int(purchases), "revenue": revenue, "cpa": cpa,
        "prev_cpm":      float(prev.get("cpm", 0)),
        "prev_ctr":      float(prev.get("ctr", 0)),
        "prev_purchases": int(prev_purchases),
        "prev_spend":    float(prev.get("spend", 0)),
        "prev_revenue":  prev_revenue,
    })

total_roas = total_revenue / total_spend if total_spend > 0 else 0.0
prev_total_spend    = sum(c["prev_spend"] for c in camp_meta)
prev_total_revenue  = sum(c["prev_revenue"] for c in camp_meta)
prev_total_purchases = sum(c["prev_purchases"] for c in camp_meta)
prev_total_roas     = prev_total_revenue / prev_total_spend if prev_total_spend > 0 else 0.0

# ── Diagnóstico automático para o resumo executivo ────────────────────────────
deu_certo = []
nao_deu   = []
melhorias = []

# Campanha com melhor ROAS
if camp_meta:
    best_roas = max(camp_meta, key=lambda c: c["roas"])
    if best_roas["roas"] >= 3.0:
        deu_certo.append(f"**{best_roas['name'][:50]}** com ROAS {best_roas['roas']:.2f}x — acima da meta de 3x.")
    elif best_roas["roas"] >= 1.0:
        deu_certo.append(f"**{best_roas['name'][:50]}** com ROAS {best_roas['roas']:.2f}x — positivo, mas ainda abaixo da meta de 3x.")

# ROAS geral vs anterior
if prev_total_roas > 0 and total_roas > prev_total_roas:
    deu_certo.append(f"ROAS geral melhorou: {prev_total_roas:.2f}x → {total_roas:.2f}x.")

# Volume de compras crescendo
if prev_total_purchases > 0 and total_purchases > prev_total_purchases:
    d = total_purchases - prev_total_purchases
    deu_certo.append(f"Volume de compras cresceu {d:+d} ({d/prev_total_purchases*100:.0f}%): {prev_total_purchases} → {total_purchases}.")

# CTR subindo
for c in camp_meta:
    if c["prev_ctr"] > 0 and c["ctr"] > c["prev_ctr"]:
        d = (c["ctr"] - c["prev_ctr"]) / c["prev_ctr"] * 100
        if d > 10:
            deu_certo.append(f"CTR de **{c['name'][:40]}** subiu {d:.0f}% — criativo com boa tração.")

# ROAS abaixo de 1x
for c in camp_meta:
    if c["spend"] > 50 and c["roas"] < 1.0:
        nao_deu.append(f"**{c['name'][:50]}** com ROAS {c['roas']:.2f}x — gasto sem retorno positivo (gasto R${c['spend']:.2f}).")

# ROAS geral caindo
if prev_total_roas > 0 and total_roas < prev_total_roas:
    d = (total_roas - prev_total_roas) / prev_total_roas * 100
    nao_deu.append(f"ROAS geral caiu {abs(d):.0f}%: {prev_total_roas:.2f}x → {total_roas:.2f}x.")

# Volume de compras caindo
if prev_total_purchases > 0 and total_purchases < prev_total_purchases:
    d = total_purchases - prev_total_purchases
    nao_deu.append(f"Volume de compras caiu {abs(d)} ({d/prev_total_purchases*100:.0f}%): {prev_total_purchases} → {total_purchases}.")

# CTR caindo
for c in camp_meta:
    if c["prev_ctr"] > 0:
        d = (c["ctr"] - c["prev_ctr"]) / c["prev_ctr"] * 100
        if d < -10:
            nao_deu.append(f"CTR de **{c['name'][:40]}** caiu {abs(d):.0f}% — sinal de fadiga criativa.")

# CPM subindo
for c in camp_meta:
    if c["prev_cpm"] > 0:
        d = (c["cpm"] - c["prev_cpm"]) / c["prev_cpm"] * 100
        if d > 15:
            nao_deu.append(f"CPM de **{c['name'][:40]}** subiu {d:.0f}% — leilão mais caro.")

# Melhorias
for c in camp_meta:
    if c["roas"] >= 3.0 and c["spend"] > 0:
        melhorias.append(f"**Escalar {c['name'][:40]}:** ROAS {c['roas']:.2f}x — aumentar budget para maximizar retorno.")
for c in camp_meta:
    if c["prev_ctr"] > 0 and (c["ctr"] - c["prev_ctr"]) / c["prev_ctr"] < -0.10:
        melhorias.append(f"**Renovar criativo de {c['name'][:40]}:** CTR em queda — testar novo ângulo de comunicação.")
for c in camp_meta:
    if c["spend"] > 50 and c["roas"] < 1.0:
        melhorias.append(f"**Revisar ou pausar {c['name'][:40]}:** ROAS abaixo de 1x — ajustar público, criativo ou landing page.")
melhorias.append("**Criar público LookAlike** dos compradores para melhorar qualidade e reduzir CPA.")
melhorias.append("**Testar novos formatos criativos** (vídeo curto, carrossel de produto) para reduzir fadiga.")

# ── Cabeçalho ─────────────────────────────────────────────────────────────────
lines = [
    "# Relatório Meta Ads — Delikata",
    f"**Período:** {since} a {until} | Plus Digital",
    "**Foco:** Compras (ROAS) | Pixel: Compra",
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
if not deu_certo:
    lines.append("- Nenhum destaque positivo identificado no período — verificar ajustes de campanha.")

lines += ["", "### ❌ O que não deu certo", ""]
for item in nao_deu:
    lines.append(f"- {item}")
if not nao_deu:
    lines.append("- Nenhum alerta identificado — conta saudável no período.")

lines += ["", "### 🚀 O que podemos fazer para melhorar", ""]
for i, item in enumerate(melhorias, 1):
    lines.append(f"{i}. {item}")

lines += ["", "---", "", "## 📋 Campanhas Ativas", ""]

# ── Seção de Campanhas ────────────────────────────────────────────────────────
for c in camp_meta:
    roas_s = "🟢" if c["roas"] >= 3.0 else ("🟡" if c["roas"] >= 1.0 else "🔴")
    lines += [
        f"## 🟢 {c['name']}",
        "| Métrica | Valor |", "|---|---|",
        f"| Status | {roas_s} ROAS {c['roas']:.2f}x |",
        f"| Gasto | R${c['spend']:.2f} |",
        f"| Receita | R${c['revenue']:.2f} |",
        f"| Compras | {c['purchases']} |",
        f"| CPA | R${c['cpa']:.2f} |",
        f"| Impressões | {c['impr']:,} |",
        f"| Cliques | {c['clicks']:,} |",
        f"| CTR | {c['ctr']:.2f}% |",
        f"| CPM | R${c['cpm']:.2f} |",
        f"| Frequência | {c['freq']:.1f} |",
        "",
    ]

lines += [
    "---",
    f"**Total investido:** R${total_spend:.2f} | **Total receita:** R${total_revenue:.2f} | "
    f"**ROAS geral:** {total_roas:.2f}x | **Compras:** {total_purchases}",
    "",
    "---",
    "## 📊 Comparativo com Semana Anterior",
    "",
    f"| Métrica | Semana anterior | Semana atual | Variação |",
    "|---|---|---|---|",
    f"| Gasto | R${prev_total_spend:.2f} | R${total_spend:.2f} | {(total_spend-prev_total_spend)/prev_total_spend*100:+.1f}% |" if prev_total_spend > 0 else "| Gasto | — | R${total_spend:.2f} | — |",
    f"| Receita | R${prev_total_revenue:.2f} | R${total_revenue:.2f} | {(total_revenue-prev_total_revenue)/prev_total_revenue*100:+.1f}% {'🟢' if total_revenue >= prev_total_revenue else '🔴'} |" if prev_total_revenue > 0 else "| Receita | — | R${total_revenue:.2f} | — |",
    f"| Compras | {prev_total_purchases} | {total_purchases} | {total_purchases-prev_total_purchases:+d} {'🟢' if total_purchases >= prev_total_purchases else '🔴'} |",
    f"| ROAS | {prev_total_roas:.2f}x | {total_roas:.2f}x | {(total_roas-prev_total_roas)/prev_total_roas*100:+.1f}% {'🟢' if total_roas >= prev_total_roas else '🔴'} |" if prev_total_roas > 0 else "| ROAS | — | {total_roas:.2f}x | — |",
    "",
    "### Por campanha",
    "",
    "| Campanha | Compras ant. | Compras | Δ | ROAS ant. | ROAS | Δ ROAS |",
    "|---|---|---|---|---|---|---|",
]
for c in camp_meta:
    prev_roas = c["prev_revenue"] / c["prev_spend"] if c["prev_spend"] > 0 else 0.0
    dc = c["purchases"] - c["prev_purchases"]
    dr = f"{(c['roas']-prev_roas)/prev_roas*100:+.1f}%" if prev_roas > 0 else "—"
    lines.append(f"| {c['name'][:40]} | {c['prev_purchases']} | {c['purchases']} | {dc:+d} | {prev_roas:.2f}x | {c['roas']:.2f}x | {dr} |")

# ── Audit de Criativos ────────────────────────────────────────────────────────
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
    if c["roas"] < 1.0 and c["spend"] > 50:
        health -= 10; alerts.append(f"🔴 **{c['name'][:40]}** — ROAS abaixo de 1x com gasto relevante")

health = max(0, health)
h_e = "🟢" if health >= 80 else ("🟡" if health >= 60 else "🔴")
lines += [
    f"**Score de Saúde da Conta:** {h_e} {health}/100",
    f"**Comparativo:** {since} a {until}  vs  {since_prev} a {until_prev}",
    "",
    "### Fadiga Criativa por Campanha",
    "",
    "| Campanha | Freq | CTR atual | CTR ant. | Δ CTR | CPM atual | Δ CPM | Status |",
    "|---|---|---|---|---|---|---|---|",
]
for c in camp_meta:
    ctv = f"{(c['ctr']-c['prev_ctr'])/c['prev_ctr']*100:+.0f}%" if c["prev_ctr"] > 0 else "—"
    cpv = f"{(c['cpm']-c['prev_cpm'])/c['prev_cpm']*100:+.0f}%" if c["prev_cpm"] > 0 else "—"
    fs  = "🔴 Crítico" if c["freq"] > 4 else ("🟡 Atenção" if c["freq"] > 3 else "🟢 OK")
    lines.append(f"| {c['name'][:35]} | {c['freq']:.1f} | {c['ctr']:.2f}% | {c['prev_ctr']:.2f}% | {ctv} | R${c['cpm']:.2f} | {cpv} | {fs} |")

lines.append("")
if alerts:
    lines += ["### ⚠️ Alertas", ""]
    for a in alerts: lines.append(f"- {a}")
    lines.append("")

ads_data = data_ads.get("data", [])
if ads_data:
    lines += [
        "### Rankings de Qualidade dos Anúncios", "",
        "| Anúncio | Qualidade | Engajamento | Conversão | Gasto |",
        "|---|---|---|---|---|",
    ]
    for ad in ads_data:
        lines.append(
            f"| {ad.get('ad_name','—')[:40]} | {RANKING.get(ad.get('quality_ranking','UNKNOWN'),'⚪')} | "
            f"{RANKING.get(ad.get('engagement_rate_ranking','UNKNOWN'),'⚪')} | "
            f"{RANKING.get(ad.get('conversion_rate_ranking','UNKNOWN'),'⚪')} | R${float(ad.get('spend',0)):.2f} |"
        )
    lines.append("")

# ── Sobreposição de Públicos ──────────────────────────────────────────────────
lines += ["---", "## 👥 Análise de Sobreposição de Públicos", ""]
adsets_list   = adsets_mgmt.get("data", [])
active_adsets = [a for a in adsets_list if a.get("effective_status") in ("ACTIVE", "PAUSED")]

if data_adsets.get("data"):
    lines += [
        "### CPM por Conjunto de Anúncios", "",
        "| Conjunto | Campanha | CPM | Frequência | Alcance |",
        "|---|---|---|---|---|",
    ]
    adset_cpms = []
    for adset in data_adsets.get("data", []):
        cpm  = float(adset.get("cpm", 0)); adset_cpms.append(cpm)
        freq = float(adset.get("frequency", 0))
        reach = int(adset.get("reach", 0))
        lines.append(f"| {adset.get('adset_name','—')[:35]} | {adset.get('campaign_name','—')[:25]} | R${cpm:.2f} | {freq:.1f} | {reach:,} |")
    lines.append("")
    if len(adset_cpms) > 1:
        avg = sum(adset_cpms) / len(adset_cpms)
        spread = (max(adset_cpms) - min(adset_cpms)) / avg * 100 if avg > 0 else 0
        if spread > 40:   lines.append(f"🔴 Variação de CPM entre conjuntos: {spread:.0f}% — possível competição interna.")
        elif spread > 20: lines.append(f"🟡 Variação de CPM: {spread:.0f}% — monitorar.")
        else:             lines.append(f"🟢 CPMs equilibrados ({spread:.0f}% de variação).")
        lines.append("")

if active_adsets:
    lines += ["### Targeting por Conjunto de Anúncios", ""]
    overlap_data = []
    for adset in active_adsets:
        targeting  = adset.get("targeting", {})
        geo        = targeting.get("geo_locations", {})
        cities     = [c.get("name", "") for c in geo.get("cities", [])]
        countries  = geo.get("countries", [])
        geo_str    = ", ".join(cities) if cities else (", ".join(countries) if countries else "—")
        age_min    = targeting.get("age_min", "—"); age_max = targeting.get("age_max", "—")
        interests  = [i.get("name","") for spec in targeting.get("flexible_spec",[]) for i in spec.get("interests",[])]
        custom_aud = [a.get("name", a.get("id","")) for a in targeting.get("custom_audiences",[])]
        int_str    = (", ".join(interests[:3]) + ("…" if len(interests)>3 else "")) if interests else "—"
        aud_str    = ", ".join(custom_aud[:2]) if custom_aud else "Interesse/Broad"
        lines += [
            f"**{adset.get('name','—')}** ({adset.get('effective_status','')})",
            f"- Geo: {geo_str} | Idade: {age_min}–{age_max}",
            f"- Interesses: {int_str} | Públicos: {aud_str}", "",
        ]
        overlap_data.append({"name": adset.get("name","—"), "geo": geo_str,
                              "interests": set(interests), "custom": set(custom_aud)})

    lines += ["### Diagnóstico de Sobreposição", ""]
    found = False
    for i in range(len(overlap_data)):
        for j in range(i+1, len(overlap_data)):
            a, b = overlap_data[i], overlap_data[j]
            si = a["interests"] & b["interests"]; sc = a["custom"] & b["custom"]
            sg = a["geo"] == b["geo"] and a["geo"] != "—"
            if si or sc or sg:
                found = True
                lines.append(f"⚠️ **{a['name'][:30]}** ↔ **{b['name'][:30]}**")
                if sg: lines.append(f"  - Mesma geo: {a['geo']}")
                if si: lines.append(f"  - Interesses: {', '.join(list(si)[:3])}")
                if sc: lines.append(f"  - Públicos: {', '.join(list(sc)[:2])}")
                lines.append("  - **Ação:** Adicionar exclusão ou consolidar em CBO"); lines.append("")
    if not found:
        lines += ["🟢 Nenhuma sobreposição detectada.", ""]

lines += [
    "### ✅ Checklist Manual", "",
    "- [ ] Ferramenta de Sobreposição de Público no Ads Manager",
    "- [ ] Públicos de remarketing excluem prospecting",
    "- [ ] Event Match Quality ≥ 6 no Events Manager",
    "- [ ] Pixel instalado corretamente (Pixel Helper Chrome)", "",
]

# ── Rodapé ────────────────────────────────────────────────────────────────────
lines += [
    "---",
    f"**Total investido:** R${total_spend:.2f} | **Receita:** R${total_revenue:.2f} | "
    f"**ROAS:** {total_roas:.2f}x | **Compras:** {total_purchases}",
    f"*Gerado automaticamente | Plus Digital | {today.strftime('%d/%m/%Y')}*",
]

os.makedirs("reports/delikata", exist_ok=True)
path = f"reports/delikata/meta-report-{report_date}.md"
with open(path, "w") as f:
    f.write("\n".join(lines))
print(f"Relatório salvo: {path}")
