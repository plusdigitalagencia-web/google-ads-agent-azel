"""
Wrapper do weekly_report_generator.py exclusivo para clientes Google Ads da Duosfera.
Gera o relatorio padrao (sem alterar o script compartilhado) e acrescenta um
bloco "RESUMO FINAL PARA TRELLO" por campanha, no mesmo espirito do bloco que
ja existe nos relatorios de Meta Ads (ex: dra_fernanda_meta_report.py).

Usage: igual ao weekly_report_generator.py
  python3 weekly_report_generator_duosfera.py --customer-id ID --mcc-id ID \
    --output FILE.md --client-name NOME --currency BRL \
    [--start-date YYYY-MM-DD --end-date YYYY-MM-DD]
"""
import os
import sys
import argparse
from datetime import date, timedelta, datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from weekly_report_generator import (
    get_client, micros, format_currency, safe_pct, pct_change, date_range,
    fetch_campaign_metrics, fetch_keywords, fetch_keyword_quality_scores,
    fetch_search_terms, aggregate_campaigns, build_qs_map, generate_report,
)

MIN_CLICKS_VENCEDORA = 5
MIN_CONVERSOES_VENCEDORA = 2
QS_BAIXO = 4
IMPR_SHARE_PERDA_ALTA = 0.30


def keywords_for_campaign(kw_rows, campaign_name):
    return [r for r in kw_rows if r.campaign.name == campaign_name]


def waste_terms_for_campaign(search_rows, campaign_name):
    return [
        r for r in search_rows
        if r.campaign.name == campaign_name
        and micros(r.metrics.cost_micros) > 0
        and r.metrics.conversions == 0
        and r.metrics.clicks >= 3
    ]


def best_keyword(camp_kw_rows):
    candidates = [r for r in camp_kw_rows if r.metrics.conversions > 0]
    if not candidates:
        return None
    with_volume = [
        r for r in candidates
        if r.metrics.clicks >= MIN_CLICKS_VENCEDORA or r.metrics.conversions >= MIN_CONVERSOES_VENCEDORA
    ]
    pool = with_volume if with_volume else candidates
    return min(pool, key=lambda r: micros(r.metrics.cost_micros) / r.metrics.conversions)


def low_qs_keywords(camp_kw_rows, qs_map):
    out = []
    for r in camp_kw_rows:
        info = qs_map.get(r.ad_group_criterion.keyword.text.lower().strip(), {})
        qs = info.get("qs")
        if qs is not None and qs < QS_BAIXO and micros(r.metrics.cost_micros) >= 5:
            out.append((r, qs))
    return sorted(out, key=lambda x: micros(x[0].metrics.cost_micros), reverse=True)


def build_resumo_final(client_name, generated_at, campaigns, cur_totals, prev_totals,
                        kw_rows, qs_map, search_rows, currency):
    def fmt(v):
        return format_currency(v, currency)

    lines = ["", "---", "", "## RESUMO FINAL PARA TRELLO", ""]
    lines.append(f"Google Ads {client_name} - {generated_at}")
    lines.append(
        f"Gasto: {fmt(cur_totals['cost'])} | Conversoes: {cur_totals['conversions']:.1f} | "
        f"CPA: {fmt(cur_totals['cpa'])} "
        f"({pct_change(cur_totals['cpa'], prev_totals['cpa']) or '--'} vs periodo anterior)"
    )
    lines.append("")

    if not campaigns:
        lines.append("_Nenhuma campanha com dados no periodo._")
        return "\n".join(lines)

    for camp in campaigns:
        cname = camp["name"]
        camp_kws = keywords_for_campaign(kw_rows, cname)
        waste = waste_terms_for_campaign(search_rows, cname)
        low_qs = low_qs_keywords(camp_kws, qs_map)
        best = best_keyword(camp_kws)
        best_cpa = (micros(best.metrics.cost_micros) / best.metrics.conversions) if best else 0

        perde_rank = camp["is_search"] and camp["lost_rank"] and camp["lost_rank"] > IMPR_SHARE_PERDA_ALTA
        perde_budget = camp["is_search"] and camp["lost_budget"] and camp["lost_budget"] > IMPR_SHARE_PERDA_ALTA

        lines += ["---", "", f"CAMPANHA: {cname}", ""]

        lines.append("O QUE ESTA FUNCIONANDO:")
        if best:
            lines.append(
                f"- Palavra-chave \"{best.ad_group_criterion.keyword.text}\" - "
                f"CTR {best.metrics.ctr * 100:.2f}% | CPA {fmt(best_cpa)} "
                f"({best.metrics.conversions:.1f} conversoes)"
            )
        else:
            lines.append(f"- {camp['conversions']:.1f} conversoes geradas no periodo")
        if camp["is_search"] and not perde_rank and not perde_budget and camp.get("impr_share"):
            lines.append(f"- Impression Share em {safe_pct(camp['impr_share'])}, sem grande perda por rank/orcamento")
        lines.append("")

        lines.append("O QUE NAO ESTA FUNCIONANDO:")
        problemas = False
        if waste:
            for w in waste[:2]:
                lines.append(
                    f"- Termo \"{w.search_term_view.search_term}\" - "
                    f"{fmt(micros(w.metrics.cost_micros))} gastos sem conversao"
                )
            problemas = True
        if low_qs:
            for r, qs in low_qs[:2]:
                lines.append(
                    f"- Palavra-chave \"{r.ad_group_criterion.keyword.text}\" com Quality Score baixo (QS {qs})"
                )
            problemas = True
        if perde_rank:
            lines.append(f"- {safe_pct(camp['lost_rank'])} de impressoes perdidas por rank (lance/anuncio mal posicionado)")
            problemas = True
        if perde_budget:
            lines.append(f"- {safe_pct(camp['lost_budget'])} de impressoes perdidas por orcamento")
            problemas = True
        if not problemas:
            lines.append("- Sem problemas criticos identificados")
        lines.append("")

        lines.append("PALAVRA-CHAVE VENCEDORA:")
        if best:
            lines.append(f"- {best.ad_group_criterion.keyword.text} - CTR {best.metrics.ctr * 100:.2f}% | CPA {fmt(best_cpa)}")
        else:
            lines.append("- A definir (sem palavra-chave com volume relevante convertendo no periodo)")
        lines.append("")

        lines.append("O QUE PRECISA SER FEITO:")
        acoes = []
        if waste:
            acoes.append("Negativar os termos de desperdicio listados acima")
        if low_qs:
            acoes.append("Revisar anuncio/pagina de destino das palavras-chave com QS baixo")
        if perde_rank:
            acoes.append("Aumentar lance ou melhorar Quality Score para reduzir a perda por rank")
        if perde_budget:
            acoes.append("Aumentar orcamento diario - ha demanda sendo perdida por falta de verba")
        if best:
            acoes.append("Escalar a palavra-chave vencedora (aumentar lance/orcamento)")
        if not acoes:
            acoes.append("Monitorar - sem acoes criticas identificadas")
        for a in acoes:
            lines.append(f"- {a}")
        lines.append("")

    return "\n".join(lines)


def generate_report_duosfera(customer_id, mcc_id, client_name, currency, start_date=None, end_date=None):
    base_report = generate_report(customer_id, mcc_id, client_name, currency, start_date, end_date)

    client = get_client(mcc_id)
    service = client.get_service("GoogleAdsService")

    if start_date and end_date:
        cur_start = datetime.strptime(start_date, "%Y-%m-%d").date()
        cur_end = datetime.strptime(end_date, "%Y-%m-%d").date()
        period_days = (cur_end - cur_start).days + 1
        prev_end = cur_start - timedelta(days=1)
        prev_start = prev_end - timedelta(days=period_days - 1)
    else:
        cur_start, cur_end = date_range(7, 1)
        prev_start, prev_end = date_range(14, 8)

    cur_rows = fetch_campaign_metrics(service, customer_id, cur_start, cur_end)
    prev_rows = fetch_campaign_metrics(service, customer_id, prev_start, prev_end)
    kw_rows = fetch_keywords(service, customer_id, cur_start, cur_end)
    qs_rows = fetch_keyword_quality_scores(service, customer_id)
    search_rows = fetch_search_terms(service, customer_id, cur_start, cur_end)

    campaigns, cur_totals = aggregate_campaigns(cur_rows)
    _, prev_totals = aggregate_campaigns(prev_rows)
    qs_map = build_qs_map(qs_rows)

    generated_at = date.today().strftime("%d/%m/%Y")
    resumo = build_resumo_final(
        client_name, generated_at, campaigns, cur_totals, prev_totals, kw_rows, qs_map, search_rows, currency
    )

    return base_report + "\n" + resumo


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--customer-id", required=True)
    parser.add_argument("--mcc-id", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--client-name", default="Cliente Duosfera")
    parser.add_argument("--currency", default="BRL", choices=["BRL", "COP", "EUR", "USD"])
    parser.add_argument("--start-date", default=None, help="Data inicial YYYY-MM-DD (opcional)")
    parser.add_argument("--end-date", default=None, help="Data final YYYY-MM-DD (opcional)")
    args = parser.parse_args()

    report = generate_report_duosfera(
        args.customer_id, args.mcc_id, args.client_name, args.currency, args.start_date, args.end_date
    )

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"Relatorio salvo em: {args.output}")
