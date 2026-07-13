# Relatório Meta Ads - Onvoix
**Período atual:** 06/07/2026 a 12/07/2026
**Período anterior:** 29/06/2026 a 05/07/2026
**Gerado em:** 13/07/2026 | **Conta:** act_1297650828540575

---

## Resumo Executivo

| Métrica | Atual | Anterior | Variação |
|---|---|---|---|
| Gasto | $44,91 | $88,25 | -49,1% 🔴 |
| Leads | 80 | 243 | -67,1% 🔴 |
| CPL | $0,56 | $0,36 | +55,6% 🔴 |
| CPM médio | $8,16 | $30,33 | -73,1% 🟢 |
| CTR médio | 22,16% | 37,43% | -40,8% 🔴 |
| Frequência média | 1,18 | 1,19 | -0,8% 🟢 |
| Campanhas ativas | 1 | 2 | -1 🔴 |

> ⚠️ **Contexto crítico:** A campanha "Site - México" — responsável por 140 leads ao CPL de $0,26 na semana anterior — não está ativa neste período. Isso explica a queda abrupta em volume e o aumento de CPL. O desempenho da campanha remanescente (Site - México — Registro) é estável ou levemente melhor que na semana anterior ($0,56 vs $0,51), portanto o problema não é qualidade — é ausência de volume.

---

## Módulo 1 — Auditoria de Campanhas e Anúncios

### Campanhas

| Campanha | Status | Gasto | Leads | CPL | CTR | CPM | Freq |
|---|---|---|---|---|---|---|---|
| Site - México — Registro | 🟢 OK | $44,91 | 80 | $0,56 | 22,16% | $8,16 | 1,18 |
| Site - México | 🔴 INATIVA | — | — | — | — | — | — |

> 🔴 **CRÍTICO:** A campanha "Site - México" gerou 140 leads ao CPL de $0,26 na semana passada e aparentemente foi pausada ou encerrou o budget. Sua ausência é a principal causa da queda de volume e elevação do CPL médio da conta.

---

### Anúncios por Campanha

**Campanha: Site - México — Registro** *(ordenados por CPL)*

| Anúncio | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| Ima 04 — Cópia | $3,56 | 9 | $0,40 | 11,35% | $9,62 | 1,58 | 🟢 OK |
| VID 01 — Cópia | $34,81 | 69 | $0,50 | 24,18% | $7,49 | 1,16 | 🟢 OK |
| Ima 02 — Cópia | $0,20 | 1 | $0,20 | 42,86% | $28,57 | 1,00 | ⚪ Dados insuficientes |
| Ima 03 — Cópia | $0,41 | 1 | $0,41 | 21,43% | $29,29 | 1,17 | ⚪ Dados insuficientes |
| Ima 06 — Cópia | $5,88 | 0 | — | 10,48% | $12,84 | 1,15 | 🔴 CRÍTICO |
| Ima 01 — Cópia | $0,05 | 0 | — | 0,00% | $6,25 | 1,00 | ⚪ Gasto mínimo |

> 🔴 **CRÍTICO — Ima 06 — Cópia:** $5,88 gastos, 0 leads, CTR de apenas 10,48%. Excede o threshold de $15 para 0 leads ainda não foi atingido, mas a tendência é preocupante. Recomenda-se monitoramento com limite claro de pausa em $10 sem conversões.

---

## Módulo 2 — Diagnóstico de CPL (Causa Raiz)

### Campanha: Site - México — Registro

**CPL atual: $0,56 | Semana anterior: $0,51 | Variação: +9,8%**

| Fator | Semana Anterior | Atual | Diagnóstico |
|---|---|---|---|
| CPM | $17,93 | $8,16 | ✅ Melhorou significativamente (-54,5%) |
| CTR | 26,05% | 22,16% | ⚠️ Leve queda (-14,9%) |
| Frequência | 1,24 | 1,18 | ✅ Sem fadiga |
| Leads | 103 | 80 | 🔴 Queda de volume |

**Causa raiz:** O CPL da campanha "Site - México — Registro" piorou moderadamente (+9,8%), o que é aceitável e não representa falha estrutural. O CPM caiu expressivamente ($17,93 → $8,16), o que é positivo, mas o CTR também recuou (26,05% → 22,16%), absorvendo parte do ganho de eficiência no custo de entrega. Em resumo: a campanha está saudável, mas o budget está concentrado em um único criativo (VID 01 — Cópia com 77% do gasto) e os criativos de imagem alternativos ainda não estão recebendo verba suficiente para validar.

**Causa raiz do deterioro geral da conta:** 100% relacionada ao encerramento da campanha "Site - México" que operava com CPL $0,26 — o melhor da conta. Sem ela, a média sobe inevitavelmente.

---

## Módulo 3 — Detecção de Anomalias

| Tipo | Anúncio | Detalhe | Ação Recomendada |
|---|---|---|---|
| 🔴 Campanha encerrada | Site - México | Gerava 140 leads/semana ao CPL $0,26 — desapareceu completamente do período atual | Investigar causa (budget esgotado? pausada manualmente?) e reativar |
| 🔴 Sem conversão com gasto relevante | Ima 06 — Cópia | $5,88 gastos, 0 leads, CTR 10,48% — padrão consistente (também 0 leads na semana anterior com $0,98) | Pausar imediatamente; nenhuma conversão em 2 semanas seguidas |
| ⚠️ CPM anômalo alto em criativos com baixo gasto | Ima 02 — Cópia | CPM $28,57 com apenas $0,20 de gasto — sem significância | Aguardar mais dados antes de qualquer decisão |
| ⚠️ CPM anômalo alto em criativos com baixo gasto | Ima 03 — Cópia | CPM $29,29 com apenas $0,41 de gasto — sem significância | Aguardar mais dados antes de qualquer decisão |
| ⚠️ Concentração de budget | VID 01 — Cópia | 77,5% do gasto total concentrado em 1 criativo — risco se saturar | Validar criativos alternativos aumentando budget progressivamente |

---

## Módulo 4 — Pacing Monitor

| Métrica | Valor |
|---|---|
| Dia do mês | 13 de 31 |
| % do mês decorrido | 41,9% |
| Gasto acumulado (estimado) | ~$44,91 (semana) |
| Projeção mensal | $192,47 |
| Budget mensal | $500,00 |
| Diferença | -$307,53 (-61,5%) |
| Status | 🔴 MUITO LENTO |

**Diagnóstico:** Com 41,9% do mês decorrido, a projeção de gasto mensal é de apenas $192,47 — 38,5% do budget de $500. O ritmo é criticamente baixo. A causa direta é o encerramento da campanha "Site - México" que, sozinha, gastava ~$5/dia ao CPL mais eficiente da conta. Sem reativação ou aumento de budget da campanha ativa, julho encerrará com ~$308 não investidos e aproximadamente 340 leads abaixo do potencial da conta.

---

## Módulo 5 — Fadiga de Criativos

| Anúncio | Frequência | CTR | Leads | Status | Recomendação |
|---|---|---|---|---|---|
| VID 01 — Cópia | 1,16 | 24,18% | 69 | ✅ OK | Manter — sem fadiga |
| Ima 04 — Cópia | 1,58 | 11,35% | 9 | ✅ OK — Monitorar | Acompanhar frequência semanalmente |
| Ima 06 — Cópia | 1,15 | 10,48% | 0 | 🔴 CRÍTICO (0 leads) | Pausar — não é fadiga mas ineficiência estrutural |
| Ima 03 — Cópia | 1,17 | 21,43% | 1 | ⚪ Dados insuficientes | Aguardar mais entrega |
| Ima 02 — Cópia | 1,00 | 42,86% | 1 | ⚪ Dados insuficientes | Aguardar mais entrega |
| Ima 01 — Cópia | 1,00 | 0,00% | 0 | ⚪ Gasto mínimo | Sem dados suficientes |

> ✅ **Conclusão geral:** Nenhum criativo apresenta fadiga de audiência. Frequências abaixo de 1,6 em todos os casos. O risco de fadiga não é o problema desta semana — o problema é volume e ineficiência de criativos específicos (Ima 06).

---

## Módulo 6 — Análise de Copy e Criativos

### 🏆 Criativo Vencedor

**VID 01 — Cópia** (Campanha: Site - México — Registro)
- CPL: $0,50 | Leads: 69 | Gasto: $34,81 | CTR: 24,18% | CPM: $7,49
- ✅ Atende critério mínimo de 5 leads (69 leads)
- Formato: Vídeo
- **Diagnóstico:** Criativo dominante da conta. CPM baixo ($7,49) indica boa relevância junto ao público mexicano. CTR sólido de 24,18%. Estável em relação à semana anterior (CPL $0,50 vs $0,50 — exatamente igual). É o sustentáculo da entrega atual.

### 🥈 Candidato a Escalar (com cautela)

**Ima 04 — Cópia** (Campanha: Site - México — Registro)
- CPL: $0,40 | Leads: 9 | Gasto: $3,56 | CTR: 11,35% | CPM: $9,62
- ✅ Atende critério mínimo de 5 leads (9 leads)
- Formato: Imagem
- **Diagnóstico:** CPL $0,40 é melhor que o vencedor principal ($0,50) com volume suficiente para consideração. Frequência 1,58 ainda saudável. Recomenda-se aumentar gradualmente o budget alocado a este criativo para validar se o CPL se mantém com maior volume. *Nota: amostra ainda pequena — escalar com cautela e monitorar CPL na escala.*

### ❌ Criativos para Pausar

| Anúncio | Motivo |
|---|---|
| **Ima 06 — Cópia** | 🔴 $5,88 gastos, 0 leads em 2 semanas consecutivas. CTR de 10,48% não converte. Anomalia confirmada no Módulo 3. |

### ⚪ Dados Insuficientes (aguardar)

- **Ima 02 — Cópia** — $0,20 gasto, 1 lead. CTR de 42,86% é promissor mas sem significância estatística.
- **Ima 03 — Cópia** — $0,41 gasto, 1 lead. Aguardar mais entrega.
- **Ima 01 — Cópia** — $0,05 gasto, 0 leads. Praticamente sem entrega.

---

## Módulo 7 — Análise de Ad Sets e Públicos

### Ad Sets Ativos

| Ad Set | Campanha | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|---|
| México amplo | Site - México — Registro | $44,91 | 80 | $0,56 | 22,16% | $8,16 | 1,18 | 🟢 OK |

**Observações:**

- **CPM eficiente:** $8,16 representa uma melhora expressiva em relação à semana anterior ($17,93 na mesma campanha). O público "México amplo" está com boa entrega e custo reduzido.
- **Sem risco de sobreposição:** Apenas 1 ad set ativo no momento. Sobreposição de audiência não é uma preocupação atual.
- **Espaço para escala:** Com frequência de 1,18 e CPM baixo, há espaço para aumentar o budget diário sem risco de saturação imediata. O público amplo ainda tem capacidade de absorver mais investimento.
- **Dependência única:** A conta opera inteiramente sobre um único ad set. Qualquer instabilidade nesse conjunto impacta 100% da entrega — recomenda-se criar um segundo ad set como contingência (ex: interesse específico ou Lookalike de leads).

---

## Plano de Ação

| Prioridade | Ação | Impacto | Prazo |
|---|---|---|---|
| 🔴 P1 | **Investigar e reativar "Site - México"** — verificar se foi pausada manualmente ou atingiu budget. Era responsável por 140 leads/semana ao CPL $0,26 (melhor da conta) | Alto — recuperação de 140+ leads/semana e redução do CPL médio para ~$0,36 | Hoje |
| 🔴 P2 | **Pausar Ima 06 — Cópia** — $5,88 gastos com 0 leads em 2 semanas consecutivas. Anomalia confirmada | Médio — elimina desperdício de ~$5-6/semana | Hoje |
| 🟡 P3 | **Aumentar budget de Ima 04 — Cópia** — CPL $0,40 com 9 leads. Elevar de forma gradual (ex: dobrar budget alocado) para validar se o CPL se sustenta em escala | Médio — potencial de tornar-se