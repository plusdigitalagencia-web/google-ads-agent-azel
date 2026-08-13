# Relatório Meta Ads — Leblon Real Estate
**Período atual:** 06/08/2026 a 12/08/2026
**Período anterior:** 30/07/2026 a 05/08/2026
**Gerado em:** 13/08/2026 | **Conta:** act_1187011709535726

---

## Resumo Executivo

| Métrica | Atual | Anterior | Variação |
|---|---|---|---|
| Gasto | €298,28 | €287,24 | +€11,04 (+3,8%) 📈 |
| Leads | 17 | 28 | -11 leads (-39,3%) 📉 |
| CPL Médio | €17,55 | €10,26 | +€7,29 (+71,1%) 🔴 |
| CPM Médio | €11,19 | €11,24 | -€0,05 (-0,4%) ➡️ |
| CTR Médio | 1,86% | 2,13% | -0,27pp (-12,7%) 📉 |
| Frequência Média | 1,84 | 1,88 | -0,04 ➡️ |

> ⚠️ **Semana crítica:** o CPL disparou +71% enquanto o volume de leads caiu quase 40%. O gasto cresceu levemente, mas a eficiência despencou. A causa principal não é CPM (praticamente estável) — é a piora estrutural da taxa de conversão, impulsionada pela degradação do criativo AD06 na campanha Europa e pelo baixo desempenho do AD15 na campanha México.

---

## Módulo 1 — Auditoria de Campanhas e Anúncios

### Campanhas

| Campanha | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| DK - [CPL] [MEXICO] [FORMS] [BOF] [09/10] | €157,75 | 9 | €17,53 | 1,75% | €14,73 | 1,74 | 🟡 ATENÇÃO |
| [CPL][EUROPA] | €140,53 | 8 | €17,57 | 1,96% | €7,66 | 1,95 | 🟡 ATENÇÃO |

> **Referência:** CPL médio da conta = €17,55 | Limiar 🟡 = até €22,82 | Limiar 🔴 = acima de €35,10
> Ambas as campanhas estão em ATENÇÃO — o CPL atual (€17,55) já representa +71% do CPL da semana passada (€10,26), mas ainda abaixo do dobro da média atual. O alerta real está na **trajetória de piora**, não apenas no número absoluto desta semana.

---

### Anúncios por Campanha

#### DK - [CPL] [MEXICO] [FORMS] [BOF] [09/10] (ordenado por CPL)

| Anúncio | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| AD10 - [IMG] [PROPRIEDADES PREMIUM] — Cópia | €96,38 | 8 | €12,05 | 1,80% | €12,57 | 1,61 | 🟢 OK |
| AD15 - [IMG] [para unos pocos] novo | €61,37 | 1 | €61,37 | 1,64% | €20,15 | 1,45 | 🔴 CRÍTICO |

> AD15 gastou €61,37 e gerou apenas 1 lead — CPL de €61,37, mais de 3,5× a média da conta. Volume insuficiente para qualquer conclusão sobre o criativo em si, mas o gasto já é alto demais para seguir sem conversão.

#### [CPL][EUROPA] (ordenado por CPL)

| Anúncio | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| AD07 | €131,30 | 8 | €16,41 | 1,94% | €7,34 | 1,91 | 🟢 OK |
| AD06 | €8,01 | 0 | — | 3,06% | €20,43 | 2,20 | 🔴 CRÍTICO |
| AD05 | €1,20 | 0 | — | 0,00% | €20,69 | 1,21 | *(gasto insuficiente)* |
| AD010 (v1) | €0,02 | 0 | — | 0,00% | €5,00 | 1,00 | *(gasto insuficiente)* |
| AD010 (v2) | €0,00 | 0 | — | 0,00% | €0,00 | 1,00 | *(sem entrega)* |

> ⚠️ **AD06 — anomalia crítica:** semana anterior gerou 6 leads com CPL €7,02 (melhor da conta). Nesta semana: €8,01 gastos, 0 leads, CPM dobrou para €20,43. Queda abrupta de desempenho — investigação imediata necessária (ver Módulo 3).

---

## Módulo 2 — Diagnóstico de CPL (Causa Raiz)

### DK - [CPL] [MEXICO] [FORMS] [BOF] [09/10]
**CPL: €12,36 → €17,53 (+41,8%)**

| Variável | Semana Anterior | Semana Atual | Impacto |
|---|---|---|---|
| CPM | €12,25 | €14,73 | ⬆️ +20,2% — contribui parcialmente |
| CTR | 1,95% | 1,75% | ⬇️ -10,3% — contribui |
| Gasto | €148,35 | €157,75 | +6,3% |
| Leads | 12 | 9 | -25% |

**Causa raiz:** dupla pressão — CPM subiu 20% (encarecimento do leilão no público México) e CTR caiu 10%. Juntos, reduziram a taxa de conversão geral. Agravante: o budget foi parcialmente desviado para o AD15 (€61,37 com 1 lead), que "roubou" investimento do AD10, que é o criativo eficiente. Na semana anterior, o AD10 rodou com €143 e gerou 12 leads; agora rodou com apenas €96 e gerou 8 — CPL estável no ad em si (€11,92 → €12,05), mas volume menor.

> **Diagnóstico real:** o problema no México não é deterioração do criativo principal (AD10), mas a ativação mal executada do AD15, que consumiu 39% do budget da campanha com retorno mínimo.

---

### [CPL][EUROPA]
**CPL: €8,68 → €17,57 (+102,4%)**

| Variável | Semana Anterior | Semana Atual | Impacto |
|---|---|---|---|
| CPM | €10,23 | €7,66 | ⬇️ -25,1% — melhorou |
| CTR | 2,32% | 1,96% | ⬇️ -15,5% — piorou |
| Leads | 16 | 8 | -50% |
| AD06 leads | 6 | 0 | 💥 perda crítica |

**Causa raiz:** o CPM na Europa **melhorou** significativamente (-25%). O CTR caiu moderadamente. O problema é estrutural: **o AD06 parou de converter**. Semana passada, o AD06 era o segundo melhor criativo da conta (CPL €7,02, 6 leads). Nesta semana, gastou €8,01 e não gerou nenhum lead — enquanto seu CPM quase dobrou (€10,75 → €20,43). Isso indica que o algoritmo passou a distribuir o AD06 para segmentos menos qualificados ou que houve mudança interna (copy, landing, form) que quebrou o funil. Essa perda de 6 leads representa isoladamente uma queda de €42 em eficiência.

> **Diagnóstico real:** CPL da Europa dobrou não porque a campanha piorou como um todo, mas porque o segundo criativo mais eficiente da conta (AD06) colapsou nesta semana. O AD07 manteve performance estável.

---

## Módulo 3 — Detecção de Anomalias

| Tipo | Anúncio | Variação | Ação Recomendada |
|---|---|---|---|
| 🔴 Colapso de conversão | AD06 ([CPL][EUROPA]) | 6 leads → 0 leads; CPM €10,75 → €20,43 (+90%) | Investigar imediatamente: verificar formulário, landing ou mudança de distribuição. Pausar se não resolver em 24h |
| 🔴 CPL explosivo | AD15 - [IMG] [para unos pocos] novo | €61,37 gastos, 1 lead — CPL 3,5× a média da conta | Pausar. Gasto já supera threshold de €15 com resultado mínimo |
| 🟡 Budget mal distribuído | AD10 vs AD15 (campanha México) | AD10 rodou com 33% menos budget (-€46) perdendo ~4 leads | Realocar budget: concentrar no AD10 enquanto AD15 está pausado |
| 🟡 Ad set #2 - [ALE][BEL][HOL] | Ad set duplicado (Europa) | €8,01 gastos, 0 leads, CPM €20,38 vs €7,38 do ad set principal | Pausar o ad set duplicado — performance muito inferior |
| ℹ️ Sem entrega | AD010 (v2) | €0,00 gastos — sem entrega na semana | Verificar se está ativo ou se foi pausado manualmente |

---

## Módulo 4 — Pacing Monitor

| Métrica | Valor |
|---|---|
| Dia do mês | 13 de 31 |
| % do mês decorrido | 41,9% |
| Gasto até agora (estimado mês) | ~€627 *(aproximação: 2 semanas + dados parciais)* |
| Gasto semana atual | €298,28 |
| Projeção mensal | €1.278,34 |
| Budget mensal | €1.500,00 |
| Diferença | -€221,66 (-14,8%) |

**Status de Pacing: 🟡 LENTO**

> No ritmo atual, agosto encerrará com aproximadamente **€1.278 dos €1.500 disponíveis** — 14,8% abaixo do budget, ultrapassando o limiar de 10% que aciona alerta amarelo. Com 41,9% do mês decorrido e apenas 17 leads na semana mais recente (vs. 28 na anterior), o mês corre risco de fechar com volume de leads abaixo do esperado. A principal alavanca para corrigir o pacing **não é aumentar o budget diário de forma indiscriminada**, mas garantir que o budget disponível seja gasto em criativos eficientes (AD10 e AD07) — pausando AD15 e o ad set duplicado que desperdiçam verba sem retorno.

---

## Módulo 5 — Fadiga de Criativos

| Anúncio | Frequência | CTR | Leads | Status | Recomendação |
|---|---|---|---|---|---|
| AD10 - [IMG] [PROPRIEDADES PREMIUM] — Cópia | 1,61 | 1,80% | 8 | 🟢 OK | Manter — sem sinais de fadiga |
| AD07 | 1,91 | 1,94% | 8 | 🟢 Monitorar | Frequência levemente elevada; CTR ainda saudável |
| AD06 | 2,20 | 3,06% | 0 | 🟡 ATENÇÃO | Frequência em zona de atenção; colapso de conversão não explicado por fadiga (CTR alto) — investigar formulário/funil |
| AD15 - [IMG] [para unos pocos] novo | 1,45 | 1,64% | 1 | 🔴 CRÍTICO (CPL) | Frequência baixa; problema não é fadiga, é ineficiência do criativo em si |
| AD05 | 1,21 | 0,00% | 0 | *(gasto insuficiente)* | Aguardar mais dados |

> **Nota sobre AD06:** a frequência de 2,20 está na zona de atenção, mas o CTR permanece alto (3,06%). Isso indica que o público ainda clica — o colapso de leads está provavelmente no funil pós-clique (formulário, landing page, segmentação do ad set), não na fadiga criativa em si.

**Escala de referência:** < 1,8 = OK | 1,8–2,5 = Monitorar | 2,5–3,5 = Atenção | > 3,5 = Fadiga crítica

---

## Módulo 6 — Análise de Copy e Criativos

### 🏆 Criativos Vencedores

**AD10 - [IMG] [PROPRIEDADES PREMIUM] — Cópia** (Campanha México)
- CPL €12,05 com **8 leads** | CPM €12,57 | CTR 1,80% | Freq 1,61
- Consistência semana a semana: CPL €11,92 na semana anterior (12 leads) — desempenho estável e confiável
- **Recomendação: escalar.** É o criativo mais consistente da conta. Com o budget liberado pela pausa do AD15, o AD10 deve receber alocação prioritária.

**AD07** (Campanha Europa)
- CPL €16,41 com **8 leads** | CPM €7,34 | CTR 1,94% | Freq 1,91
- Semana anterior: CPL €9,46, 10 leads — leve piora, mas o CPM está no menor nível registrado (€7,34). A queda no volume pode ser efeito da divisão de budget com AD06 e ad sets secundários.
- **Recomendação: manter e consolidar.** Com o ad set duplicado pausado, o AD07 deve concentrar o budget da campanha Europa.

---

### 🔴 Criativos para Pausar

| Criativo | Motivo |
|---|---|
| **AD15 - [IMG] [para unos pocos] novo** | €61,37 gastos, 1 lead, CPL €61,37 — 3,5× a média. Gasto já supera threshold de €15 sem retorno. Marcado como anomalia crítica no Módulo 3. |
| **AD06** | Colapso abrupto: 6 leads → 0 leads. CPM quase dobrou. Antes de reativar, investigar o funil pós-clique (formulário, landing). Marcado como anomalia crítica no Módulo 3. |

---

### ⏳ Dados Insuficientes (aguardar ou investigar)
- **AD05:** €1,20 gastos, 0 leads — sem significância estatística. Verificar se está ativo.
- **AD010 (ambas as versões):** gasto praticamente zero. Verificar status de entrega.

---

## Módulo 7 — Análise de Ad Sets e Públicos

| Ad Set | Campanha | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|---|
| [PS - Cidades x Rico X México] | México | €96,38 | 8 | €12,05 | 1,80% | €12,57 | 1,61 | 🟢 OK |
| [ALE][BEL][HOL] | Europa | €132,52 | 8 | €16,57 | 1,94% | €7,38 | 1,91 | 🟢 OK |
| #2 - [ALE][BEL][HOL] | Europa | €8,01 | 0 | — | 3,05% | €20,38 | 2,20 | 🔴 CRÍTICO |
| #2- [PS - Cidades x Rico X México] | México | €61,37 | 1 | €61,37 | 1,64% | €20,15 | 1,45 | 🔴 CRÍTICO |

### Observações:

**Sobreposição de públicos — risco real:**
Ambas as campanhas têm um ad set principal e um duplicado (#2) com o mesmo target geográfico. Os ad sets duplicados têm CPM significativamente mais alto que os principais (€20,15 vs €12,57 no México; €20,38 vs €7,38 na Europa), sugerindo que estão competindo no mesmo leilão e encarecendo o custo de ambos.

**Ad set [PS - Cidades x Rico X México]:** público sólido — CPM razoável, boa conversão, frequência segura (1,61). Ainda tem espaço para escalar.

**Ad set [ALE][BEL][HOL]:** CPM excepcionalmente baixo (€7,38) para o mercado europeu — excelente eficiência de entrega. Prioridade máxima de escala.

**Ad set #2 - [ALE][BEL][HOL]:** CPM de €20,38 vs €7,38 do principal — quase 3× mais caro para o mesmo público. Zero leads. **Pausar imediatamente.**

**Ad set #2- [PS - Cidades x Rico X México]:** €61,37 gastos, 1 lead. Mesmo diagnóstico — está inflacionando o leilão da própria campanha. **Pausar imediatamente.**

---

## Plano de Ação

| Prioridade | Ação | Impacto Esperado | Prazo |
|---|---|---|---|
| 🔴 P1 | **Pausar AD15** ([para unos pocos] novo) na campanha México | Eliminar €61/lead de desperdício; liberar ~€60 de budget para AD10 | Hoje |
| 🔴 P1 | **Pausar ad set #2- [PS - Cidades x Rico X México]** | Reduzir sobreposição de leilão; reduzir CPM do ad set principal | Hoje |
| 🔴 P2 | **Pausar ad set #2 - [ALE][BEL][HOL]** | CPM €20,38 vs €7,38 do principal — eliminar inflação de leilão | Hoje |
| 🔴 P2 | **Investigar AD06**: verificar formulário, landing page e configuração do ad set duplicado | Identificar se é falha técnica (form quebrado) ou de segmentação | Hoje — até 24h |
| 🟡 P3 | **Realocar budget liberado para AD10** (México) e **AD07** (Europa) | Concentrar verba nos dois criativos com 5+ leads e CPL saudável | 24h |
| 🟡 P3 | **Monitorar pacing**: com pausa dos ad sets ineficientes, verificar se projeção mensal sobe para €1.350+ | Corrigir déficit de 14,8% sem precisar aumentar budget total | 48h |
| 🟡 P3 | **Reativar AD06** apenas após confirmação de que o funil está funcionando | Recuperar o segundo melhor criativo da conta (CPL €7,02 na semana anterior) | 48–72h |
| 🟢 P4 | **Testar novo criativo** para substituir AD15 na campanha México — aprendizado: o conceito "para unos pocos" não converteu com este formato | Diversificar mix criativo com base no aprendizado do AD10 | Próxima semana |

---

## BLOCO TRELLO

```
Meta Ads — Leblon Real Estate | 13/08/2026
Gasto: €298,28 | Leads: 17 | CPL: €17,55
Variação vs semana anterior: CPL +71,1% 🔴 | Leads -39,3% 🔴
Pacing: 🟡 LENTO — Projeção €1.278 vs Budget €1.500 (41,9% do mês decorrido)
```

---

📌 **CONTEXTO DA SEMANA**
A campanha México ativou um novo criativo (AD15) que consumiu €61,37 com apenas 1 lead, desviando budget do AD10 (o melhor criativo da conta). Paralelamente, o AD06 — que era o segundo melhor criativo da conta na semana passada com CPL €7,02 — colapsou completamente, passando de 6 leads para 0, com CPM quase dobrando. Esses dois eventos simultâneos são a causa direta da piora de 71% no CPL semanal.

---

📊 **PANORAMA DA SEMANA**

🔍 **Campanhas & Anúncios**
Duas campanhas ativas: México (€157,75, 9 leads) e Europa (€140,53, 8 leads) — CPLs praticamente idênticos e ambos em zona de atenção (€17,53 e €17,57). Na Europa, o AD07 segura a campanha sozinho com 8 leads e CPL €16,41, enquanto o AD06 travou. No México, o AD10 entregou 8 leads com CPL €12,05, mas o AD15 consumiu 39% do budget sem resultado.

📉 **Causa Raiz do CPL**
O CPM médio da conta praticamente não mudou (€11,24 → €11,19) — o problema não está no custo de audiência. A piora vem de dois fatores internos: (1) o AD15 queimou €61 com 1 lead, puxando o CPL médio da campanha México para cima; (2) o AD06 perdeu toda a conversão na Europa, eliminando os 6 leads mais baratos da conta (CPL médio de €7,02). Juntos, esses dois eventos removeram ~10 leads baratos da semana e adicionaram gasto improdutivo — impacto combinado responsável por praticamente toda a alta de CPL.

⚠️ **Anomalias**
- 🔴 **AD06 ([CPL][EUROPA]):** colapsou de 6 leads → 0 leads; CPM quase dobrou (€10,75 → €20,43). CTR ainda alto (3,06%), então o público clica — o problema está no funil pós-clique. Verificar formulário/landing urgentemente.
- 🔴 **AD15 ([MEXICO]):** €61,37 gastos, 1 lead. CPL de €61,37 — 3,5× a média. Deve ser pausado hoje.
- 🟡 **Ad sets duplicados (#2):** ambos com CPM 2–3× mais caro que os ad sets principais, gerando 0 leads e inflacionando o leilão da própria conta.

📅 **Pacing**
No ritmo atual, agosto encerrará com ~€1.278 dos €1.500 disponíveis — 14,8% abaixo do budget, em status 🟡 LENTO. Com 41,9% do mês decorrido, há espaço para recuperar, mas não aumentando budget às cegas. A ação correta é pausar os ad sets e criativos que desperdiçam budget (AD15, #2-México, #2-Europa) e consolidar o investimento em AD10 e AD07, que já provaram conversão. Isso deve melhorar tanto o pacing quanto o CPL ao mesmo tempo.

😴 **Fadiga de Criativos**
Situação geral controlada — AD10 (freq 1,61) e AD07 (freq 1,91) estão em zona verde/monitoramento. AD06 tem frequência 2,20 (zona de atenção), mas o CTR alto indica que o problema não é fadiga — é falha no funil. Nenhum criativo com entrega relevante está em zona de fadiga crítica (>2,5).

🎨 **Criativos**
- **Vencedor principal:** AD10 - [IMG] [PROPRIEDADES PREMIUM] — Cópia — CPL €12,05 com **8 leads** (imagem) — consistente por 2 semanas
- **Candidato a escalar:** AD07 — CPL €16,41 com **8 leads** (Europa) — CPM excepcionalmente baixo no ad set principal (€7,34), potencial alto
- **Para pausar:** AD15 — €61,37 gastos, 1 lead, CPL €61,37 | AD06 — 0 leads após colapso (investigar antes de reativar)
- **Dados insuficientes (aguardar):** AD05, AD010 (ambas as versões)

🎯 **Ad Sets & Públicos**
O ad set principal da Europa ([ALE][BEL][HOL]) tem o CPM mais baixo da conta (€7,38) — excelente eficiência para público europeu, com espaço real para escala. O ad set duplicado (#2) do mesmo público está com CPM €20,38 — quase 3× mais caro — e zero leads, indicando sobreposição de leilão ativa. Pausar os dois ad sets #2 deve reduzir o CPM dos principais e melhorar a eficiência geral imediatamente.

---

🚀 **PRÓXIMOS PASSOS**
- 🔴 **[Hoje] Pausar AD15** ([para unos pocos] novo) na campanha México — eliminar €61/lead de desperdício
- 🔴 **[Hoje] Pausar os dois ad sets #2** (México e Europa) — estão inflacionando o leilão da própria conta sem gerar leads
- 🔴 **[Hoje — até 24h] Investigar AD06**: checar formulário, landing page e configuração do ad set duplicado de Europa — se o funil estiver íntegro, reativar em ad set limpo
- 🟡 **[24h] Realocar budget liberado** para AD10 (México) e AD07 (Europa) — concentrar nos dois criativos com 5+ leads validados
- 🟢 **[Próxima semana] Desenvolver novo criativo** para substituir AD15 na campanha México, usando o perfil do AD10 (imagem, propriedades premium) como referência de formato vencedor