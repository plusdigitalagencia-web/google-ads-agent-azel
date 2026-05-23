"""
Generates a weekly Markdown report for a Google Ads account.
Usage: python3 weekly_report_generator.py --customer-id CUSTOMER_ID --mcc-id MCC_ID --output FILE.md [--client-name NAME] [--currency BRL|COP]
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
    if currency == "COP":
        return f"COP {value:,.0f}"
    return f"R$ {value:,.2f}"


def pct_change(current, previous):
    if previous == 0:
        return None
    change = ((current - previous) / previous) * 100
    arrow = "↑" if change >= 0 else "↓"
    return f"{arrow} {change:+.1f}%"


def date_range(days_ago_start, days_ago_end):
    today = date.today()
    end = today - timedelta(days=days_ago_end)
    start = today - timedelta(days=days_ago_start)
    return start, end


def fetch_campaign_metrics(service, customer_id, start, end):
    query = f"""
        SELECT
            campaign.id,
            campaign.name,
            campaign.status,
            campaign.advertising_channel_type,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.ctr,
            metrics.average_cpc
        FROM campaign
        WHERE segments.date BETWEEN '{start}' AND '{end}'
        AND campaign.status != 'REMOVED'
        AND metrics.impressions > 0
        ORDER BY metrics.cost_micros DESC
    """
    response = service.search(customer_id=customer_id, query=query)
    return list(response)


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
    response = service.search(customer_id=customer_id, query=query)
    return list(response)


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
            metrics.ctr
        FROM keyword_view
        WHERE segments.date BETWEEN '{start}' AND '{end}'
        AND metrics.impressions > 0
        ORDER BY metrics.cost_micros DESC
    """
    response = service.search(customer_id=customer_id, query=query)
    return list(response)


def aggregate_campaigns(rows):
    totals = {"cost": 0, "clicks": 0, "impressions": 0, "conversions": 0}
    campaigns = []
    channel_map = {
        "SEARCH": "Search", "PERFORMANCE_MAX": "PMax",
        "DISPLAY": "Display", "SHOPPING": "Shopping", "VIDEO": "Video",
    }
    for row in rows:
        c = row.campaign
        m = row.metrics
        cost = micros(m.cost_micros)
        cpc = micros(m.average_cpc)
        cpa = (cost / m.conversions) if m.conversions > 0 else 0
        totals["cost"] += cost
        totals["clicks"] += m.clicks
        totals["impressions"] += m.impressions
        totals["conversions"] += m.conversions
        campaigns.append({
            "name": c.name,
            "channel": channel_map.get(c.advertising_channel_type.name, c.advertising_channel_type.name),
            "status": "ATIVA" if c.status.name == "ENABLED" else "PAUSADA",
            "cost": cost, "clicks": m.clicks, "impressions": m.impressions,
            "ctr": m.ctr * 100, "cpc": cpc,
            "conversions": m.conversions, "cpa": cpa,
        })
    totals["ctr"] = (totals["clicks"] / totals["impressions"] * 100) if totals["impressions"] > 0 else 0
    totals["cpc"] = (totals["cost"] / totals["clicks"]) if totals["clicks"] > 0 else 0
    totals["cpa"] = (totals["cost"] / totals["conversions"]) if totals["conversions"] > 0 else 0
    return campaigns, totals


def generate_report(customer_id, mcc_id, client_name, currency):
    client = get_client(mcc_id)
    service = client.get_service("GoogleAdsService")

    cur_start, cur_end = date_range(7, 1)
    prev_start, prev_end = date_range(14, 8)

    def fmt(v):
        return format_currency(v, currency)

    try:
        cur_rows = fetch_campaign_metrics(service, customer_id, cur_start, cur_end)
        prev_rows = fetch_campaign_metrics(service, customer_id, prev_start, prev_end)
        search_rows = fetch_search_terms(service, customer_id, cur_start, cur_end)
        kw_rows = fetch_keywords(service, customer_id, cur_start, cur_end)
    except GoogleAdsException as ex:
        errors = [e.message for e in ex.failure.errors]
        raise RuntimeError(f"Google Ads API error: {'; '.join(errors)}")

    campaigns, cur = aggregate_campaigns(cur_rows)
    _, prev = aggregate_campaigns(prev_rows)

    week_label = f"{cur_start.strftime('%d/%m/%Y')} a {cur_end.strftime('%d/%m/%Y')}"
    prev_label = f"{prev_start.strftime('%d/%m/%Y')} a {prev_end.strftime('%d/%m/%Y')}"
    generated_at = date.today().strftime("%d/%m/%Y")

    lines = [
        f"# Relatorio Google Ads -- {client_name}",
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
        f"",
        f"---",
        f"",
        f"## Campanhas",
        f"",
    ]

    if not campaigns:
        lines.append("_Nenhuma campanha com dados no periodo._")
    else:
        for camp in campaigns:
            status_icon = "ATIVA" if camp['status'] == "ATIVA" else "PAUSADA"
            lines += [
                f"### {camp['name']} | {camp['channel']} | {status_icon}",
                f"",
                f"| Metrica | Valor |",
                f"|---|---|",
                f"| Gasto | {fmt(camp['cost'])} |",
                f"| Cliques | {camp['clicks']:,} |",
                f"| Impressoes | {camp['impressions']:,} |",
                f"| CTR | {camp['ctr']:.2f}% |",
                f"| CPC medio | {fmt(camp['cpc'])} |",
                f"| Conversoes | {camp['conversions']:.1f} |",
                f"| CPA | {fmt(camp['cpa'])} |",
                f"",
            ]

    lines += [
        f"---",
        f"",
        f"## Palavras-chave Ativas",
        f"",
        f"| Palavra-chave | Tipo | Campanha | Cliques | Gasto | Conversoes | CTR |",
        f"|---|---|---|---|---|---|---|",
    ]

    match_map = {"EXACT": "Exata", "PHRASE": "Frase", "BROAD": "Ampla"}
    for row in kw_rows:
        kw = row.ad_group_criterion.keyword
        m = row.metrics
        cost = micros(m.cost_micros)
        match = match_map.get(kw.match_type.name, kw.match_type.name)
        lines.append(
            f"| {kw.text} | {match} | {row.campaign.name} | {m.clicks:,} | {fmt(cost)} | {m.conversions:.1f} | {m.ctr*100:.2f}% |"
        )

    if not kw_rows:
        lines.append("_Nenhuma palavra-chave com dados no periodo._")

    lines += [
        f"",
        f"---",
        f"",
        f"## Termos de Pesquisa",
        f"",
        f"### Termos com gasto e zero conversao",
        f"",
        f"| Termo | Campanha | Cliques | Gasto | CTR |",
        f"|---|---|---|---|---|",
    ]

    waste_terms = [r for r in search_rows if micros(r.metrics.cost_micros) > 0 and r.metrics.conversions == 0 and r.metrics.clicks >= 3]
    if waste_terms:
        for row in waste_terms:
            m = row.metrics
            lines.append(f"| {row.search_term_view.search_term} | {row.campaign.name} | {m.clicks:,} | {fmt(micros(m.cost_micros))} | {m.ctr*100:.2f}% |")
    else:
        lines.append("_Nenhum termo com desperdicio identificado._")

    lines += [
        f"",
        f"### Todos os termos do periodo",
        f"",
        f"| Termo | Campanha | Cliques | Gasto | Conversoes | CTR |",
        f"|---|---|---|---|---|---|",
    ]

    for row in search_rows:
        m = row.metrics
        lines.append(f"| {row.search_term_view.search_term} | {row.campaign.name} | {m.clicks:,} | {fmt(micros(m.cost_micros))} | {m.conversions:.1f} | {m.ctr*100:.2f}% |")

    if not search_rows:
        lines.append("_Nenhum termo de pesquisa encontrado no periodo._")

    lines += [
        f"",
        f"---",
        f"",
        f"_Relatorio gerado automaticamente via GitHub Actions + Google Ads API | Plus Digital_",
    ]

    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--customer-id", required=True)
    parser.add_argument("--mcc-id", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--client-name", default="Nordika Aires")
    parser.add_argument("--currency", default="COP", choices=["BRL", "COP"])
    args = parser.parse_args()

    report = generate_report(args.customer_id, args.mcc_id, args.client_name, args.currency)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Relatorio salvo em: {args.output}")
