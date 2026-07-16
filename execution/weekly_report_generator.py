"""
Generates a weekly Markdown report for a Google Ads account.
Usage: python3 weekly_report_generator.py --customer-id ID --mcc-id ID --output FILE.md [--client-name NAME] [--currency BRL|COP|EUR|USD]
"""
import os
import argparse
from datetime import date, timedelta
from dotenv import load_dotenv
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

load_dotenv("/etc/secrets/.env", override=True)
load_dotenv(override=True)


def get_client(mcc_id):
    return GoogleAdsClient.load_from_dict({
        "developer_token": os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN"),
        "client_id": os.getenv("GOOGLE_ADS_CLIENT_ID"),
        "client_secret": os.getenv("GOOGLE_ADS_CLIENT_SECRET"),
        "refresh_token": os.getenv("GOOGLE_ADS_REFRESH_TOKEN"),
        "login_customer_id": mcc_id,
        "use_proto_plus": True,
    })


def micros(value):
    return value / 1_000_000


def format_currency(value, currency="BRL"):
    if currency == "COP": return f"COP {value:,.0f}"
    if currency == "EUR": return f"\u20ac{value:,.2f}"
    if currency == "USD": return f"US$ {value:,.2f}"
    return f"R$ {value:,.2f}"


def safe_pct(value):
    """Format impression share safely — returns '—' for unavailable/NaN values."""
    try:
        v = float(value)
        if v <= 0 or v != v: return "\u2014"
        return f"{v * 100:.1f}%"
    except Exception:
        return "\u2014"


def pct_change(current, previous):
    if previous == 0: return None
    change = ((current - previous) / previous) * 100
    arrow = "\u2191" if change >= 0 else "\u2193"
    return f"{arrow} {change:+.1f}%"


def date_range(days_ago_start, days_ago_end):
    today = date.today()
    end = today - timedelta(days=days_ago_end)
    start = today - timedelta(days=days_ago_start)
    return start, end


# \u2500\u2500 Query functions \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500

def fetch_campaign_metrics(service, customer_id, start, end):
    query = f"""
        SELECT
            campaign.id,
            campaign.name,
            campaign.status,
            campaign.advertising_channel_type,
            campaign_budget.amount_micros,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.conversions_value,
            metrics.all_conversions,
            metrics.ctr,
            metrics.average_cpc,
            metrics.search_impression_share,
            metrics.search_rank_lost_impression_share,
            metrics.search_budget_lost_impression_share,
            metrics.search_top_impression_share,
            metrics.search_absolute_top_impression_share
        FROM campaign
        WHERE segments.date BETWEEN '{start}' AND '{end}'
        AND campaign.status != 'REMOVED'
        AND metrics.impressions > 0
        ORDER BY metrics.cost_micros DESC
    """
    return list(service.search(customer_id=customer_id, query=query))


def fetch_keywords(service, customer_id, start, end):
    query = f"""
        SELECT
            ad_group_criterion.keyword.text,
            ad_group_criterion.keyword.match_type,
            campaign.name,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.ctr,
            metrics.average_cpc
        FROM keyword_view
        WHERE segments.date BETWEEN '{start}' AND '{end}'
        AND metrics.impressions > 0
        ORDER BY metrics.cost_micros DESC
    """
    return list(service.search(customer_id=customer_id, query=query))


def fetch_keyword_quality_scores(service, customer_id):
    """Quality Score is a current-state metric — no date range needed."""
    query = """
        SELECT
            ad_group_criterion.keyword.text,
            ad_group_criterion.quality_info.quality_score,
            ad_group_criterion.quality_info.creative_quality_score,
            ad_group_criterion.quality_info.post_click_quality_score,
            ad_group_criterion.quality_info.search_predicted_ctr,
            campaign.name
        FROM keyword_view
        WHERE ad_group_criterion.status != 'REMOVED'
        AND campaign.status = 'ENABLED'
        AND ad_group.status = 'ENABLED'
    """
    try:
        return list(service.search(customer_id=customer_id, query=query))
    except Exception:
        return []


def fetch_device_breakdown(service, customer_id, start, end):
    query = f"""
        SELECT
            segments.device,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.impressions,
            metrics.ctr,
            metrics.average_cpc
        FROM campaign
        WHERE segments.date BETWEEN '{start}' AND '{end}'
        AND metrics.impressions > 0
    """
    try:
        return list(service.search(customer_id=customer_id, query=query))
    except Exception:
        return []


def fetch_ad_groups(service, customer_id, start, end):
    query = f"""
        SELECT
            ad_group.name,
            ad_group.status,
            campaign.name,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.ctr,
            metrics.average_cpc
        FROM ad_group
        WHERE segments.date BETWEEN '{start}' AND '{end}'
        AND metrics.impressions > 0
        AND ad_group.status != 'REMOVED'
        ORDER BY metrics.cost_micros DESC
    """
    try:
        return list(service.search(customer_id=customer_id, query=query))
    except Exception:
        return []


def fetch_ads(service, customer_id, start, end):
    query = f"""
        SELECT
            ad_group_ad.ad.id,
            ad_group_ad.ad.type,
            ad_group_ad.ad_strength,
            ad_group_ad.status,
            ad_group_ad.ad.responsive_search_ad.headlines,
            campaign.name,
            ad_group.name,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.ctr
        FROM ad_group_ad
        WHERE segments.date BETWEEN '{start}' AND '{end}'
        AND ad_group_ad.status = 'ENABLED'
        AND metrics.impressions > 0
        ORDER BY metrics.cost_micros DESC
        LIMIT 20
    """
    try:
        return list(service.search(customer_id=customer_id, query=query))
    except Exception:
        return []


def fetch_search_terms(service, customer_id, start, end):
    query = f"""
        SELECT
            search_term_view.search_term,
            search_term_view.status,
            campaign.name,
            ad_group.name,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.ctr
        FROM search_term_view
        WHERE segments.date BETWEEN '{start}' AND '{end}'
        AND metrics.impressions > 0
        ORDER BY metrics.cost_micros DESC
        LIMIT 50
    """
    return list(service.search(customer_id=customer_id, query=query))


# \u2500\u2500 Aggregation helpers \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500

def aggregate_campaigns(rows):
    totals = {"cost": 0, "clicks": 0, "impressions": 0, "conversions": 0, "conversions_value": 0, "all_conversions": 0}
    campaigns = []
    channel_map = {
        "SEARCH": "Search", "PERFORMANCE_MAX": "PMax",
        "DISPLAY": "Display", "SHOPPING": "Shopping", "VIDEO": "Video",
    }
    for row in rows:
        c = row.campaign
        m = row.metrics
        b = row.campaign_budget
        cost = micros(m.cost_micros)
        cpc = micros(m.average_cpc)
        cpa = (cost / m.conversions) if m.conversions > 0 else 0
        roas = (m.conversions_value / cost) if cost > 0 and m.conversions_value > 0 else 0
        budget_daily = micros(b.amount_micros) if b.amount_micros else 0
        totals["cost"] += cost
        totals["clicks"] += m.clicks
        totals["impressions"] += m.impressions
        totals["conversions"] += m.conversions
        totals["conversions_value"] += m.conversions_value
        totals["all_conversions"] += m.all_conversions
        campaigns.append({
            "name": c.name,
            "channel": channel_map.get(c.advertising_channel_type.name, c.advertising_channel_type.name),
            "status": "ATIVA" if c.status.name == "ENABLED" else "PAUSADA",
            "is_search": c.advertising_channel_type.name in ("SEARCH",),
            "cost": cost, "clicks": m.clicks, "impressions": m.impressions,
            "ctr": m.ctr * 100, "cpc": cpc,
            "conversions": m.conversions, "cpa": cpa,
            "conversions_value": m.conversions_value, "roas": roas,
            "all_conversions": m.all_conversions,
            "budget_daily": budget_daily,
            "impr_share": m.search_impression_share,
            "lost_rank": m.search_rank_lost_impression_share,
            "lost_budget": m.search_budget_lost_impression_share,
            "top_share": m.search_top_impression_share,
            "abs_top": m.search_absolute_top_impression_share,
        })
    totals["ctr"] = (totals["clicks"] / totals["impressions"] * 100) if totals["impressions"] > 0 else 0
    totals["cpc"] = (totals["cost"] / totals["clicks"]) if totals["clicks"] > 0 else 0
    totals["cpa"] = (totals["cost"] / totals["conversions"]) if totals["conversions"] > 0 else 0
    totals["roas"] = (totals["conversions_value"] / totals["cost"]) if totals["cost"] > 0 and totals["conversions_value"] > 0 else 0
    return campaigns, totals


def aggregate_devices(rows):
    device_names = {"DESKTOP": "Desktop", "MOBILE": "Mobile", "TABLET": "Tablet", "CONNECTED_TV": "CTV", "OTHER": "Outro"}
    device_map = {}
    for row in rows:
        dev = row.segments.device.name
        label = device_names.get(dev, dev)
        m = row.metrics
        if label not in device_map:
            device_map[label] = {"clicks": 0, "cost": 0, "conversions": 0, "impressions": 0}
        device_map[label]["clicks"] += m.clicks
        device_map[label]["cost"] += micros(m.cost_micros)
        device_map[label]["conversions"] += m.conversions
        device_map[label]["impressions"] += m.impressions
    result = []
    for label, d in sorted(device_map.items(), key=lambda x: -x[1]["cost"]):
        cpa = d["cost"] / d["conversions"] if d["conversions"] > 0 else 0
        ctr = (d["clicks"] / d["impressions"] * 100) if d["impressions"] > 0 else 0
        result.append({"device": label, "cpa": cpa, "ctr": ctr, **d})
    return result


def build_qs_map(qs_rows):
    quality_labels = {"BELOW_AVERAGE": "\u2b07 Abaixo", "AVERAGE": "\u2192 Medio", "ABOVE_AVERAGE": "\u2b06 Acima", "UNKNOWN": "\u2014"}
    qs_map = {}
    for row in qs_rows:
        kw = row.ad_group_criterion
        key = kw.keyword.text.lower().strip()
        qs = kw.quality_info.quality_score
        qs_map[key] = {
            "qs": qs if qs > 0 else None,
            "creative": quality_labels.get(kw.quality_info.creative_quality_score.name, "\u2014"),
            "landing": quality_labels.get(kw.quality_info.post_click_quality_score.name, "\u2014"),
            "ctr_exp": quality_labels.get(kw.quality_info.search_predicted_ctr.name, "\u2014"),
        }
    return qs_map


def qs_icon(score):
    if score is None: return "\u2014"
    if score >= 7: return f"\U0001f7e2 {score}"
    if score >= 4: return f"\U0001f7e1 {score}"
    return f"\U0001f534 {score}"


def ad_strength_label(name):
    labels = {"POOR": "\U0001f534 Fraco", "AVERAGE": "\U0001f7e1 Regular", "GOOD": "\U0001f7e2 Bom", "EXCELLENT": "\u2b50 Excelente"}
    return labels.get(name, "\u2014")


def build_resumo_executivo(campaigns, cur, prev, qs_map, waste_count, waste_cost, currency):
    """Generates the qualitative Resumo Executivo block (what worked, what didn't, recommendations)."""
    def fmt(v): return format_currency(v, currency)

    positives = []
    negatives = []
    recommendations = []

    conv_change = ((cur["conversions"] - prev["conversions"]) / prev["conversions"] * 100) if prev["conversions"] > 0 else None
    cpa_change = ((cur["cpa"] - prev["cpa"]) / prev["cpa"] * 100) if prev["cpa"] > 0 and cur["cpa"] > 0 else None
    ctr_change = ((cur["ctr"] - prev["ctr"]) / prev["ctr"] * 100) if prev["ctr"] > 0 else None
    cost_change = ((cur["cost"] - prev["cost"]) / prev["cost"] * 100) if prev["cost"] > 0 else None

    # Conversions trend
    if conv_change is not None:
        if conv_change > 10:
            positives.append(f"Convers\u00f5es subiram {conv_change:+.1f}% ({prev['conversions']:.1f} \u2192 {cur['conversions']:.1f})")
        elif conv_change < -10:
            negatives.append(f"Convers\u00f5es ca\u00edram {abs(conv_change):.1f}% ({prev['conversions']:.1f} \u2192 {cur['conversions']:.1f})")

    # CPA trend
    if cpa_change is not None:
        if cpa_change < -10:
            positives.append(f"CPA melhorou {abs(cpa_change):.1f}% ({fmt(prev['cpa'])} \u2192 {fmt(cur['cpa'])})")
        elif cpa_change > 15:
            negatives.append(f"CPA aumentou {cpa_change:+.1f}% ({fmt(prev['cpa'])} \u2192 {fmt(cur['cpa'])})")

    # CTR trend
    if ctr_change is not None and abs(ctr_change) > 15:
        if ctr_change > 0:
            positives.append(f"CTR melhorou {ctr_change:+.1f}% ({prev['ctr']:.2f}% \u2192 {cur['ctr']:.2f}%)")
        else:
            negatives.append(f"CTR caiu {abs(ctr_change):.1f}% ({prev['ctr']:.2f}% \u2192 {cur['ctr']:.2f}%) \u2014 poss\u00edvel fadiga de an\u00fancios")
            recommendations.append("Renovar criativos/headlines dos an\u00fancios \u2014 CTR em queda indica fadiga")

    # ROAS
    if cur["roas"] > 0:
        roas_change = ((cur["roas"] - prev["roas"]) / prev["roas"] * 100) if prev["roas"] > 0 else None
        suffix = f" ({roas_change:+.1f}% vs per\u00edodo anterior)" if roas_change is not None else ""
        if cur["roas"] >= 3:
            positives.append(f"ROAS consolidado saud\u00e1vel: {cur['roas']:.2f}x{suffix}")
        elif cur["roas"] < 1.5:
            negatives.append(f"ROAS abaixo de 1.5x ({cur['roas']:.2f}x) \u2014 custo supera receita gerada")
            recommendations.append("Revisar estrat\u00e9gia de lances e segmenta\u00e7\u00e3o \u2014 ROAS abaixo do m\u00ednimo saud\u00e1vel")

    # Best/worst campaign by CPA
    active_conv = [c for c in campaigns if c["status"] == "ATIVA" and c["conversions"] > 0]
    if active_conv:
        best = min(active_conv, key=lambda x: x["cpa"])
        positives.append(f"Melhor CPA: **{best['name']}** \u2192 {fmt(best['cpa'])} ({best['conversions']:.1f} conv.)")
        if len(active_conv) > 1:
            worst = max(active_conv, key=lambda x: x["cpa"])
            if worst["name"] != best["name"] and cur["cpa"] > 0 and worst["cpa"] > cur["cpa"] * 1.5:
                gap = (worst["cpa"] - cur["cpa"]) / cur["cpa"] * 100
                negatives.append(f"CPA mais alto: **{worst['name']}** \u2192 {fmt(worst['cpa'])} ({gap:+.0f}% acima da m\u00e9dia da conta)")
                recommendations.append(f"Otimizar lances em **{worst['name']}** para reduzir CPA")

    # Quality Score
    low_qs = [kw for kw, info in qs_map.items() if info.get("qs") is not None and info["qs"] <= 3]
    good_qs = [kw for kw, info in qs_map.items() if info.get("qs") is not None and info["qs"] >= 7]
    if good_qs:
        positives.append(f"{len(good_qs)} keyword(s) com Quality Score \u2265 7 (boa relev\u00e2ncia)")
    if low_qs:
        sample = ", ".join(f"\"{k}\"" for k in low_qs[:3])
        negatives.append(f"{len(low_qs)} keyword(s) com QS \u2264 3: {sample}")
        recommendations.append(f"Revisar ou pausar keywords com QS \u2264 3: {sample}")

    # Wasted spend
    if waste_count > 0:
        recommendations.append(f"Adicionar {waste_count} termo(s) como negativas \u2014 desperd\u00edcio estimado de {fmt(waste_cost)}")

    # General trends
    if conv_change is not None and conv_change < -15:
        recommendations.append("Revisar criativos e p\u00e1ginas de destino \u2014 queda expressiva de convers\u00f5es no per\u00edodo")
    if cpa_change is not None and cpa_change > 20:
        recommendations.append("Ajustar estrat\u00e9gia de lance \u2014 CPA crescendo acima do esperado")

    if not positives:
        positives.append("Per\u00edodo est\u00e1vel \u2014 sem varia\u00e7\u00f5es positivas expressivas a destacar")
    if not negatives:
        negatives.append("Sem alertas cr\u00edticos identificados no per\u00edodo")
    if not recommendations:
        recommendations.append("Manter estrat\u00e9gia atual e acompanhar tend\u00eancia nas pr\u00f3ximas semanas")

    block = ["## \U0001f9ed Resumo Executivo", "", "### \u2705 O que deu certo"]
    for p in positives:
        block.append(f"- {p}")
    block += ["", "### \u274c O que n\u00e3o deu certo"]
    for n in negatives:
        block.append(f"- {n}")
    block += ["", "### \U0001f680 O que podemos fazer para melhorar"]
    for i, r in enumerate(recommendations, 1):
        block.append(f"{i}. {r}")
    return block


# \u2500\u2500 Report generation \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500

def generate_report(customer_id, mcc_id, client_name, currency, start_date=None, end_date=None):
    client = get_client(mcc_id)
    service = client.get_service("GoogleAdsService")

    if start_date and end_date:
        from datetime import datetime
        cur_start = datetime.strptime(start_date, "%Y-%m-%d").date()
        cur_end = datetime.strptime(end_date, "%Y-%m-%d").date()
        period_days = (cur_end - cur_start).days + 1
        prev_end = cur_start - timedelta(days=1)
        prev_start = prev_end - timedelta(days=period_days - 1)
    else:
        cur_start, cur_end = date_range(7, 1)
        prev_start, prev_end = date_range(14, 8)

    def fmt(v): return format_currency(v, currency)

    cur_rows = fetch_campaign_metrics(service, customer_id, cur_start, cur_end)
    prev_rows = fetch_campaign_metrics(service, customer_id, prev_start, prev_end)
    search_rows = fetch_search_terms(service, customer_id, cur_start, cur_end)
    kw_rows = fetch_keywords(service, customer_id, cur_start, cur_end)
    qs_rows = fetch_keyword_quality_scores(service, customer_id)
    device_rows = fetch_device_breakdown(service, customer_id, cur_start, cur_end)
    adgroup_rows = fetch_ad_groups(service, customer_id, cur_start, cur_end)
    ad_rows = fetch_ads(service, customer_id, cur_start, cur_end)

    campaigns, cur = aggregate_campaigns(cur_rows)
    _, prev = aggregate_campaigns(prev_rows)
    devices = aggregate_devices(device_rows)
    qs_map = build_qs_map(qs_rows)

    # Compute waste terms early (used both in Resumo Executivo and in the search terms section)
    waste_terms = [r for r in search_rows if micros(r.metrics.cost_micros) > 0 and r.metrics.conversions == 0 and r.metrics.clicks >= 3]
    waste_count = len(waste_terms)
    waste_cost = sum(micros(r.metrics.cost_micros) for r in waste_terms)

    week_label = f"{cur_start.strftime('%d/%m/%Y')} a {cur_end.strftime('%d/%m/%Y')}"
    prev_label = f"{prev_start.strftime('%d/%m/%Y')} a {prev_end.strftime('%d/%m/%Y')}"
    generated_at = date.today().strftime("%d/%m/%Y")

    match_map = {"EXACT": "Exata", "PHRASE": "Frase", "BROAD": "Ampla"}

    lines = [
        f"# Relatorio Google Ads \u2014 {client_name}",
        f"",
        f"**Periodo analisado:** {week_label}",
        f"**Semana anterior:** {prev_label}",
        f"**Conta:** {customer_id}",
        f"**Gerado em:** {generated_at}",
        f"",
        f"---",
        f"",
    ]

    # \u2500\u2500 Resumo Executivo (what worked / what didn't / recommendations) \u2500\u2500\u2500\u2500\u2500\u2500
    lines += build_resumo_executivo(campaigns, cur, prev, qs_map, waste_count, waste_cost, currency)
    lines += [
        f"",
        f"---",
        f"",
        f"## Resumo da Semana",
        f"",
        f"| Metrica | Semana Atual | Semana Anterior | Variacao |",
        f"|---|---|---|---|",
        f"| Gasto total | {fmt(cur['cost'])} | {fmt(prev['cost'])} | {pct_change(cur['cost'], prev['cost']) or '--'} |",
        f"| Cliques | {cur['clicks']:,} | {prev['clicks']:,} | {pct_change(cur['clicks'], prev['clicks']) or '--'} |",
        f"| Impressoes | {cur['impressions']:,} | {prev['impressions']:,} | {pct_change(cur['impressions'], prev['impressions']) or '--'} |",
        f"| CTR | {cur['ctr']:.2f}% | {prev['ctr']:.2f}% | {pct_change(cur['ctr'], prev['ctr']) or '--'} |",
        f"| CPC medio | {fmt(cur['cpc'])} | {fmt(prev['cpc'])} | {pct_change(cur['cpc'], prev['cpc']) or '--'} |",
        f"| Conversoes | {cur['conversions']:.1f} | {prev['conversions']:.1f} | {pct_change(cur['conversions'], prev['conversions']) or '--'} |",
        f"| CPA | {fmt(cur['cpa'])} | {fmt(prev['cpa'])} | {pct_change(cur['cpa'], prev['cpa']) or '--'} |",
    ]

    if cur["roas"] > 0 or prev["roas"] > 0:
        lines.append(f"| ROAS | {cur['roas']:.2f}x | {prev['roas']:.2f}x | {pct_change(cur['roas'], prev['roas']) or '--'} |")

    if cur["all_conversions"] > cur["conversions"]:
        diff = cur["all_conversions"] - cur["conversions"]
        lines.append(f"| Micro-conversoes | +{diff:.1f} (total {cur['all_conversions']:.1f}) | \u2014 | \u2014 |")

    lines += ["", "---", "", "## Campanhas", ""]

    if not campaigns:
        lines.append("_Nenhuma campanha com dados no periodo._")
    else:
        for camp in campaigns:
            status_icon = "\U0001f7e2 ATIVA" if camp["status"] == "ATIVA" else "\u23f8 PAUSADA"
            lines += [
                f"### {camp['name']} | {camp['channel']} | {status_icon}",
                f"",
                f"| Metrica | Valor |",
                f"|---|---|",
                f"| Gasto | {fmt(camp['cost'])} |",
                f"| Orcamento diario | {fmt(camp['budget_daily'])} |",
                f"| Cliques | {camp['clicks']:,} |",
                f"| Impressoes | {camp['impressions']:,} |",
                f"| CTR | {camp['ctr']:.2f}% |",
                f"| CPC medio | {fmt(camp['cpc'])} |",
                f"| Conversoes | {camp['conversions']:.1f} |",
                f"| CPA | {fmt(camp['cpa'])} |",
            ]
            if camp["roas"] > 0:
                lines.append(f"| ROAS | {camp['roas']:.2f}x |")
            if camp["is_search"]:
                lines += [
                    f"| Impression Share | {safe_pct(camp['impr_share'])} |",
                    f"| Perdido por rank | {safe_pct(camp['lost_rank'])} |",
                    f"| Perdido por orcamento | {safe_pct(camp['lost_budget'])} |",
                    f"| Top of Page | {safe_pct(camp['top_share'])} |",
                    f"| Topo absoluto | {safe_pct(camp['abs_top'])} |",
                ]
            lines.append("")

    # \u2500\u2500 Dispositivos \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
    lines += ["---", "", "## Breakdown por Dispositivo", ""]
    if devices:
        lines += [
            "| Dispositivo | Cliques | Gasto | Conversoes | CPA | CTR |",
            "|---|---|---|---|---|---|",
        ]
        for d in devices:
            lines.append(
                f"| {d['device']} | {d['clicks']:,} | {fmt(d['cost'])} | {d['conversions']:.1f} | {fmt(d['cpa'])} | {d['ctr']:.2f}% |"
            )
    else:
        lines.append("_Sem dados de dispositivo no periodo._")

    # \u2500\u2500 Grupos de an\u00fancios \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
    lines += ["", "---", "", "## Grupos de Anuncios", ""]
    if adgroup_rows:
        lines += [
            "| Grupo | Campanha | Cliques | Gasto | Conversoes | CPA | CTR |",
            "|---|---|---|---|---|---|---|",
        ]
        for row in adgroup_rows:
            m = row.metrics
            cost = micros(m.cost_micros)
            cpa = cost / m.conversions if m.conversions > 0 else 0
            lines.append(
                f"| {row.ad_group.name} | {row.campaign.name} | {m.clicks:,} | {fmt(cost)} | {m.conversions:.1f} | {fmt(cpa)} | {m.ctr * 100:.2f}% |"
            )
    else:
        lines.append("_Sem dados de grupos de anuncios no periodo._")

    # \u2500\u2500 An\u00fancios ativos \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
    lines += ["", "---", "", "## Anuncios Ativos", ""]
    if ad_rows:
        lines += [
            "| Titulo (RSA) | Forca | Grupo | Campanha | Impressoes | Cliques | Conv. | CTR |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for row in ad_rows:
            ad = row.ad_group_ad.ad
            m = row.metrics
            strength = ad_strength_label(row.ad_group_ad.ad_strength.name)
            try:
                headlines = ad.responsive_search_ad.headlines
                title = headlines[0].text if headlines else f"[{ad.type_.name}]"
            except Exception:
                title = f"[{ad.type_.name}]"
            title = title[:50]
            lines.append(
                f"| {title} | {strength} | {row.ad_group.name} | {row.campaign.name} | {m.impressions:,} | {m.clicks:,} | {m.conversions:.1f} | {m.ctr * 100:.2f}% |"
            )
    else:
        lines.append("_Sem dados de anuncios no periodo._")

    # \u2500\u2500 Palavras-chave \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
    lines += [
        "", "---", "", "## Palavras-chave Ativas", "",
        "| Palavra-chave | Tipo | QS | CTR exp. | Anuncio | Pag. dest. | Campanha | Cliques | Gasto | Conv. | CTR |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for row in kw_rows:
        kw = row.ad_group_criterion.keyword
        m = row.metrics
        cost = micros(m.cost_micros)
        match = match_map.get(kw.match_type.name, kw.match_type.name)
        qs_info = qs_map.get(kw.text.lower().strip(), {})
        qs_display = qs_icon(qs_info.get("qs"))
        ctr_exp = qs_info.get("ctr_exp", "\u2014")
        ad_quality = qs_info.get("creative", "\u2014")
        landing_quality = qs_info.get("landing", "\u2014")
        lines.append(
            f"| {kw.text} | {match} | {qs_display} | {ctr_exp} | {ad_quality} | {landing_quality} | {row.campaign.name} | {m.clicks:,} | {fmt(cost)} | {m.conversions:.1f} | {m.ctr * 100:.2f}% |"
        )
    if not kw_rows:
        lines.append("_Nenhuma palavra-chave com dados no periodo._")

    # \u2500\u2500 Keywords com melhor performance (SOP M\u00f3dulo 4) \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
    lines += ["", "---", "", "## \u2b50 Keywords com Melhor Performance (Geradoras de Convers\u00e3o)", ""]
    conv_kws = sorted(
        [r for r in kw_rows if r.metrics.conversions > 0],
        key=lambda r: micros(r.metrics.cost_micros) / r.metrics.conversions
    )
    if conv_kws:
        lines += [
            "| Keyword | Tipo | Campanha | Conv. | CPA | CTR | QS | A\u00e7\u00e3o |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for i, row in enumerate(conv_kws[:10]):
            kw = row.ad_group_criterion.keyword
            m = row.metrics
            cost = micros(m.cost_micros)
            cpa_kw = cost / m.conversions
            match = match_map.get(kw.match_type.name, kw.match_type.name)
            qs_info = qs_map.get(kw.text.lower().strip(), {})
            qs_display = qs_icon(qs_info.get("qs"))
            star = "\u2b50 VENCEDORA" if i == 0 else ("\ud83d\udfe2 Escalar" if cpa_kw <= cur["cpa"] * 0.8 else "\ud83d\udfe2 Manter")
            lines.append(f"| {kw.text} | {match} | {row.campaign.name} | {m.conversions:.1f} | {fmt(cpa_kw)} | {m.ctr * 100:.2f}% | {qs_display} | {star} |")
    else:
        lines.append("_Nenhuma keyword com convers\u00e3o no per\u00edodo._")

    lines += ["", "---", "", "## \ud83d\udd34 Keywords com Perda de Verba (Sem Convers\u00e3o)", ""]
    waste_kws = [r for r in kw_rows if r.metrics.conversions == 0 and micros(r.metrics.cost_micros) > 0]
    waste_kws_sorted = sorted(waste_kws, key=lambda r: micros(r.metrics.cost_micros), reverse=True)
    if waste_kws_sorted:
        lines += [
            "| Keyword | Tipo | Campanha | Gasto | Cliques | QS | Diagn\u00f3stico | A\u00e7\u00e3o |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for row in waste_kws_sorted[:15]:
            kw = row.ad_group_criterion.keyword
            m = row.metrics
            cost = micros(m.cost_micros)
            match = match_map.get(kw.match_type.name, kw.match_type.name)
            qs_info = qs_map.get(kw.text.lower().strip(), {})
            qs_val = qs_info.get("qs")
            if qs_val and qs_val <= 3:
                diag = "QS baixo \u2014 relev\u00e2ncia fraca"
                action = "\ud83d\udd34 Reescrever an\u00fancio/LP"
            elif match == "Ampla":
                diag = "Match Ampla \u2014 tr\u00e1fego irrelevante"
                action = "\ud83d\udfe1 Trocar para Frase/Exata"
            elif cost > cur["cpa"] * 3 if cur["cpa"] > 0 else cost > 50:
                diag = f"Gasto {fmt(cost)} sem retorno"
                action = "\ud83d\udd34 Pausar"
            else:
                diag = "Ainda em aprendizado"
                action = "\ud83d\udfe1 Monitorar"
            lines.append(f"| {kw.text} | {match} | {row.campaign.name} | {fmt(cost)} | {m.clicks:,} | {qs_icon(qs_val)} | {diag} | {action} |")
    else:
        lines.append("_Todas as keywords geraram convers\u00f5es no per\u00edodo._")

    # \u2500\u2500 Termos de pesquisa \u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500\u2500
    lines += [
        "", "---", "", "## Termos de Pesquisa", "",
        "### Termos com gasto e zero conversao (candidatos a negativa)", "",
        "| Termo | Campanha | Cliques | Gasto | CTR |",
        "|---|---|---|---|---|",
    ]
    if waste_terms:
        for row in waste_terms:
            m = row.metrics
            lines.append(f"| {row.search_term_view.search_term} | {row.campaign.name} | {m.clicks:,} | {fmt(micros(m.cost_micros))} | {m.ctr * 100:.2f}% |")
    else:
        lines.append("_Nenhum termo com desperdicio identificado._")

    lines += [
        "", "### Todos os termos do periodo", "",
        "| Termo | Campanha | Cliques | Gasto | Conv. | CTR |",
        "|---|---|---|---|---|---|",
    ]
    for row in search_rows:
        m = row.metrics
        lines.append(f"| {row.search_term_view.search_term} | {row.campaign.name} | {m.clicks:,} | {fmt(micros(m.cost_micros))} | {m.conversions:.1f} | {m.ctr * 100:.2f}% |")
    if not search_rows:
        lines.append("_Nenhum termo de pesquisa encontrado no periodo._")

    # ── Pacing Monitor (SOP Módulo 6) ────────────────────────────────────────────
    lines += ["", "---", "", "## 📊 Pacing Monitor (Ritmo de Gasto)", ""]
    today_dt = date.today()
    days_in_month = (date(today_dt.year + today_dt.month // 12, today_dt.month % 12 + 1, 1) - timedelta(days=1)).day
    total_daily_budget = sum(c["budget_daily"] for c in campaigns)
    monthly_budget_est = total_daily_budget * days_in_month
    weekly_spend = cur["cost"]
    monthly_projected = (weekly_spend / 7) * days_in_month
    pct_mes = (today_dt.day / days_in_month) * 100
    lines += [
        f"Dia **{today_dt.day}** de {days_in_month} do mês ({pct_mes:.0f}% do período).",
        f"- Gasto semanal: **{fmt(weekly_spend)}**",
        f"- Projeção mensal (ritmo atual): **{fmt(monthly_projected)}**",
    ]
    if monthly_budget_est > 0:
        lines.append(f"- Budget estimado (orçamentos diários × {days_in_month} dias): {fmt(monthly_budget_est)}")
        pct_proj = (monthly_projected / monthly_budget_est) * 100
        diff = pct_proj - pct_mes
        if abs(diff) <= 10:
            lines.append(f"- Status: 🟢 NO RITMO — projeção {fmt(monthly_projected)} alinhada com o mês")
        elif diff > 10:
            lines.append(f"- Status: 🔴 ACELERADO — projeção {int(pct_proj)}% do budget vs {int(pct_mes)}% do mês decorrido")
        else:
            lines.append(f"- Status: 🟡 LENTO — projeção {int(pct_proj)}% do budget vs {int(pct_mes)}% do mês decorrido")
    else:
        lines.append("- Status: ⚠️ Budget diário não configurado nas campanhas")

    # ── Bloco Trello (SOP formato obrigatório) ───────────────────────────────────
    cpa_var_str = pct_change(cur["cpa"], prev["cpa"]) or "---"
    conv_var_str = pct_change(cur["conversions"], prev["conversions"]) or "---"
    if monthly_budget_est > 0:
        pct_proj2 = (monthly_projected / monthly_budget_est) * 100
        diff2 = pct_proj2 - pct_mes
        if abs(diff2) <= 10:   pac_icon, pac_st = "🟢", "NO RITMO"
        elif diff2 > 10:       pac_icon, pac_st = "🔴", "ACELERADO"
        else:                  pac_icon, pac_st = "🟡", "LENTO"
        pacing_trello = f"Pacing: {pac_icon} {pac_st} — Projeção {fmt(monthly_projected)} vs Budget est. {fmt(monthly_budget_est)} ({int(pct_mes)}% do mês)"
    else:
        pacing_trello = "Pacing: ⚠️ Budget não configurado"

    lines += [
        "", "---", "",
        "## 🟦 RESUMO FINAL PARA TRELLO — copie e cole quando quiser postar", "",
        f"📊 Google Ads {client_name} — {generated_at}",
        f"💰 Gasto: {fmt(cur['cost'])} | 🎯 Conversões: {cur['conversions']:.0f} | 📉 CPA: {fmt(cur['cpa'])}",
        f"Variação vs semana anterior: CPA {cpa_var_str} | Conversões {conv_var_str}",
        pacing_trello,
        "",
    ]
    for camp in campaigns:
        if camp["status"] != "ATIVA" or camp["cost"] == 0:
            continue
        camp_conv_kws = sorted(
            [r for r in kw_rows if r.campaign.name == camp["name"] and r.metrics.conversions > 0],
            key=lambda r: micros(r.metrics.cost_micros) / r.metrics.conversions
        )
        winner_kw = camp_conv_kws[0] if camp_conv_kws else None
        camp_waste_terms = [r for r in waste_terms if r.campaign.name == camp["name"]]

        lines += ["---", "", f"📌 Campanha: {camp['name']}", "", "✅ O que está funcionando:"]
        if winner_kw:
            kw_txt = winner_kw.ad_group_criterion.keyword.text
            kw_cpa = micros(winner_kw.metrics.cost_micros) / winner_kw.metrics.conversions
            kw_ctr = winner_kw.metrics.ctr * 100
            lines.append(f"- Keyword `{kw_txt}` — CTR {kw_ctr:.2f}% | CPA {fmt(kw_cpa)}")
        if camp["conversions"] > 0:
            lines.append(f"- {camp['conversions']:.0f} conversões no período (CPA {fmt(camp['cpa'])})")
        if camp["impr_share"] and float(camp["impr_share"]) > 0 and float(camp["impr_share"]) >= 0.6:
            lines.append(f"- Impression Share {safe_pct(camp['impr_share'])} — boa cobertura")
        if not winner_kw and camp["conversions"] == 0:
            lines.append("- Nenhum resultado positivo identificado nesta semana")

        lines += ["", "❌ O que não está funcionando:"]
        if camp_waste_terms:
            for r in camp_waste_terms[:2]:
                m_w = r.metrics
                lines.append(f"- `{r.search_term_view.search_term}` — {fmt(micros(m_w.cost_micros))} gastos, 0 conversões")
        if camp["conversions"] == 0 and camp["cost"] > 0:
            lines.append(f"- 0 conversões com {fmt(camp['cost'])} investidos")
        if camp["lost_budget"] and float(camp["lost_budget"]) > 0.2:
            lines.append(f"- IS perdida por orçamento: {safe_pct(camp['lost_budget'])} — budget limitando alcance")
        if camp["lost_rank"] and float(camp["lost_rank"]) > 0.2:
            lines.append(f"- IS perdida por qualidade: {safe_pct(camp['lost_rank'])} — melhorar QS")
        if not camp_waste_terms and camp["conversions"] > 0:
            lines.append("- Sem problemas críticos nesta campanha")

        lines.append("")
        if winner_kw:
            kw_txt = winner_kw.ad_group_criterion.keyword.text
            kw_match = match_map.get(winner_kw.ad_group_criterion.keyword.match_type.name, "")
            kw_cpa = micros(winner_kw.metrics.cost_micros) / winner_kw.metrics.conversions
            kw_ctr = winner_kw.metrics.ctr * 100
            lines.append(f"⭐ Keyword vencedora: `{kw_txt}` [{kw_match}] — CTR {kw_ctr:.2f}% | CPA {fmt(kw_cpa)}")
        else:
            lines.append("⭐ Keyword vencedora: a definir — aguardar mais volume no período")

        if camp_waste_terms:
            lines += ["", "🚫 Negativações da semana:"]
            for r in camp_waste_terms[:5]:
                lines.append(f"- {r.search_term_view.search_term}")

        lines += ["", "🔧 O que precisa ser feito:"]
        trello_actions = []
        if camp_waste_terms:
            terms_str = ", ".join(f'"{r.search_term_view.search_term}"' for r in camp_waste_terms[:3])
            trello_actions.append(f"Negativar termos: {terms_str}")
        if winner_kw:
            kw_cpa2 = micros(winner_kw.metrics.cost_micros) / winner_kw.metrics.conversions
            if cur["cpa"] > 0 and kw_cpa2 <= cur["cpa"] * 0.8:
                trello_actions.append(f"Aumentar bid na keyword `{winner_kw.ad_group_criterion.keyword.text}` — CPA abaixo da média")
        if camp["lost_rank"] and float(camp["lost_rank"]) > 0.2:
            trello_actions.append("Revisar RSA — melhorar Quality Score")
        if camp["lost_budget"] and float(camp["lost_budget"]) > 0.2:
            trello_actions.append(f"Aumentar budget diário — perdendo {safe_pct(camp['lost_budget'])} de IS")
        if not trello_actions:
            trello_actions.append("Monitorar — sem ações urgentes identificadas")
        for a in trello_actions:
            lines.append(f"- {a}")
        lines.append("")
    lines.append("---")

    lines += ["", "---", "", "_Relatorio gerado automaticamente via GitHub Actions + Google Ads API | Plus Digital_"]

    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--customer-id", required=True)
    parser.add_argument("--mcc-id", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--client-name", default="Nordika Aires")
    parser.add_argument("--currency", default="COP", choices=["BRL", "COP", "EUR", "USD"])
    parser.add_argument("--start-date", default=None, help="Data inicial YYYY-MM-DD (opcional)")
    parser.add_argument("--end-date", default=None, help="Data final YYYY-MM-DD (opcional)")
    args = parser.parse_args()

    report = generate_report(args.customer_id, args.mcc_id, args.client_name, args.currency,
                             args.start_date, args.end_date)

    report = report.encode("utf-8", errors="replace").decode("utf-8")
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Relatorio salvo em: {args.output}")
