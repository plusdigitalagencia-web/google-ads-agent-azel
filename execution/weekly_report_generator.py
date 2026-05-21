"""
Generates a weekly Markdown report for a Google Ads account.
Usage: python3 weekly_report_generator.py --customer-id CUSTOMER_ID --mcc-id MCC_ID [--days 7] --output FILE.md
"""
import os
import sys
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


def build_date_range(days):
    end = date.today() - timedelta(days=1)
    start = end - timedelta(days=days - 1)
    return start, end


def micros(value):
    return value / 1_000_000


def generate_report(customer_id, mcc_id, days=7):
    client = get_client(mcc_id)
    service = client.get_service("GoogleAdsService")

    start, end = build_date_range(days)

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
            metrics.average_cpc,
            metrics.all_conversions
        FROM campaign
        WHERE segments.date BETWEEN '{start}' AND '{end}'
        AND campaign.status != 'REMOVED'
        ORDER BY metrics.cost_micros DESC
    """

    try:
        response = service.search(customer_id=customer_id, query=query)
        rows = list(response)
    except GoogleAdsException as ex:
        errors = [e.message for e in ex.failure.errors]
        raise RuntimeError(f"Google Ads API error: {'; '.join(errors)}")

    channel_map = {
        "SEARCH": "Search",
        "PERFORMANCE_MAX": "PMax",
        "DISPLAY": "Display",
        "SHOPPING": "Shopping",
        "VIDEO": "Video",
    }

    total_cost = total_clicks = total_impressions = total_conversions = 0
    campaigns = []

    for row in rows:
        c = row.campaign
        m = row.metrics
        cost = micros(m.cost_micros)
        cpc = micros(m.average_cpc)
        cpa = (cost / m.conversions) if m.conversions > 0 else 0
        channel = channel_map.get(c.advertising_channel_type.name, c.advertising_channel_type.name)
        status = "Ativa" if c.status.name == "ENABLED" else "Pausada"

        total_cost += cost
        total_clicks += m.clicks
        total_impressions += m.impressions
        total_conversions += m.conversions

        campaigns.append({
            "name": c.name,
            "channel": channel,
            "status": status,
            "cost": cost,
            "clicks": m.clicks,
            "impressions": m.impressions,
            "ctr": m.ctr * 100,
            "cpc": cpc,
            "conversions": m.conversions,
            "cpa": cpa,
        })

    total_ctr = (total_clicks / total_impressions * 100) if total_impressions > 0 else 0
    total_cpc = (total_cost / total_clicks) if total_clicks > 0 else 0
    total_cpa = (total_cost / total_conversions) if total_conversions > 0 else 0

    week_label = f"{start.strftime('%d/%m/%Y')} a {end.strftime('%d/%m/%Y')}"
    generated_at = date.today().strftime("%d/%m/%Y")

    lines = [
        f"# Relatório Semanal Google Ads — Nordika Aires",
        f"",
        f"**Período:** {week_label}  ",
        f"**Conta:** {customer_id}  ",
        f"**Gerado em:** {generated_at}",
        f"",
        f"---",
        f"",
        f"## Resumo da Conta",
        f"",
        f"| Métrica | Valor |",
        f"|---|---|",
        f"| Gasto total | R$ {total_cost:,.2f} |",
        f"| Cliques | {total_clicks:,} |",
        f"| Impressões | {total_impressions:,} |",
        f"| CTR médio | {total_ctr:.2f}% |",
        f"| CPC médio | R$ {total_cpc:.2f} |",
        f"| Conversões | {total_conversions:.1f} |",
        f"| CPA médio | R$ {total_cpa:.2f} |",
        f"",
        f"---",
        f"",
        f"## Campanhas",
        f"",
    ]

    if not campaigns:
        lines.append("_Nenhuma campanha com dados no período._")
    else:
        for camp in campaigns:
            lines += [
                f"### {camp['name']}",
                f"",
                f"| Métrica | Valor |",
                f"|---|---|",
                f"| Tipo | {camp['channel']} |",
                f"| Status | {camp['status']} |",
                f"| Gasto | R$ {camp['cost']:,.2f} |",
                f"| Cliques | {camp['clicks']:,} |",
                f"| Impressões | {camp['impressions']:,} |",
                f"| CTR | {camp['ctr']:.2f}% |",
                f"| CPC médio | R$ {camp['cpc']:.2f} |",
                f"| Conversões | {camp['conversions']:.1f} |",
                f"| CPA | R$ {camp['cpa']:.2f} |",
                f"",
            ]

    lines += [
        f"---",
        f"",
        f"_Relatório gerado automaticamente via GitHub Actions + Google Ads API_",
    ]

    return "\n".join(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--customer-id", required=True)
    parser.add_argument("--mcc-id", required=True)
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    report = generate_report(args.customer_id, args.mcc_id, args.days)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Relatório salvo em: {args.output}")
