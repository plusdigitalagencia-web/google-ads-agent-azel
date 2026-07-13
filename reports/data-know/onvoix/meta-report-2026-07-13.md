# Relatório Meta Ads — Onvoix
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

> ⚠️ **Contexto crítico:** A queda em leads e gasto não reflete perda de eficiência do criativo em si — reflete o encerramento da campanha "Site - México", que sozinha gerou 140 leads a $0,26 CPL na semana anterior. A conta operou com metade do inventário esta semana.

---

## Módulo 1 — Auditoria de Campanhas e Anúncios

### Campanhas

| Campanha | Status | Gasto | Leads | CPL | CTR | CPM | Freq |
|---|---|---|---|---|---|---|---|
| Site - México — Registro | 🟢 OK | $44,91 | 80 | $0,56 | 22,16% | $8,16 | 1,18 |
| ~~Site - México~~ | ⛔ Pausada | — | — | — | — | — | — |

> **Média da conta (semana atual):** CPL $0,56 (única campanha ativa). Referência de thresholds calculada sobre este valor.

---

### Anúncios por Campanha

#### Site - México — Registro

*Ordenados por CPL (anúncios com leads primeiro)*

| Anúncio | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| VID 01 — Cópia | $34,81 | 69 | $0,50 | 24,18% | $7,49 | 1,16 | 🟢 OK |
| Ima 04 — Cópia | $3,56 | 9 | $0,40 | 11,35% | $9,62 | 1,58 | 🟢 OK |
| Ima 02 — Cópia | $0,20 | 1 | $0,20 | 42,86% | $28,57 | 1,00 | ⚪ Dados insuficientes |
| Ima 03 — Cópia | $0,41 | 1 | $0,41 | 21,43% | $29,29 | 1,17 | ⚪ Dados insuficientes |
| Ima 06 — Cópia | $5,88 | 0 | — | 10,48% | $12,84 | 1,15 | 🔴 CRÍTICO |
| Ima 01 — Cópia | $0,05 | 0 | — | 0,00% | $6,25 | 1,00 | ⚪ Dados insuficientes |

> **Ima 06 — Cópia:** $5,88 gastos, 0 leads → ultrapassa o threshold de $3 sem conversão. Status 🔴 CRÍTICO confirmado.

---

## Módulo 2 — Diagnóstico de CPL (Causa Raiz)

### Site - México — Registro

**CPL atual: $0,56 | CPL anterior (mesma campanha): $0,51 → variação: +9,8%**

A leve piora no CPL desta campanha isolada tem causa identificável:

- **CPM caiu de $17,93 → $8,16** (melhora de -54,6%): o algoritmo encontrou impressões mais baratas, possivelmente por menor concorrência no leilão ou expansão do público amplo.
- **CTR caiu de 26,05% → 22,16%** (queda de -14,9%): a distribuição de budget foi parcialmente canalizada para criativos de imagem menos eficientes (Ima 06 consumiu $5,88 sem nenhum lead), diluindo o CTR agregado da campanha.
- **Conclusão:** CPM mais barato parcialmente compensou o CTR menor, mas o Ima 06 agiu como "dreno silencioso" — consumiu $5,88 (13% do budget semanal) sem gerar nenhuma conversão, elevando o CPL médio em comparação ao potencial real do VID 01.

### Comparativo consolidado da conta (causa raiz da queda de leads)

| Fator | Impacto |
|---|---|
| "Site - México" pausada | Perda de 140 leads/semana a CPL $0,26 — causa principal da queda de -67% em leads |
| Ima 06 consumindo budget sem converter | Dreno de $5,88 sem retorno — eleva CPL da campanha ativa |
| CPM mais barato na campanha ativa | Fator positivo, parcialmente compensador |
| Público único ativo (México amplo) | Sem alternativa para escalar — todo budget em 1 ad set |

---

## Módulo 3 — Detecção de Anomalias

| Tipo | Anúncio | Detalhe | Ação Recomendada |
|---|---|---|---|
| 🔴 Zero leads com gasto acima de $3 | Ima 06 — Cópia | $5,88 gastos, 0 leads, CTR 10,48% — gasto 117x maior vs semana anterior ($0,98) sem conversão | Pausar imediatamente |
| 🔴 Campanha desaparecida | Site - México | Presente na semana anterior ($35,72 / 140 leads / CPL $0,26) — ausente esta semana | Investigar motivo do encerramento e reativar |
| 🟡 CPM anômalo em criativos de imagem | Ima 02 e Ima 03 | CPM $28,57 e $29,29 vs $7,49 do VID 01 — públicos muito pequenos ou lances competitivos | Monitorar: gastaram pouco (<$0,50), ainda sem significância |
| 🟡 Budget concentrado em 1 criativo | VID 01 — Cópia | Recebe 77,5% do gasto total da campanha ($34,81 de $44,91) | Saudável enquanto performa — testar novos criativos para reduzir dependência |

---

## Módulo 4 — Pacing Monitor

| Parâmetro | Valor |
|---|---|
| Dia do mês | 13 de 31 |
| % do mês decorrido | 41,9% |
| Gasto acumulado (estimado) | ~$44,91 (semana atual) |
| Projeção mensal | $192,47 |
| Budget mensal | $500,00 |
| Diferença | -$307,53 (-61,5%) |
| Status | 🔴 MUITO LENTO |

> **Análise:** No ritmo atual, julho encerrará com apenas $192 de $500 gastos — 38,5% do budget aproveitado. A causa direta é o encerramento da campanha "Site - México", que operava em paralelo e sozinha contribuía com ~$35/semana. Com apenas uma campanha ativa, o volume de impressões e conversões foi drasticamente reduzido. Ação urgente: reativar "Site - México" ou aumentar significativamente o budget diário da campanha ativa para compensar.

---

## Módulo 5 — Fadiga de Criativos

| Anúncio | Freq Atual | Freq Anterior | CTR | Leads | Status | Recomendação |
|---|---|---|---|---|---|---|
| VID 01 — Cópia | 1,16 | 1,25 (Registro) / 1,15 (México) | 24,18% | 69 | 🟢 OK | Manter — frequência saudável |
| Ima 04 — Cópia | 1,58 | 1,00 | 11,35% | 9 | 🟢 OK | Monitorar — frequência subiu 58% mas ainda dentro do intervalo OK |
| Ima 06 — Cópia | 1,15 | 1,08 (Registro) | 10,48% | 0 | 🟢 Freq OK / 🔴 CPL crítico | Pausar por performance, não por fadiga |
| Ima 03 — Cópia | 1,17 | 1,64 | 21,43% | 1 | 🟢 OK | Dados insuficientes — aguardar |
| Ima 02 — Cópia | 1,00 | 1,65 | 42,86% | 1 | 🟢 OK | Dados insuficientes — aguardar |
| Ima 01 — Cópia | 1,00 | 1,25 | 0,00% | 0 | 🟢 OK | Gasto mínimo ($0,05) — sem dados |

> **Resumo de fadiga:** Nenhum criativo apresenta risco de fadiga por frequência. Todos estão abaixo de 1,8. O problema do Ima 06 é de performance criativa (CTR baixo + zero conversões), não de saturação de público.

---

## Módulo 6 — Análise de Copy e Criativos

### 🏆 Criativo Vencedor

**VID 01 — Cópia** (formato: vídeo)
- CPL $0,50 com **69 leads** — estatisticamente significativo ✅
- CTR 24,18% com CPM baixíssimo de $7,49 — melhor relação volume/custo da conta
- Consistente nas duas semanas e em ambas as campanhas: $0,26 CPL em "Site - México" (140 leads), $0,50 em "Registro" (69 leads esta semana, 101 semana anterior)
- **Recomendação:** Manter como criativo principal. Candidato a escalar com aumento de budget.

### 🥈 Candidato a Escalar (com ressalva)

**Ima 04 — Cópia** (formato: imagem)
- CPL $0,40 com **9 leads** — volume mínimo atingido, pode ser considerado ✅
- CPL 28,6% abaixo da média da campanha ($0,56) — sinal positivo
- CTR 11,35% abaixo do VID 01, mas CPM ($9,62) competitivo
- **Ressalva:** 9 leads em $3,56 — aumentar budget gradualmente e monitorar se CPL se mantém. Volume ainda pequeno para conclusão definitiva.

### ⚠️ Criativos para Pausar

**Ima 06 — Cópia**
- $5,88 gastos, **0 leads**, CTR 10,48% — marcado como 🔴 CRÍTICO no Módulo 1 e anomalia no Módulo 3
- Padrão consistente: 0 leads na semana anterior também ($0,98 gastos)
- **Ação: pausar imediatamente.** O budget liberado (~$5-6/semana) pode ser realocado para VID 01 ou Ima 04.

### ⏳ Dados Insuficientes — Aguardar

- **Ima 02 — Cópia:** $0,20 gastos / 1 lead — CTR impressionante (42,86%) mas sem significância estatística. Gasto abaixo de $3. Aguardar.
- **Ima 03 — Cópia:** $0,41 gastos / 1 lead — também insuficiente. Aguardar.
- **Ima 01 — Cópia:** $0,05 gastos / 0 leads — sem dados úteis.

---

## Módulo 7 — Análise de Ad Sets e Públicos

| Ad Set | Campanha | Gasto | Leads | CPL | CTR | CPM | Freq |
|---|---|---|---|---|---|---|---|
| México amplo | Site - México — Registro | $44,91 | 80 | $0,56 | 22,16% | $8,16 | 1,18 |

**Observações:**

- **CPM extremamente baixo ($8,16):** indica que o público "México amplo" tem grande alcance disponível e pouca pressão de leilão — há espaço considerável para escalar budget sem deterioração imediata de CPM.
- **Público único ativo:** toda a conta depende de um único ad set. Não há risco de sobreposição no momento, mas há risco operacional alto — qualquer problema neste ad set (rejeição, saturação futura) paralisa toda a geração de leads.
- **Semana anterior:** quando "Site - México" estava ativa, seu público operava com CPM de $42,73 — significativamente mais caro. A campanha atual com CPM $8,16 sugere segmentação ou posicionamento diferente (ou mesmo público diferente dentro do México amplo). Vale investigar se a campanha pausada tinha ad set distinto.
- **Recomendação:** Criar um segundo ad set (ex: interesse específico ou lookalike) para reduzir dependência e testar CPM alternativo, aproveitando o espaço de escala identificado.

---

## Plano de Ação

| Prioridade | Ação | Impacto | Prazo |
|---|---|---|---|
| 🔴 P1 | **Pausar Ima 06 — Cópia:** $5,88 sem leads em 2 semanas consecutivas. Realocar budget para VID 01 | Alto — elimina dreno de budget | Hoje |
| 🔴 P2 | **Investigar e reativar "Site - México":** campanha gerava 140 leads/semana a CPL $0,26 — melhor performance da conta. Identificar por que foi pausada | Muito alto — pode dobrar volume de leads e reduzir CPL de volta a ~$0,35 | Hoje |
| 🔴 P3 | **Aumentar budget diário da campanha ativa:** pacing em -61,5% — projeção $192 vs $500 budget. CPM baixo ($8,16) indica espaço de escala disponível | Alto — corrige pacing e aproveita janela de CPM barato | 24h |
| 🟡 P4 | **Monitorar Ima 04 — Cópia por mais 1 semana:** CPL $0,40 com 9 leads é promissor — confirmar consistência antes de escalar budget | Médio — pode revelar segundo criativo vencedor | 48-72h |
| 🟡 P5 | **Aguardar dados de Ima 02 e Ima 03:** CTR alto mas gasto < $0,50. Não pausar — deixar o algoritmo distribuir mais antes de julgar | Baixo/Médio | Próxima semana |
| 🟢 P6 | **Criar segundo ad set** (lookalike ou interesse) para reduzir dependência do México amplo e testar CPM alternativo | Médio — diversificação operacional | Próximos 7 dias |

---

## BLOCO TRELLO

---

**Meta Ads Onvoix — 13/07/2026**
Gasto: $44,91 | Leads: 80 | CPL: $0,56
Variação vs semana anterior: CPL +55,6% 🔴 | Leads -67,1% 🔴
Pacing: 🔴 MUITO LENTO — Projeção $192 vs Budget $500 (41,9% do mês decorrido)

---

**📌 CONTEXTO DA SEMANA**
A campanha "Site - México" — que na semana anterior gerou 140 leads a CPL $0,26, o melhor resultado histórico recente da conta — não está ativa nesta semana. A causa do encerramento precisa ser investigada com urgência, pois essa campanha sozinha respondia por 58% dos leads totais da semana anterior. Toda a operação atual está concentrada em uma única campanha ("Site - México — Registro") com um único ad set, o que aumenta o risco operacional e explica diretamente a queda de -67% em leads e o estouro do CPL.

---

**📊 PANORAMA DA SEMANA**

**🔍 Campanhas & Anúncios**
Apenas 1 campanha ativa esta semana: "Site - México — Registro", com ad set "México amplo" e 6 anúncios rodando. O VID 01 — Cópia domina com 77,5% do budget ($34,81) e entrega os melhores resultados. O Ima 04 aparece como candidato secundário consistente. Os demais criativos de imagem ou têm gasto irrisório (abaixo de $0,50) e precisam de mais tempo, ou estão ativamente prejudicando a campanha — caso do Ima 06 — Cópia, que consumiu $5,88 sem gerar nenhum lead.

**📉 Causa Raiz do CPL**
O CPL subiu de $0,36 para $0,56 (+55,6%), mas a causa não é deterioração do criativo principal — é estrutural. A campanha "Site - México" estava convertendo a $0,26 CPL e foi encerrada, removendo o segmento mais eficiente da conta. Dentro da campanha ativa, o CPL saiu de $0,51 para $0,56 (+9,8%), variação pequena explicada pelo Ima 06 atuando como dreno: gastou $5,88 (13% do budget) com 0 leads, elevando a média. O CPM caiu muito ($17,93 → $8,16), o que é positivo, mas o CTR também caiu (26% → 22%) por causa da distribuição para criativos menos eficientes.

**⚠️ Anomalias**
- 🔴 **Ima 06 — Cópia:** $5,88 gastos, 0 leads — segunda semana consecutiva sem conversão. Dreno ativo de budget.
- 🔴 **Campanha "Site - México" ausente:** desapareceu sem registro de motivo. Era a principal fonte de leads ($0,26 CPL, 140 leads/semana).

**📅 Pacing**
No ritmo atual, julho encerrará com apenas $192 de $500 gastos — aproveitando menos de 40% do budget mensal. A causa direta é o encerramento da "Site - México", que contribuía com ~$35/semana de gasto adicional. Com apenas uma campanha ativa e budget diário limitado, a conta está drasticamente subpacificada. Ação necessária: reativar a campanha pausada E/OU aumentar o budget diário da campanha ativa — o CPM baixo ($8,16) confirma que há espaço de escala disponível no público sem deterioração imediata de custos.

**😴 Fadiga de Criativos**
Situação tranquila. Nenhum criativo acima de 1,58 de frequência — todos abaixo do limiar de atenção (1,8). O Ima 04 subiu de 1,00 para 1,58, mas ainda dentro do intervalo seguro. Fadiga não é risco esta semana.

**🎨 Criativos**
🏆 Vencedor principal: **VID 01 — Cópia** — CPL $0,50 com **69 leads** (vídeo) — consistente em duas campanhas e duas semanas
🥈 Candidato a escalar: **Ima 04 — Cópia** — CPL $0,40 com **9 leads** (imagem) — monitorar mais 1 semana antes de escalar
🔴 Para pausar: **Ima 06 — Cópia** — $5,88 sem nenhum lead em 2 semanas consecutivas
⏳ Dados insuficientes (aguardar): Ima 02, Ima 03, Ima 01

**🎯 Ad Sets & Públicos**
CPM de $8,16 no "México amplo" é um sinal claro de público com amplo inventário disponível — há espaço para aumentar budget sem pressionar o leilão imediatamente. O risco atual é de concentração total: 100% dos leads dependem de um único ad set. Criar um segundo ad set (lookalike ou por interesse) nos próximos 7 dias é recomendado para diversificação e escala.

---

**🚀 PRÓXIMOS PASSOS**
- 🔴 **Pausar Ima 06 — Cópia hoje** — 2 semanas, $6,86 gastos acumulados, zero leads. Realocar para VID 01.
- 🔴 **Investigar e reativar "Site - México" hoje** — era a campanha mais eficiente da conta (CPL $0,26, 140 leads/semana). Ausência direta causa o pacing crítico e a queda de leads.
- 🔴 **Aumentar budget diário da campanha ativa em 24h** — pacing em -61,5%, CPM baixo confirma espaço de escala. Sem reativação da outra campanha, o budget mensal ficará 60% subutilizado.
- 🟡 **Avaliar Ima 04 — Cópia na próxima semana** — CPL $0,40 com 9 leads é promissor. Se mantiver consistência, escalar budget gradualmente.
- 🟢 **Criar segundo ad set nos próximos 7 dias** — reduzir dependência operacional do México amplo e testar CPM em segmento alternativo.

---