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
    if currency == "EUR": return f"€{value:,.2f}"
    if currency == "USD": return f"US$ {value:,.2f}"
    return f"R$ {value:,.2f}"


def safe_pct(value):
    """Format impression share safely — returns '—' for unavailable/NaN values."""
    try:
        v = float(value)
        if v <= 0 or v != v: return "—"
        return f"{v * 100:.1f}%"
    except Exception:
        return "—"


def pct_change(current, previous):
    if previous == 0: return None
    change = ((current - previous) / previous) * 100
    arrow = "↑" if change >= 0 else "↓"
    return f"{arrow} {change:+.1f}%"


def date_range(days_ago_start, days_ago_end):
    today = date.today()
    end = today - timedelta(days=days_ago_end)
    start = today - timedelta(days=days_ago_start)
    return start, end


# ── Query functions ──────────────────────────────────────────────────────────

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


# ── Aggregation helpers ──────────────────────────────────────────────────────

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
    quality_labels = {"BELOW_AVERAGE": "⬇ Abaixo", "AVERAGE": "→ Médio", "ABOVE_AVERAGE": "⬆ Acima", "UNKNOWN": "—"}
    qs_map = {}
    for row in qs_rows:
        kw = row.ad_group_criterion
        key = kw.keyword.text.lower().strip()
        qs = kw.quality_info.quality_score
        qs_map[key] = {
            "qs": qs if qs > 0 else None,
            "creative": quality_labels.get(kw.quality_info.creative_quality_score.name, "—"),
            "landing": quality_labels.get(kw.quality_info.post_click_quality_score.name, "—"),
            "ctr_exp": quality_labels.get(kw.quality_info.search_predicted_ctr.name, "—"),
        }
    return qs_map


def qs_icon(score):
    if score is None: return "—"
    if score >= 7: return f"🟢 {score}"
    if score >= 4: return f"🟡 {score}"
    return f"🔴 {score}"


def ad_strength_label(name):
    labels = {"POOR": "🔴 Fraco", "AVERAGE": "🟡 Regular", "GOOD": "🟢 Bom", "EXCELLENT": "⭐ Excelente"}
    return labels.get(name, "—")


# ── Report generation ────────────────────────────────────────────────────────

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

    week_label = f"{cur_start.strftime('%d/%m/%Y')} a {cur_end.strftime('%d/%m/%Y')}"
    prev_label = f"{prev_start.strftime('%d/%m/%Y')} a {prev_end.strftime('%d/%m/%Y')}"
    generated_at = date.today().strftime("%d/%m/%Y")

    match_map = {"EXACT": "Exata", "PHRASE": "Frase", "BROAD": "Ampla"}

    lines = [
        f"# Relatorio Google Ads — {client_name}",
        f"",
        f"**Periodo analisado:** {week_label}",
        f"**Semana anterior:** {prev_label}",
        f"**Conta:** {customer_id}",
        f"**Gerado em:** {generated_at}",
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
        lines.append(f"| Micro-conversoes | +{diff:.1f} (total {cur['all_conversions']:.1f}) | — | — |")

    lines += ["", "---", "", "## Campanhas", ""]

    if not campaigns:
        lines.append("_Nenhuma campanha com dados no periodo._")
    else:
        for camp in campaigns:
            status_icon = "🟢 ATIVA" if camp["status"] == "ATIVA" else "⏸ PAUSADA"
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

    # ── Dispositivos ──────────────────────────────────────────────────────────
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

    # ── Grupos de anúncios ────────────────────────────────────────────────────
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

    # ── Anúncios ativos ───────────────────────────────────────────────────────
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

    # ── Palavras-chave ────────────────────────────────────────────────────────
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
        ctr_exp = qs_info.get("ctr_exp", "—")
        ad_quality = qs_info.get("creative", "—")
        landing_quality = qs_info.get("landing", "—")
        lines.append(
            f"| {kw.text} | {match} | {qs_display} | {ctr_exp} | {ad_quality} | {landing_quality} | {row.campaign.name} | {m.clicks:,} | {fmt(cost)} | {m.conversions:.1f} | {m.ctr * 100:.2f}% |"
        )
    if not kw_rows:
        lines.append("_Nenhuma palavra-chave com dados no periodo._")

    # ── Termos de pesquisa ────────────────────────────────────────────────────
    lines += [
        "", "---", "", "## Termos de Pesquisa", "",
        "### Termos com gasto e zero conversao (candidatos a negativa)", "",
        "| Termo | Campanha | Cliques | Gasto | CTR |",
        "|---|---|---|---|---|",
    ]
    waste_terms = [r for r in search_rows if micros(r.metrics.cost_micros) > 0 and r.metrics.conversions == 0 and r.metrics.clicks >= 3]
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

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Relatorio salvo em: {args.output}")

