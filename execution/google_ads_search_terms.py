"""
Analyze search terms report and identify negative keyword opportunities.
Usage: python3 google_ads_search_terms.py --customer-id CUSTOMER_ID [--days 30] [--min-cost 10]
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

def analyze_search_terms(customer_id, days=30, min_cost=10):
    client = get_client()
    service = client.get_service("GoogleAdsService")

    query = f"""
        SELECT
            search_term_view.search_term,
            search_term_view.status,
            campaign.name,
            campaign.advertising_channel_type,
            ad_group.name,
            metrics.impressions,
            metrics.clicks,
            metrics.cost_micros,
            metrics.conversions,
            metrics.conversions_value,
            metrics.ctr,
            metrics.average_cpc
        FROM search_term_view
        WHERE segments.date DURING LAST_{days}_DAYS
        AND metrics.clicks > 0
        ORDER BY metrics.cost_micros DESC
        LIMIT 500
    """

    try:
        response = service.search(customer_id=customer_id, query=query)
        rows = list(response)
    except GoogleAdsException as ex:
        for error in ex.failure.errors:
            print(f"Erro API: {error.message}")
        return

    if not rows:
        print("Nenhum termo de pesquisa encontrado.")
        return

    print(f"\n{'='*80}")
    print(f"TERMOS DE PESQUISA — Conta {customer_id} | Últimos {days} dias")
    print(f"{'='*80}\n")

    total_cost = 0
    wasted_cost = 0
    negative_candidates = []
    converters = []
    all_terms = []

    for row in rows:
        st = row.search_term_view
        m = row.metrics
        cost = micros_to_brl(m.cost_micros)
        cpc = micros_to_brl(m.average_cpc)
        cpa = (cost / m.conversions) if m.conversions > 0 else 0

        entry = {
            "term": st.search_term,
            "status": st.status.name,
            "campaign": row.campaign.name,
            "channel": row.campaign.advertising_channel_type.name,
            "ad_group": row.ad_group.name,
            "cost": cost,
            "clicks": m.clicks,
            "impressions": m.impressions,
            "conversions": m.conversions,
            "conv_value": m.conversion_value,
            "ctr": m.ctr,
            "cpc": cpc,
            "cpa": cpa,
        }

        total_cost += cost
        all_terms.append(entry)

        if m.conversions == 0 and cost >= min_cost:
            wasted_cost += cost
            negative_candidates.append(entry)

        if m.conversions > 0:
            converters.append(entry)

    print(f"Total de termos analisados: {len(rows)}")
    print(f"Total gasto: R${total_cost:,.2f}")
    print(f"Gasto sem conversão (≥R${min_cost}): R${wasted_cost:,.2f} ({wasted_cost/total_cost*100:.1f}% do total)\n")

    if converters:
        print(f"{'─'*80}")
        print(f"✓ TERMOS QUE CONVERTEM — {len(converters)} termos")
        print(f"{'─'*80}")
        for e in sorted(converters, key=lambda x: x['conversions'], reverse=True)[:20]:
            roas = (e['conv_value'] / e['cost']) if e['cost'] > 0 else 0
            print(f"  \"{e['term']}\"")
            print(f"    Custo: R${e['cost']:.2f} | Conv: {e['conversions']:.1f} | CPA: R${e['cpa']:.2f} | ROAS: {roas:.2f}x")
            print(f"    Campanha: {e['campaign']} > {e['ad_group']}")

    if negative_candidates:
        print(f"\n{'─'*80}")
        print(f"⚠ CANDIDATOS A NEGATIVAS — {len(negative_candidates)} termos | R${wasted_cost:,.2f} desperdiçados")
        print(f"{'─'*80}")
        print("Estes termos tiveram gasto significativo mas ZERO conversões:\n")
        for e in sorted(negative_candidates, key=lambda x: x['cost'], reverse=True):
            print(f"  \"{e['term']}\" — R${e['cost']:.2f} | {e['clicks']} cliques | CTR: {e['ctr']*100:.1f}%")
            print(f"    [{e['channel']}] {e['campaign']} > {e['ad_group']}")

        print(f"\n{'─'*80}")
        print("LISTA DE NEGATIVAS SUGERIDAS (copie e adicione na conta):")
        print(f"{'─'*80}")
        for e in sorted(negative_candidates, key=lambda x: x['cost'], reverse=True):
            print(f"  {e['term']}")

    print(f"\n{'='*80}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--customer-id", required=True)
    parser.add_argument("--days", type=int, default=30)
    parser.add_argument("--min-cost", type=float, default=10, help="Custo mínimo para considerar candidato a negativa (padrão: R$10)")
    args = parser.parse_args()
    analyze_search_terms(args.customer_id, args.days, args.min_cost)
