"""
Read campaign metrics for a Google Ads account.
Usage: python3 google_ads_metrics_reader.py --customer-id CUSTOMER_ID [--days 30]
"""
import os
import sys
import argparse
from dotenv import load_dotenv
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

load_dotenv("/etc/secrets/.env", override=True)
load_dotenv(override=True)

def get_client():
    return GoogleAdsClient.load_from_dict({
        "developer_token": os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN"),
        "client_id": os.getenv("GOOGLE_ADS_CLIENT_ID"),
        "client_secret": os.getenv("GOOGLE_ADS_CLIENT_SECRET"),
        "refresh_token": os.getenv("GOOGLE_ADS_REFRESH_TOKEN"),
        "login_customer_id": os.getenv("GOOGLE_ADS_LOGIN_CUSTOMER_ID"),
        "use_proto_plus": True,
    })

def micros_to_brl(micros):
    return micros / 1_000_000

def build_date_filter(days):
    from datetime import date, timedelta
    literals = {7: "LAST_7_DAYS", 14: "LAST_14_DAYS", 30: "LAST_30_DAYS", 90: "LAST_90_DAYS"}
    if days == 0:
        return "segments.date DURING THIS_MONTH"
    if days in literals:
        return f"segments.date DURING {literals[days]}"
    end = date.today()
    start = end - timedelta(days=days - 1)
    return f"segments.date BETWEEN '{start}' AND '{end}'"

def read_metrics(customer_id, days=30):
    client = get_client()
    service = client.get_service("GoogleAdsService")

    date_filter = build_date_filter(days)
    label = "Maio 2026 (até hoje)" if days == 0 else f"Últimos {days} dias"

    query = f"""
        SELECT
            campaign.id,
            campaign.name,
            campaign.status,
            campaign.advertising_channel_type,
            campaign.bidding_strategy_type,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.conversions_value,
            metrics.ctr,
            metrics.average_cpc,
            metrics.search_impression_share,
            metrics.all_conversions
        FROM campaign
        WHERE {date_filter}
        AND campaign.status != 'REMOVED'
        ORDER BY metrics.cost_micros DESC
    """

    try:
        response = service.search(customer_id=customer_id, query=query)
        rows = list(response)
    except GoogleAdsException as ex:
        for error in ex.failure.errors:
            print(f"Erro API: {error.message}")
        return

    if not rows:
        print(f"Nenhuma campanha encontrada para conta {customer_id} nos últimos {days} dias.")
        return

    total_cost = 0
    total_clicks = 0
    total_impressions = 0
    total_conversions = 0
    total_conversions_value = 0

    print(f"\n{'='*80}")
    print(f"MÉTRICAS DE CAMPANHAS — Conta {customer_id} | {label}")
    print(f"{'='*80}\n")

    channel_map = {
        "SEARCH": "Search",
        "PERFORMANCE_MAX": "PMax",
        "DISPLAY": "Display",
        "SHOPPING": "Shopping",
        "VIDEO": "Video",
    }

    for row in rows:
        c = row.campaign
        m = row.metrics
        cost = micros_to_brl(m.cost_micros)
        cpc = micros_to_brl(m.average_cpc)
        roas = (m.conversions_value / cost) if cost > 0 else 0
        cpa = (cost / m.conversions) if m.conversions > 0 else 0
        channel = channel_map.get(c.advertising_channel_type.name, c.advertising_channel_type.name)
        status = "✓" if c.status.name == "ENABLED" else "✗"

        total_cost += cost
        total_clicks += m.clicks
        total_impressions += m.impressions
        total_conversions += m.conversions
        total_conversions_value += m.conversions_value

        print(f"{status} [{channel}] {c.name}")
        print(f"   Gasto: R$ {cost:,.2f} | Cliques: {m.clicks:,} | Impressões: {m.impressions:,}")
        print(f"   CTR: {m.ctr*100:.2f}% | CPC médio: R$ {cpc:.2f} | Conversões: {m.conversions:.1f}")
        if cost > 0:
            print(f"   CPA: R$ {cpa:.2f} | ROAS: {roas:.2f}x | Conv. Value: R$ {m.conversions_value:,.2f}")
        if m.search_impression_share > 0:
            print(f"   Share de impressão: {m.search_impression_share*100:.1f}%")
        print()

    total_roas = (total_conversions_value / total_cost) if total_cost > 0 else 0
    total_cpa = (total_cost / total_conversions) if total_conversions > 0 else 0

    print(f"{'='*80}")
    print(f"TOTAL DA CONTA")
    print(f"  Gasto: R$ {total_cost:,.2f} | Cliques: {total_clicks:,} | Impressões: {total_impressions:,}")
    print(f"  Conversões: {total_conversions:.1f} | CPA: R$ {total_cpa:.2f} | ROAS: {total_roas:.2f}x")
    print(f"{'='*80}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--customer-id", required=True, help="Google Ads customer ID (sem traços)")
    parser.add_argument("--days", type=int, default=30, help="Período em dias (padrão: 30)")
    args = parser.parse_args()
    read_metrics(args.customer_id, args.days)
