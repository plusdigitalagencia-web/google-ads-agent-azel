"""
Analyze active keywords and find new opportunities via Keyword Planner.
Usage: python3 google_ads_keyword_analyzer.py --customer-id CUSTOMER_ID [--campaign-id ID] [--new-ideas KEYWORD]
"""
import os
import argparse
from dotenv import load_dotenv
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

load_dotenv()

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

def analyze_keywords(customer_id, campaign_id=None, days=30):
    client = get_client()
    service = client.get_service("GoogleAdsService")

    campaign_filter = f"AND campaign.id = {campaign_id}" if campaign_id else ""

    query = f"""
        SELECT
            ad_group_criterion.keyword.text,
            ad_group_criterion.keyword.match_type,
            ad_group_criterion.quality_info.quality_score,
            ad_group_criterion.quality_info.creative_quality_score,
            ad_group_criterion.quality_info.post_click_quality_score,
            ad_group_criterion.quality_info.search_predicted_ctr,
            ad_group_criterion.status,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.average_cpc,
            metrics.ctr,
            campaign.name,
            ad_group.name
        FROM keyword_view
        WHERE segments.date DURING LAST_{days}_DAYS
        AND ad_group_criterion.status = 'ENABLED'
        AND campaign.status = 'ENABLED'
        {campaign_filter}
        ORDER BY metrics.cost_micros DESC
        LIMIT 200
    """

    try:
        response = service.search(customer_id=customer_id, query=query)
        rows = list(response)
    except GoogleAdsException as ex:
        for error in ex.failure.errors:
            print(f"Erro API: {error.message}")
        return

    if not rows:
        print("Nenhuma keyword encontrada.")
        return

    print(f"\n{'='*80}")
    print(f"ANÁLISE DE KEYWORDS — Conta {customer_id} | Últimos {days} dias")
    print(f"{'='*80}\n")

    wasted = []
    low_qs = []
    top = []

    match_map = {"EXACT": "[exata]", "PHRASE": '"frase"', "BROAD": "ampla"}

    for row in rows:
        kw = row.ad_group_criterion.keyword
        qi = row.ad_group_criterion.quality_info
        m = row.metrics
        cost = micros_to_brl(m.cost_micros)
        cpc = micros_to_brl(m.average_cpc)
        qs = qi.quality_score if qi.quality_score > 0 else None
        match = match_map.get(kw.match_type.name, kw.match_type.name)

        entry = {
            "text": kw.text,
            "match": match,
            "qs": qs,
            "cost": cost,
            "clicks": m.clicks,
            "impressions": m.impressions,
            "conversions": m.conversions,
            "cpc": cpc,
            "ctr": m.ctr,
            "campaign": row.campaign.name,
            "ad_group": row.ad_group.name,
        }

        if cost > 50 and m.conversions == 0:
            wasted.append(entry)
        if qs and qs <= 4:
            low_qs.append(entry)
        if m.conversions > 0:
            top.append(entry)

    print(f"{'─'*80}")
    print(f"TOP KEYWORDS (com conversões) — {len(top)} encontradas")
    print(f"{'─'*80}")
    for e in top[:20]:
        cpa = e['cost'] / e['conversions'] if e['conversions'] > 0 else 0
        qs_str = f"QS:{e['qs']}" if e['qs'] else "QS:n/d"
        print(f"  {e['match']} \"{e['text']}\"")
        print(f"    Gasto: R${e['cost']:.2f} | Conv: {e['conversions']:.1f} | CPA: R${cpa:.2f} | {qs_str} | CTR: {e['ctr']*100:.1f}%")
        print(f"    Campanha: {e['campaign']} > {e['ad_group']}")

    if wasted:
        print(f"\n{'─'*80}")
        print(f"⚠ KEYWORDS COM GASTO SEM CONVERSÃO — {len(wasted)} encontradas")
        print(f"{'─'*80}")
        total_wasted = sum(e['cost'] for e in wasted)
        print(f"  Total desperdiçado: R${total_wasted:,.2f}\n")
        for e in sorted(wasted, key=lambda x: x['cost'], reverse=True):
            print(f"  {e['match']} \"{e['text']}\" — R${e['cost']:.2f} | {e['clicks']} cliques | {e['impressions']} impressões")
            print(f"    Campanha: {e['campaign']} > {e['ad_group']}")

    if low_qs:
        print(f"\n{'─'*80}")
        print(f"⚠ KEYWORDS COM QUALITY SCORE BAIXO (≤4) — {len(low_qs)} encontradas")
        print(f"{'─'*80}")
        for e in sorted(low_qs, key=lambda x: x['qs']):
            print(f"  QS:{e['qs']} {e['match']} \"{e['text']}\" — R${e['cost']:.2f} | {e['clicks']} cliques")
            print(f"    Campanha: {e['campaign']} > {e['ad_group']}")

    print(f"\n{'='*80}")
    print(f"Total de keywords analisadas: {len(rows)}")
    print(f"{'='*80}\n")

def get_keyword_ideas(customer_id, keywords, location_id="1001767", language_id="1014"):
    """Get keyword ideas from Keyword Planner. location_id 1001767 = Brazil, language_id 1014 = Portuguese."""
    client = get_client()
    kp_service = client.get_service("KeywordPlanIdeaService")
    ga_service = client.get_service("GoogleAdsService")

    location_rn = f"geoTargetConstants/{location_id}"
    language_rn = ga_service.language_constant_path(language_id)

    request = client.get_type("GenerateKeywordIdeasRequest")
    request.customer_id = customer_id
    request.language = language_rn
    request.geo_target_constants = [location_rn]
    request.include_adult_keywords = False
    request.keyword_plan_network = client.enums.KeywordPlanNetworkEnum.GOOGLE_SEARCH
    request.keyword_seed.keywords.extend(keywords)

    print(f"\n{'='*80}")
    print(f"KEYWORD PLANNER — Ideias para: {', '.join(keywords)}")
    print(f"{'='*80}\n")

    try:
        ideas = kp_service.generate_keyword_ideas(request=request)
        results = []
        for idea in ideas:
            m = idea.keyword_idea_metrics
            avg_searches = m.avg_monthly_searches
            competition = m.competition.name
            low_bid = m.low_top_of_page_bid_micros / 1_000_000 if m.low_top_of_page_bid_micros else 0
            high_bid = m.high_top_of_page_bid_micros / 1_000_000 if m.high_top_of_page_bid_micros else 0
            results.append({
                "text": idea.text,
                "avg_searches": avg_searches,
                "competition": competition,
                "low_bid": low_bid,
                "high_bid": high_bid,
            })

        results.sort(key=lambda x: x['avg_searches'], reverse=True)

        comp_map = {"LOW": "Baixa", "MEDIUM": "Média", "HIGH": "Alta"}
        for r in results[:50]:
            comp = comp_map.get(r['competition'], r['competition'])
            bid_str = f"R${r['low_bid']:.2f}–R${r['high_bid']:.2f}" if r['high_bid'] > 0 else "n/d"
            print(f"  \"{r['text']}\"")
            print(f"    Volume: {r['avg_searches']:,}/mês | Competição: {comp} | CPC estimado: {bid_str}")

    except GoogleAdsException as ex:
        for error in ex.failure.errors:
            print(f"Erro API: {error.message}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--customer-id", required=True)
    parser.add_argument("--campaign-id", help="Filtrar por campanha específica")
    parser.add_argument("--days", type=int, default=30)
    parser.add_argument("--new-ideas", nargs="+", help="Keywords para buscar ideias no Keyword Planner")
    args = parser.parse_args()

    if args.new_ideas:
        get_keyword_ideas(args.customer_id, args.new_ideas)
    else:
        analyze_keywords(args.customer_id, args.campaign_id, args.days)
