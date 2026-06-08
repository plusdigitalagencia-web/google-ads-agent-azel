import os, json, urllib.request, urllib.parse
from datetime import datetime, timezone, timedelta

TOKEN = os.environ["META_ACCESS_TOKEN"]
APP_ID = os.environ["META_APP_ID"]
APP_SECRET = os.environ["META_APP_SECRET"]

ACCOUNTS = [
    {"id": "act_1057721942577752", "name": "Leão XIII"},
    {"id": "act_1888156658506198", "name": "Conta 2"},
]

BASE = "https://graph.facebook.com/v25.0"
BRT = timezone(timedelta(hours=-3))
now = datetime.now(BRT)
today = now.date()

# --- Token ---
def refresh_token(tok):
    url = (f"{BASE}/oauth/access_token?grant_type=fb_exchange_token"
           f"&client_id={APP_ID}&client_secret={APP_SECRET}&fb_exchange_token={tok}")
    try:
        return json.loads(urllib.request.urlopen(url, timeout=15).read()).get("access_token", tok)
    except Exception as e:
        print(f"[WARN] Token refresh falhou: {e}")
        return tok

# --- API ---
def api(url):
    try:
        return json.loads(urllib.request.urlopen(url, timeout=30).read())
    except Exception as e:
        print(f"[API ERROR] {e}")
        return {}

def fetch_insights(token, account_id, time_range, level="campaign"):
    fields = ("campaign_name,adset_name,ad_name,spend,clicks,impressions,"
              "reach,cpm,ctr,frequency,actions,cost_per_action_type")
    params = urllib.parse.urlencode({
        "fields": fields,
        "level": level,
        "time_range": json.dumps(time_range),
        "action_breakdowns": "action_type",
        "access_token": token,
        "limit": 500,
    })
    url = f"{BASE}/{account_id}/insights?{params}"
    data = api(url)
    rows = data.get("data", [])
    while data.get("paging", {}).get("next"):
        data = api(data["paging"]["next"])
        rows.extend(data.get("data", []))
    return rows

# --- Helpers ---
def val(lst, key):
    for x in (lst or []):
        if x.get("action_type") == key:
            return float(x.get("value", 0))
    return 0.0

def cpr_label(cpr):
    if cpr <= 0:   return "⚪ Sem dados"
    if cpr < 3.0:  return "🟢 Ideal"
    if cpr <= 5.5: return "🟡 Atenção"
    return "🔴 Crítico"

def ctr_label(ctr):
    if ctr >= 2.5: return "🟢"
    if ctr >= 1.5: return "🟡"
    if ctr >= 0.8: return "⚠️"
    return "🔴"

def cpm_label(cpm):
    if cpm <= 0:   return "⚪"
    if cpm < 6.0:  return "🟢"
    if cpm <= 9.0: return "🟡"
    return "🔴"

def freq_label(freq):
    if freq <= 0:   return "—"
    if freq < 2.0:  return "🟢"
    if freq <= 3.5: return "🟡"
    return "🔴 Fadiga"

def pct(a, b):
    if not b:
        return "—"
    v = ((a - b) / b) * 100
    return f"{'+'if v >= 0 else ''}{v:.0f}%"

def parse(rows):
    out = []
    for d in rows:
        sp = float(d.get("spend") or 0)
        ac = d.get("actions") or []
        conv = val(ac, "onsite_conversion.messaging_conversation_started_7d")
        cpr = sp / conv if conv > 0 else 0.0
        out.append({
            "name":   (d.get("campaign_name") or d.get("adset_name") or d.get("ad_name") or "—")[:60],
            "spend":  sp,
            "conv":   conv,
            "cpr":    cpr,
            "cpm":    float(d.get("cpm") or 0),
            "ctr":    float(d.get("ctr") or 0),
            "freq":   float(d.get("frequency") or 0),
            "imp":    int(d.get("impressions") or 0),
            "clicks": int(d.get("clicks") or 0),
            "reach":  int(d.get("reach") or 0),
        })
    return out

# --- Períodos ---
cur = {
    "since": str(today - timedelta(days=7)),
    "until": str(today - timedelta(days=1)),
}
prv = {
    "since": str(today - timedelta(days=14)),
    "until": str(today - timedelta(days=8)),
}

token = refresh_token(TOKEN)

# ==================================================
# GERAR SEÇÃO POR CONTA
# ==================================================
all_sections = []

for acc in ACCOUNTS:
    aid   = acc["id"]
    aname = acc["name"]

    camp_cur = parse(fetch_insights(token, aid, cur, "campaign"))
    camp_prv = parse(fetch_insights(token, aid, prv, "campaign"))
    ads_cur  = parse(fetch_insights(token, aid, cur, "ad"))

    prv_map = {r["name"]: r for r in camp_prv}

    # Totais período atual
    ts    = sum(r["spend"] for r in camp_cur)
    tc    = sum(r["conv"]  for r in camp_cur)
    cpr_g = ts / tc if tc > 0 else 0.0

    # Totais período anterior
    ts_p    = sum(r["spend"] for r in camp_prv)
    tc_p    = sum(r["conv"]  for r in camp_prv)
    cpr_gp  = ts_p / tc_p if tc_p > 0 else 0.0

    critical = [r for r in camp_cur if r["cpr"] > 5.5 and r["conv"] > 0]
    winners  = [r for r in camp_cur if r["cpr"] < 3.0 and r["conv"] >= 30]
    fatigued = [r for r in camp_cur if r["freq"] > 3.5]

    # --- Resumo Executivo ---
    best = min(camp_cur, key=lambda r: r["cpr"]) if [c for c in camp_cur if c["conv"] > 0] else None
    exec_lines = [
        f"- Investimento 7 dias: **R${ts:.2f}** ({pct(ts, ts_p)} vs semana anterior)",
        f"- Conversas WhatsApp: **{int(tc)}** ({pct(tc, tc_p)} vs semana anterior)",
        f"- CPR geral: **R${cpr_g:.2f}** → {cpr_label(cpr_g)} ({pct(cpr_g, cpr_gp)} vs semana anterior)",
    ]
    if best and best["conv"] > 0:
        exec_lines.append(f"- Melhor campanha: **{best['name']}** — CPR R${best['cpr']:.2f} {cpr_label(best['cpr'])}")
    if critical:
        names = ", ".join(r["name"][:35] for r in critical[:3])
        exec_lines.append(f"- ⚠️ **{len(critical)} campanha(s) com CPR crítico** (>R$5,50): {names}")
    if winners:
        names = ", ".join(r["name"][:35] for r in winners[:2])
        exec_lines.append(f"- 🚀 **{len(winners)} campanha(s) vencedora(s)** para escalar: {names}")
    if fatigued:
        names = ", ".join(r["name"][:35] for r in fatigued[:2])
        exec_lines.append(f"- 💀 **{len(fatigued)} campanha(s) com fadiga** (frequência >3,5): {names}")

    # --- Tabela campanhas ---
    camp_rows = sorted(camp_cur, key=lambda x: -x["spend"])
    camp_tbl = (
        "| Campanha | Gasto | Conversas | CPR | Var CPR | CTR | CPM | Freq | Status |\n"
        "|---|---|---|---|---|---|---|---|---|\n"
    )
    for r in camp_rows:
        p = prv_map.get(r["name"], {})
        camp_tbl += (
            f"| {r['name']} "
            f"| R${r['spend']:.2f} "
            f"| {int(r['conv'])} "
            f"| R${r['cpr']:.2f} "
            f"| {pct(r['cpr'], p.get('cpr', 0))} "
            f"| {r['ctr']:.2f}% {ctr_label(r['ctr'])} "
            f"| R${r['cpm']:.2f} {cpm_label(r['cpm'])} "
            f"| {r['freq']:.1f} {freq_label(r['freq'])} "
            f"| {cpr_label(r['cpr'])} |\n"
        )
    camp_tbl += (
        f"| **TOTAL** | **R${ts:.2f}** | **{int(tc)}** | **R${cpr_g:.2f}** "
        f"| {pct(cpr_g, cpr_gp)} | — | — | — | {cpr_label(cpr_g)} |\n"
    )

    # --- Ranking criativos Top 5 ---
    ads_with_conv = [a for a in ads_cur if a["conv"] > 0]
    top5 = sorted(ads_with_conv, key=lambda x: x["cpr"])[:5]
    if top5:
        top_tbl = (
            "| # | Anúncio | Conversas | CPR | CTR | CPM | Freq | Status |\n"
            "|---|---|---|---|---|---|---|---|\n"
        )
        for i, a in enumerate(top5, 1):
            top_tbl += (
                f"| {i} | {a['name']} | {int(a['conv'])} "
                f"| R${a['cpr']:.2f} | {a['ctr']:.2f}% "
                f"| R${a['cpm']:.2f} | {a['freq']:.1f} "
                f"| {cpr_label(a['cpr'])} |\n"
            )
    else:
        top_tbl = "_Sem criativos com conversas no período._\n"

    # --- Criativos críticos Bottom 3 ---
    bottom3 = sorted([a for a in ads_cur if a["cpr"] > 5.5 and a["conv"] > 0], key=lambda x: -x["cpr"])[:3]
    if bottom3:
        bot_tbl = (
            "| # | Anúncio | Conversas | CPR | Freq | Diagnóstico |\n"
            "|---|---|---|---|---|---|\n"
        )
        for i, a in enumerate(bottom3, 1):
            diag = []
            if a["freq"] > 3.5:  diag.append("frequência alta → fadiga")
            if a["ctr"] < 0.8:   diag.append("CTR crítico → hook fraco")
            if a["cpm"] > 9:     diag.append("CPM caro → leilão ruim")
            if not diag:         diag.append("investigar causa raiz")
            bot_tbl += (
                f"| {i} | {a['name']} | {int(a['conv'])} "
                f"| R${a['cpr']:.2f} | {a['freq']:.1f} "
                f"| {'; '.join(diag)} |\n"
            )
    else:
        bot_tbl = "_Nenhum criativo com CPR crítico no período._\n"

    # --- Diagnóstico CPR crítico ---
    crit_lines = []
    for r in critical:
        p = prv_map.get(r["name"], {})
        lines = [f"\n**{r['name']}** — CPR R${r['cpr']:.2f} ({pct(r['cpr'], p.get('cpr', 0))} vs semana anterior)"]
        if r["freq"] > 3.5:
            lines.append(f"  - Frequência {r['freq']:.1f} → público saturado, mesmo criativo reexibido demais")
        if r["ctr"] < 0.8:
            lines.append(f"  - CTR {r['ctr']:.2f}% → hook do criativo sem força, trocar ângulo")
        if r["cpm"] > 9:
            lines.append(f"  - CPM R${r['cpm']:.2f} → leilão caro, testar novo público ou criativo")
        if r["ctr"] >= 0.8 and r["cpm"] <= 9 and r["freq"] <= 3.5:
            lines.append("  - Métricas intermediárias normais → possível problema no link WhatsApp ou mensagem inicial")
        crit_lines.append("\n".join(lines))
    crit_diag = "\n".join(crit_lines) if crit_lines else "_Nenhuma campanha com CPR crítico no período._"

    # --- Plano de Ação ---
    actions = []
    for r in sorted(critical, key=lambda x: -x["cpr"])[:2]:
        actions.append(
            f"| 🔴 Alta | Diagnosticar **{r['name'][:40]}** (CPR R${r['cpr']:.2f}) "
            f"| Cortar gasto ou criar criativo novo com ângulo diferente | Hoje |"
        )
    for r in winners[:2]:
        actions.append(
            f"| 🟢 Alta | Escalar **{r['name'][:40]}** (CPR R${r['cpr']:.2f}) "
            f"| Aumentar budget 20–30% — campanha vencedora | Hoje |"
        )
    for r in fatigued[:2]:
        actions.append(
            f"| 🟡 Média | Inserir criativo novo em **{r['name'][:40]}** (freq {r['freq']:.1f}) "
            f"| Aliviar fadiga — manter ângulo mas renovar visual | 2 dias |"
        )
    if not actions:
        actions.append("| ⚪ — | Conta estável, sem ações urgentes | Monitorar tendências | — |")

    act_tbl = (
        "| Prioridade | Ação | Impacto Esperado | Prazo |\n"
        "|---|---|---|---|\n"
        + "\n".join(actions) + "\n"
    )

    section = f"""
---

# Conta: {aname} (`{aid}`)

## Resumo Executivo

{chr(10).join(exec_lines)}

---

## Performance por Campanha — {cur['since']} a {cur['until']} vs Semana Anterior

{camp_tbl}
> **Benchmark Shineray MA:** CTR ideal >2,5% | CPM eficiente <R$6,00 | CPR ideal <R$3,00 | Frequência saudável <2,0

---

## Ranking de Criativos — Top 5 Vencedores

{top_tbl}
> Criativos com menos de 30 conversas ainda em aprendizado — não pausar.

---

## Criativos Críticos (CPR > R$5,50)

{bot_tbl}

---

## Diagnóstico — Campanhas com CPR Crítico

{crit_diag}

---

## Plano de Ação

{act_tbl}"""
    all_sections.append(section)

# ==================================================
# MONTAR RELATÓRIO FINAL
# ==================================================
report_date_str = now.strftime("%d/%m/%Y %H:%M")
report = f"""# Relatório Meta Ads WhatsApp — Shineray Maranhão
📅 **{report_date_str} (BRT)** | Período: {cur['since']} a {cur['until']} | Plus Digital Agência

{''.join(all_sections)}

---
*Gerado automaticamente via Graph API Meta v25.0*
*Filosofia Andromeda: CPR ideal <R$3,00 | atenção R$3,00–R$5,50 | crítico >R$5,50*
"""

# Salvar
report_filename = f"reports/shineray/meta-report-{today}.md"
os.makedirs("reports/shineray", exist_ok=True)
with open(report_filename, "w", encoding="utf-8") as f:
    f.write(report)

print(f"[OK] Relatório salvo: {report_filename}")
print(f"[OK] Gasto total: R${sum(r['spend'] for acc_section in [parse(fetch_insights(token, acc['id'], cur, 'campaign')) for acc in ACCOUNTS] for r in acc_section):.2f}")
