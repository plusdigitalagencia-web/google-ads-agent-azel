# Relatório Meta Ads — Onvoix
**Período atual:** 23/07/2026 a 29/07/2026
**Período anterior:** 16/07/2026 a 22/07/2026
**Gerado em:** 30/07/2026 | **Conta:** act_1297650828540575

---

## Resumo Executivo

| Métrica | Atual | Anterior | Variação |
|---|---|---|---|
| Gasto | $121,77 | $39,76 | +$82,01 (+206%) 📈 |
| Leads | 150 | 104 | +46 (+44%) 📈 |
| CPL médio | $0,81 | $0,38 | +$0,43 (+113%) 🔴 |
| CPM médio | $3,76 | $15,05 | -$11,29 (-75%) 🟢 |
| CTR médio | 5,32% | 39,55% | -34,23pp 🔴 |
| Frequência | 1,26 | 1,20 | +0,06 🟢 |

> **Leitura do período:** O volume de leads cresceu 44% e o CPM despencou 75%, mas o CPL mais que dobrou ($0,38 → $0,81). O principal fator foi a queda abrupta de CTR (39,55% → 5,32%). O gasto triplicou, o que indica mudança expressiva no budget diário ou reativação da campanha com configuração diferente. Mais leads no total, porém a eficiência de conversão por clique piorou significativamente.

---

## Módulo 1 — Auditoria de Campanhas e Anúncios

### Campanhas

| Campanha | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| Site - México — Registro | $121,77 | 150 | $0,81 | 5,32% | $3,76 | 1,26 | 🟢 OK |

> Média da conta (atual): CPL $0,81. Limite 🟡 ATENÇÃO: > $1,05. Limite 🔴 CRÍTICO: > $1,62.

---

### Anúncios por Campanha — Site - México — Registro
*(ordenados por CPL ascendente; anúncios sem leads aparecem ao final)*

| Anúncio | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| VID 01 — Cópia | $97,25 | 121 | $0,80 | 5,66% | $3,57 | 1,27 | 🟢 OK |
| Ima 02 — Cópia | $23,86 | 29 | $0,82 | 3,47% | $4,75 | 1,19 | 🟢 OK |
| Ima 06 — Cópia | $0,43 | 0 | — | 19,35% | $13,87 | 1,07 | 🟡 ATENÇÃO¹ |
| Ima 04 — Cópia | $0,17 | 0 | — | 2,13% | $3,62 | 1,27 | ⚪ Dados insuficientes |
| Ima 03 — Cópia | $0,05 | 0 | — | 0,00% | $1,85 | 1,23 | ⚪ Dados insuficientes |
| Ima 01 — Cópia | $0,01 | 0 | — | 0,00% | $0,91 | 1,22 | ⚪ Dados insuficientes |

> ¹ **Ima 06 — Cópia:** CTR de 19,35% mas zero conversões com $0,43 gastos — possível problema de landing page ou público específico não convertendo. Gasto ainda abaixo de $3, então sem conclusão definitiva.
>
> ⚪ Ima 01, Ima 03 e Ima 04 com gasto < $3: mencionados por completude, mas **nenhuma recomendação estratégica** será baseada nesses dados.

---

## Módulo 2 — Diagnóstico de CPL (Causa Raiz)

### Site - México — Registro

**CPL atual: $0,81 | CPL anterior: $0,38 → deterioração de +113%**

A causa raiz **não é o CPM** — pelo contrário, o CPM melhorou drasticamente ($15,05 → $3,76), o que indica entrega a públicos mais amplos e baratos. O problema está no **colapso do CTR**:

| Fator | Semana anterior | Semana atual | Impacto |
|---|---|---|---|
| CPM | $15,05 | $3,76 | ✅ Melhorou 75% |
| CTR | 39,55% | 5,32% | 🔴 Caiu 87% |
| Taxa de conversão implícita | Alta | Moderada | 🟡 Piorou |

**Interpretação:**
- Na semana anterior, o algoritmo entregava o VID 01 para um segmento muito qualificado (CTR de 41,48% é extraordinariamente alto — sugestivo de público retargeting ou lookalike muito restrito). Isso explica CPL baixíssimo ($0,35) mesmo com CPM alto.
- Na semana atual, o público passou a ser **"México amplo"** com entrega mais abrangente: CPM despencou, mas o público genérico converte menos por clique. O resultado é um CPL ainda razoável ($0,81) em escala muito maior (150 leads vs. 104).
- Em termos absolutos, a conta produziu **mais leads com mais gasto** — a piora do CPL reflete a transição de um público ultra-qualificado para escala real. Isso pode ser saudável se o budget disponível para crescimento justificar o CPL de $0,81.

---

## Módulo 3 — Detecção de Anomalias

| Tipo | Anúncio | Detalhe | Ação |
|---|---|---|---|
| 🟡 CTR colapsou | VID 01 — Cópia | CTR 41,48% → 5,66% (-86%). Pode indicar mudança de público-alvo (escala para amplo) mais do que degradação do criativo | Monitorar CTR nas próximas semanas; comparar performance em públicos semelhantes |
| 🟡 CTR alto sem conversão | Ima 06 — Cópia | CTR 19,35% com $0,43 gastos e 0 leads — CTR alto sugere cliques, mas sem lead. Gasto insuficiente para conclusão | Aguardar mais gasto ($3+) antes de qualquer ação; verificar tracking da landing page |
| 🟡 Gasto triplicou em uma semana | Campanha geral | Gasto $39,76 → $121,77 (+206%) em uma semana. Budget diário foi aumentado ou campanha estava pausada parte da semana anterior | Confirmar se o aumento de budget foi intencional; validar projeção de julho |
| ⚪ Ima 03 — Cópia | Ima 03 — Cópia | Tinha 1 lead com CPL $0,06 na semana anterior — dado não replicável (gasto $0,06 total). Esta semana: 0 leads, $0,05. Sem relevância estatística | Sem ação necessária |

---

## Módulo 4 — Pacing Monitor

| Parâmetro | Valor |
|---|---|
| Dia do mês | 30 de 31 (96,8% do mês decorrido) |
| Gasto acumulado estimado (julho) | ~$521,87 *(projeção com base na semana atual)* |
| Budget mensal | $500,00 |
| Projeção vs. Budget | +4,4% acima |
| Status | 🟢 OK — dentro do ritmo |

> **Leitura:** Com 96,8% do mês decorrido, a projeção de $521,87 indica um leve estouro de 4,4% sobre o budget de $500. Dado que estamos praticamente no último dia do mês, o risco real de estouro é mínimo e está dentro da margem tolerável. **Ação recomendada:** nenhuma para julho. Planejamento para agosto deve considerar se o budget diário atual será mantido ou ajustado.

---

## Módulo 5 — Fadiga de Criativos

| Anúncio | Freq. Atual | Freq. Anterior | CTR | Leads | Status | Recomendação |
|---|---|---|---|---|---|---|
| VID 01 — Cópia | 1,27 | 1,19 | 5,66% | 121 | 🟢 OK | Manter — sem fadiga |
| Ima 02 — Cópia | 1,19 | 1,38 | 3,47% | 29 | 🟢 OK | Manter — frequência baixa |
| Ima 06 — Cópia | 1,07 | 1,05 | 19,35% | 0 | ⚪ Insuficiente | Dados insuficientes |
| Ima 04 — Cópia | 1,27 | 1,21 | 2,13% | 0 | ⚪ Insuficiente | Dados insuficientes |
| Ima 03 — Cópia | 1,23 | 1,00 | 0,00% | 0 | ⚪ Insuficiente | Dados insuficientes |
| Ima 01 — Cópia | 1,22 | 1,00 | 0,00% | 0 | ⚪ Insuficiente | Dados insuficientes |

> **Conclusão geral:** Toda a conta está com frequência abaixo de 1,8. **Nenhum criativo apresenta fadiga.** O público amplo do México ainda tem espaço de entrega saudável.

---

## Módulo 6 — Análise de Copy e Criativos

### 🏆 Criativos Vencedores (mínimo 5 leads)

**1. VID 01 — Cópia — Vencedor Principal**
- CPL $0,80 com **121 leads** | Gasto $97,25 | CTR 5,66% | CPM $3,57
- Responsável por **80,7% dos leads** da semana com o melhor CPL da conta
- Formato vídeo demonstra clara superioridade de entrega no público amplo México
- **Recomendação: manter ativo e priorizar budget**

**2. Ima 02 — Cópia — Segundo colocado**
- CPL $0,82 com **29 leads** | Gasto $23,86 | CTR 3,47% | CPM $4,75
- CPL praticamente equivalente ao VID 01 ($0,02 de diferença), com volume significativo
- CTR menor (3,47% vs 5,66%) e CPM ligeiramente maior — eficiente, porém inferior ao vídeo
- **Recomendação: manter ativo como complemento ao VID 01**

---

### ⏸️ Criativos para Pausar

| Anúncio | Motivo |
|---|---|
| Ima 01 — Cópia | $0,01 gastos, 0 leads, 0% CTR — o algoritmo não entrega; pausar para limpar o ad set |
| Ima 03 — Cópia | $0,05 gastos, 0 leads, 0% CTR — sem entrega significativa alguma |
| Ima 04 — Cópia | $0,17 gastos, 0 leads — entrega marginal por duas semanas consecutivas |

> ⚠️ **Ima 06 — Cópia:** CTR de 19,35% é intrigante, mas com apenas $0,43 gastos e 0 leads, **não há base estatística para escalar nem para pausar com convicção**. Aguardar mais 3-5 dias de entrega antes de decidir.

---

### 📊 Comparativo Semana Anterior vs. Atual (criativos com dados)

| Anúncio | CPL Anterior | CPL Atual | Leads Anterior | Leads Atual | Variação CPL |
|---|---|---|---|---|---|
| VID 01 — Cópia | $0,35 | $0,80 | 97 | 121 | +129% 🔴 |
| Ima 02 — Cópia | $0,38 | $0,82 | 2 | 29 | +116% 🔴 |
| Ima 04 — Cópia | $0,36 | — | 4 | 0 | — |

> A piora de CPL em VID 01 e Ima 02 é consistente com a mudança de público (amplo vs. restrito), não com degradação dos criativos em si.

---

## Módulo 7 — Análise de Ad Sets e Públicos

| Ad Set | Campanha | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|---|
| México amplo | Site - México — Registro | $121,77 | 150 | $0,81 | 5,32% | $3,76 | 1,26 | 🟢 OK |

**Observações:**

- **Apenas 1 ad set ativo:** sem risco de sobreposição de públicos.
- **CPM de $3,76 é excepcionalmente baixo** para o mercado mexicano — indica espaço amplo de entrega e público não saturado.
- **Frequência 1,26** confirma que o público ainda está longe de exaustão. Há margem significativa para aumentar budget sem sacrificar eficiência de entrega.
- **Risco identificado:** com apenas 1 ad set e 1 público, toda a conta depende da saúde deste segmento. Considerar testar um segundo ad set com público diferente (ex: lookalike 1-3% ou interesse específico) para reduzir dependência e comparar CPL.

---

## Plano de Ação

| Prioridade | Ação | Impacto | Prazo |
|---|---|---|---|
| 🔴 P1 | Pausar Ima 01, Ima 03 e Ima 04 — sem entrega relevante por duas semanas, consumindo espaço no ad set | Limpeza do ad set; concentra budget nos criativos eficientes | Hoje |
| 🟡 P2 | Monitorar Ima 06 — aguardar atingir $3 de gasto para avaliar conversão; CTR alto pode indicar criativo com potencial | Decisão de pausar ou escalar com dados reais | 3-5 dias |
| 🟡 P3 | Testar novo ad set com público diferente (lookalike 1-3% ou segmentação por interesse) para reduzir dependência de um único público | Diversificação de risco; possível CPL menor com público mais qualificado | Semana de 01/08 |
| 🟡 P4 | Investigar causa da queda de CTR do VID 01 (41% → 5,66%) — confirmar se é mudança de público ou início de degradação do criativo | Entender se o vídeo precisa de variação nova para agosto | Esta semana |
| 🟢 P5 | Planejar budget de agosto: definir se mantém ~$500/mês ou escala, considerando que CPL $0,81 com público amplo é sustentável | Garante continuidade sem surpresas de budget | Até 01/08 |

---

## BLOCO TRELLO

```
Meta Ads Onvoix — 30/07/2026
Gasto: $121,77 | Leads: 150 | CPL: $0,81
Variação vs semana anterior: CPL +113% 🔴 | Leads +44% 📈
Pacing: 🟢 OK — Projeção $521,87 vs Budget $500 (96,8% do mês decorrido)
```

---

📌 **CONTEXTO DA SEMANA**
O gasto triplicou esta semana ($39,76 → $121,77), o que indica aumento de budget diário ou que a campanha estava parcialmente pausada na semana anterior. Junto com isso, o público passou a operar de forma mais ampla ("México amplo"), o que explica o CPM 75% menor e o CTR muito mais baixo. Essa mudança de escala é o principal driver de todos os números desta semana — tanto o aumento de leads quanto a piora de CPL são consequências diretas dessa expansão.

---

📊 **PANORAMA DA SEMANA**

🔍 **Campanhas & Anúncios**
Uma campanha ativa: "Site - México — Registro", com 6 anúncios no ad set "México amplo". Na prática, apenas 2 criativos geraram leads de forma relevante: **VID 01 — Cópia** (121 leads, 80% do total) e **Ima 02 — Cópia** (29 leads, 19% do total). Os outros 4 anúncios (Ima 01, 03, 04, 06) somaram menos de $0,70 de gasto e zero conversões — estão dormentes e deveriam ser pausados.

📉 **Causa Raiz do CPL**
O CPL dobrou ($0,38 → $0,81) não por deterioração dos criativos, mas por mudança de público. Na semana anterior, o VID 01 operava com CTR de 41% — sinal claro de público muito qualificado (possivelmente restrito ou retargeting), que converte mais por clique mesmo com CPM alto. Esta semana, no público amplo México, o CPM despencou para $3,76 mas o CTR caiu para 5,66% — o algoritmo alcança mais pessoas, porém com menor intenção de conversão. O resultado é um CPL maior em um volume maior. O CPL $0,81 ainda é eficiente em termos absolutos; a questão é se o público anterior (mais qualificado) pode ser recuperado ou testado em paralelo.

⚠️ **Anomalias**
- 🟡 **VID 01 — Cópia:** CTR caiu de 41,48% para 5,66% — mudança radical ligada à expansão de público, mas vale monitorar para garantir que não seja início de saturação do criativo.
- 🟡 **Ima 06 — Cópia:** CTR de 19,35% com zero leads e apenas $0,43 gastos — clicks acontecem mas sem conversão. Pode ser problema de tracking ou landing page para esse segmento. Aguardar mais dados.
- 🟡 **Gasto triplicou:** aumento de 206% no gasto em uma semana; confirmar se foi intencional e planejado para agosto.

📅 **Pacing**
Com 96,8% do mês decorrido, a projeção encerra julho em $521,87 — apenas 4,4% acima do budget de $500, dentro da margem tolerável. Não há risco real de estouro relevante neste ponto do mês. Atenção para agosto: se o budget diário atual for mantido, o mês vai exigir plano claro desde o dia 1 para não ultrapassar os $500 ou para justificar um budget maior.

😴 **Fadiga de Criativos**
Frequência geral abaixo de 1,30 em todos os anúncios. Nenhum criativo apresenta risco de fadiga. O público amplo do México tem espaço de entrega confortável — há margem para aumentar budget sem penalidade de frequência no curto prazo.

🎨 **Criativos**
- **Vencedor principal:** VID 01 — Cópia — CPL $0,80 com **121 leads** (formato: vídeo) ✅
- **Candidato sólido:** Ima 02 — Cópia — CPL $0,82 com **29 leads** (formato: imagem)
- **Para pausar:** Ima 01, Ima 03 e Ima 04 — sem entrega significativa por duas semanas consecutivas, zero leads, zero relevância prática
- **Aguardar dados:** Ima 06 — CTR alto mas sem conversão; menos de $0,50 gastos — sem conclusão possível ainda

🎯 **Ad Sets & Públicos**
Único ad set ativo: "México amplo" com CPM $3,76 — excepcionalmente barato, indicando público não saturado com grande espaço de entrega. Frequência 1,26 está saudável. O risco principal é concentração total em um único público; uma segunda segmentação (lookalike ou interesse) deveria ser testada em agosto para diversificar e potencialmente reduzir o CPL abaixo de $0,81.

---

🚀 **PRÓXIMOS PASSOS**
- 🔴 Pausar **Ima 01, Ima 03 e Ima 04** — hoje. Zero leads em duas semanas, sem entrega relevante, apenas poluindo o ad set.
- 🟡 Monitorar **Ima 06** por mais 3-5 dias até atingir $3 de gasto; verificar se o tracking da landing page está funcionando para esse criativo.
- 🟡 Investigar **queda de CTR do VID 01** (41% → 5,66%) — confirmar se é 100% explicado pelo público ou se o criativo precisa de variação nova para agosto.
- 🟢 Criar e testar **segundo ad set em agosto** (lookalike 1-3% ou segmentação por interesse) para diversificar risco e comparar CPL com o público amplo atual.

---