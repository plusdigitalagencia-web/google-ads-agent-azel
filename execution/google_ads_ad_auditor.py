"""
Audit ads, headlines, descriptions, and extensions for Search and PMax campaigns.
Usage: python3 google_ads_ad_auditor.py --customer-id CUSTOMER_ID [--campaign-id ID]
"""
import os
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

def audit_search_ads(customer_id, campaign_id=None, days=30):
    client = get_client()
    service = client.get_service("GoogleAdsService")

    campaign_filter = f"AND campaign.id = {campaign_id}" if campaign_id else ""

    query = f"""
        SELECT
            ad_group_ad.ad.id,
            ad_group_ad.ad.responsive_search_ad.headlines,
            ad_group_ad.ad.responsive_search_ad.descriptions,
            ad_group_ad.ad.final_urls,
            ad_group_ad.status,
            ad_group_ad.ad_strength,
            ad_group_ad.policy_summary.approval_status,
            campaign.id,
            campaign.name,
            ad_group.name,
            metrics.impressions,
            metrics.clicks,
            metrics.ctr,
            metrics.conversions,
            metrics.cost_micros
        FROM ad_group_ad
        WHERE ad_group_ad.ad.type = 'RESPONSIVE_SEARCH_AD'
        AND ad_group_ad.status = 'ENABLED'
        AND campaign.status = 'ENABLED'
        AND segments.date DURING LAST_{days}_DAYS
        {campaign_filter}
        ORDER BY metrics.cost_micros DESC
    """

    try:
        response = service.search(customer_id=customer_id, query=query)
        rows = list(response)
    except GoogleAdsException as ex:
        for error in ex.failure.errors:
            print(f"Erro API Search Ads: {error.message}")
        return

    strength_map = {
        "EXCELLENT": "Excelente",
        "GOOD": "Bom",
        "AVERAGE": "Médio",
        "POOR": "Fraco",
        "PENDING": "Pendente",
        "UNSPECIFIED": "n/d",
    }

    print(f"\n{'='*80}")
    print(f"AUDITORIA DE ANÚNCIOS SEARCH — Conta {customer_id}")
    print(f"{'='*80}\n")

    for row in rows:
        ad = row.ad_group_ad.ad
        rsa = ad.responsive_search_ad
        m = row.metrics
        cost = m.cost_micros / 1_000_000
        strength = strength_map.get(row.ad_group_ad.ad_strength.name, "n/d")
        approval = row.ad_group_ad.policy_summary.approval_status.name

        print(f"Campanha: {row.campaign.name} > {row.ad_group.name}")
        print(f"Força do anúncio: {strength} | Status: {approval}")
        print(f"Métricas: R${cost:.2f} | {m.clicks} cliques | CTR: {m.ctr*100:.2f}% | Conv: {m.conversions:.1f}")

        print(f"Headlines ({len(rsa.headlines)}/15):")
        for h in rsa.headlines:
            pinned = f" [PIN {h.pinned_field.name}]" if h.pinned_field.name != "UNSPECIFIED" else ""
            print(f"  • {h.text}{pinned}")

        print(f"Descriptions ({len(rsa.descriptions)}/4):")
        for d in rsa.descriptions:
            pinned = f" [PIN {d.pinned_field.name}]" if d.pinned_field.name != "UNSPECIFIED" else ""
            print(f"  • {d.text}{pinned}")

        if ad.final_urls:
            print(f"URL final: {ad.final_urls[0]}")
        print()

def audit_pmax_assets(customer_id, campaign_id=None):
    client = get_client()
    service = client.get_service("GoogleAdsService")

    campaign_filter = f"AND campaign.id = {campaign_id}" if campaign_id else ""

    query = f"""
        SELECT
            asset_group.id,
            asset_group.name,
            asset_group.status,
            asset_group.ad_strength,
            asset_group.final_urls,
            campaign.name,
            campaign.id
        FROM asset_group
        WHERE campaign.advertising_channel_type = 'PERFORMANCE_MAX'
        AND campaign.status = 'ENABLED'
        {campaign_filter}
    """

    try:
        response = service.search(customer_id=customer_id, query=query)
        rows = list(response)
    except GoogleAdsException as ex:
        for error in ex.failure.errors:
            print(f"Erro API PMax: {error.message}")
        return

    if not rows:
        return

    print(f"\n{'='*80}")
    print(f"AUDITORIA PMAX — ASSET GROUPS — Conta {customer_id}")
    print(f"{'='*80}\n")

    strength_map = {
        "EXCELLENT": "Excelente", "GOOD": "Bom", "AVERAGE": "Médio",
        "POOR": "Fraco", "PENDING": "Pendente", "UNSPECIFIED": "n/d",
    }

    for row in rows:
        ag = row.asset_group
        strength = strength_map.get(ag.ad_strength.name, "n/d")
        urls = ", ".join(ag.final_urls) if ag.final_urls else "n/d"
        print(f"Campanha: {row.campaign.name}")
        print(f"Asset Group: {ag.name} | Força: {strength} | Status: {ag.status.name}")
        print(f"URLs: {urls}\n")

def audit_extensions(customer_id):
    client = get_client()
    service = client.get_service("GoogleAdsService")

    query = """
        SELECT
            campaign_asset.asset_type,
            campaign_asset.status,
            campaign.name
        FROM campaign_asset
        WHERE campaign_asset.status = 'ENABLED'
        AND campaign.status = 'ENABLED'
        ORDER BY campaign.name
    """

    try:
        response = service.search(customer_id=customer_id, query=query)
        rows = list(response)
    except GoogleAdsException as ex:
        for error in ex.failure.errors:
            print(f"Erro API Extensions: {error.message}")
        return

    if not rows:
        print("Nenhuma extensão ativa encontrada.")
        return

    print(f"\n{'='*80}")
    print(f"EXTENSÕES ATIVAS POR CAMPANHA — Conta {customer_id}")
    print(f"{'='*80}\n")

    from collections import defaultdict
    by_campaign = defaultdict(set)
    for row in rows:
        by_campaign[row.campaign.name].add(row.campaign_asset.asset_type.name)

    important_types = {"SITELINK", "CALLOUT", "STRUCTURED_SNIPPET", "CALL", "LEAD_FORM", "PROMOTION"}

    for camp_name, types in sorted(by_campaign.items()):
        present = types & important_types
        missing = important_types - types
        print(f"Campanha: {camp_name}")
        print(f"  ✓ Tem: {', '.join(sorted(present)) if present else 'nenhuma importante'}")
        if missing:
            print(f"  ✗ Faltam: {', '.join(sorted(missing))}")
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--customer-id", required=True)
    parser.add_argument("--campaign-id", help="Filtrar por campanha específica")
    parser.add_argument("--days", type=int, default=30)
    parser.add_argument("--type", choices=["search", "pmax", "extensions", "all"], default="all")
    args = parser.parse_args()

    if args.type in ("search", "all"):
        audit_search_ads(args.customer_id, args.campaign_id, args.days)
    if args.type in ("pmax", "all"):
        audit_pmax_assets(args.customer_id, args.campaign_id)
    if args.type in ("extensions", "all"):
        audit_extensions(args.customer_id)
