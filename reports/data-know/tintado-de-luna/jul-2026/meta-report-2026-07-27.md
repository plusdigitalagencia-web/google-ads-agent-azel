# Relatório Meta Ads - Tintado de Luna
**Período atual:** 20/07/2026 a 26/07/2026
**Período anterior:** 13/07/2026 a 19/07/2026
**Gerado em:** 27/07/2026 | **Conta:** act_9709425065783957

---

## Resumo Executivo

| Métrica | Atual | Anterior | Variação |
|---|---|---|---|
| Gasto | €0,00 | €0,00 | — |
| Leads | 0 | 0 | — |
| CPL | — | — | — |
| CPM Médio | — | — | — |
| CTR Médio | — | — | — |
| Frequência Média | — | — | — |

> ⚠️ **Atenção:** Nenhuma dado de campanha foi encontrado para o período analisado. A conta não registrou gasto, impressões, cliques nem leads nas duas semanas. Todas as análises abaixo refletem esse estado — conta inativa ou sem dados disponíveis via API.

---

## Módulo 1 - Auditoria de Campanhas e Anúncios

### Campanhas

| Campanha | Status | Gasto | Leads | CPL | Observação |
|---|---|---|---|---|---|
| — | — | — | — | — | Nenhuma campanha ativa detectada |

### Anúncios por Campanha

| Anúncio | Campanha | Gasto | Leads | CPL | CTR | Status |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | Nenhum anúncio encontrado |

> 🔴 **CRÍTICO:** Zero campanhas e zero anúncios retornados pela API para ambos os períodos. A conta aparenta estar completamente pausada ou houve falha na coleta de dados.

---

## Módulo 2 - Diagnóstico de CPL (Causa Raiz)

**Diagnóstico impossível — sem dados de veiculação.**

Sem impressões, cliques ou conversões registradas, não é possível identificar causa raiz de variação de CPL. As hipóteses a investigar manualmente são:

- **Conta pausada:** todas as campanhas podem ter sido pausadas manualmente ou por política do Meta (pagamento, violação de política, limite de gasto).
- **Falha na coleta via API:** o token de acesso pode ter expirado ou a permissão de leitura da conta foi revogada.
- **Budget esgotado:** se havia um budget mensal configurado, pode ter sido atingido antes do período analisado.
- **Campanha em rascunho:** anúncios criados mas nunca publicados não aparecem nos dados de veiculação.

---

## Módulo 3 - Detecção de Anomalias

| Tipo | Elemento | Variação | Ação Recomendada |
|---|---|---|---|
| 🔴 Conta sem veiculação | Conta inteira | 100% do gasto zerado | Verificar status da conta no Business Manager imediatamente |
| 🔴 Zero leads — período inteiro | Todos os anúncios | 0 leads na semana atual e anterior | Confirmar se campanhas existem e estão ativas |
| ⚠️ Dados ausentes na API | act_9709425065783957 | Nenhum objeto retornado | Validar token de acesso e permissões da conta |

---

## Módulo 4 - Pacing Monitor

| Indicador | Valor |
|---|---|
| Dia do mês | 27 de 31 |
| % do mês decorrido | 87,1% |
| Gasto acumulado no mês | €0,00 |
| Projeção mensal | €0,00 |
| Budget mensal estimado | Não configurado |
| Status | 🔴 SEM VEICULAÇÃO |

> 🔴 **CRÍTICO:** Com 87,1% do mês já decorrido e €0 gastos, o budget de julho não está sendo utilizado. Se a conta deveria estar ativa, cada dia de inatividade representa oportunidade de geração de leads perdida e não recuperável no mês corrente.

---

## Módulo 5 - Fadiga de Criativos

| Anúncio | Frequência | CTR | Leads | Status | Recomendação |
|---|---|---|---|---|---|
| — | — | — | — | — | Sem dados de veiculação |

> Sem impressões registradas, não há frequência a monitorar. O risco de fadiga é irrelevante enquanto a conta não estiver veiculando.

---

## Módulo 6 - Análise de Copy e Criativos

**Criativo vencedor:** Não identificável — nenhum anúncio veiculou no período.

**Criativos para pausar:** N/A — sem dados.

**Criativos para escalar:** N/A — sem dados.

> ⚠️ Regra aplicada: sem mínimo de 5 leads em qualquer criativo, nenhum vencedor pode ser declarado. Quando a conta voltar a veicular, aguardar acúmulo de dados antes de qualquer decisão de escala.

---

## Módulo 7 - Análise de Ad Sets e Públicos

| Ad Set | Campanha | Gasto | Leads | CPM | Frequência | Status |
|---|---|---|---|---|---|---|
| — | — | — | — | — | — | Nenhum ad set encontrado |

> Sem ad sets ativos, não há análise de sobreposição de públicos, saturação ou performance por segmentação possível.

---

## Plano de Ação

| Prioridade | Ação | Impacto | Prazo |
|---|---|---|---|
| 🔴 P1 | Acessar o Meta Business Manager e verificar o status real da conta act_9709425065783957 — se há campanhas pausadas, bloqueio de conta ou limite de gasto atingido | Alto — desbloqueia toda a veiculação | Hoje |
| 🔴 P2 | Verificar se o token de acesso da API ainda é válido e se as permissões `ads_read` e `ads_management` estão ativas para a conta | Alto — pode ser falha de coleta, não de veiculação | Hoje |
| 🔴 P3 | Confirmar método de pagamento da conta — conta bloqueada por pagamento recusado é a causa mais comum de parada total | Alto — se for pagamento, resolução imediata reativa a conta | Hoje |
| 🟡 P4 | Se a conta estiver OK e os dados ausentes forem falha de API, reprocessar a coleta para o período 20–26/07 e regenerar o relatório com dados reais | Médio — garante visibilidade correta | 24h |
| 🟢 P5 | Definir e registrar o budget mensal no sistema de relatórios — o campo `budget_monthly` está zerado, impedindo cálculo correto de pacing | Baixo — melhoria de processo | Esta semana |

---

## BLOCO TRELLO

```
Meta Ads Tintado de Luna - 27/07/2026
Gasto: €0 | Leads: 0 | CPL: —
Variação vs semana anterior: sem dados em ambas as semanas ⚠️
Pacing: 🔴 SEM VEICULAÇÃO — €0 gastos com 87,1% do mês decorrido
```

---

📌 **CONTEXTO DA SEMANA**
A conta Tintado de Luna não registrou absolutamente nenhuma atividade nas últimas duas semanas — nem na semana atual (20–26/07) nem na anterior (13–19/07). Os dados retornados pela API estão completamente zerados: zero campanhas, zero ad sets, zero anúncios, zero gasto e zero leads. Isso representa um cenário crítico que exige verificação imediata antes de qualquer análise de performance ser possível.

---

📊 **PANORAMA DA SEMANA**

🔍 **Campanhas & Anúncios**
Nenhuma campanha foi retornada pela API para o período 20/07 a 26/07. O mesmo ocorre para o período anterior (13–19/07). Não há anúncios ativos, pausados ou em rascunho visíveis nos dados coletados. A conta está efetivamente "em silêncio" — sem nenhuma veiculação detectável.

📉 **Causa Raiz do CPL**
Não há CPL a analisar, mas há três causas prováveis para o silêncio total da conta que devem ser investigadas em ordem: **(1)** problema de pagamento — causa mais comum de parada abrupta no Meta, com bloqueio automático da conta; **(2)** campanhas pausadas manualmente — seja por decisão interna ou por política do Meta (anúncio reprovado); **(3)** falha na integração da API — token expirado ou permissões revogadas, onde a conta pode estar ativa mas os dados não chegam ao sistema de relatórios. Até confirmar qual das três é a causa real, nenhuma análise de performance é possível.

⚠️ **Anomalias**
- 🔴 Conta inteira sem veiculação por pelo menos 14 dias consecutivos
- 🔴 Zero leads gerados em duas semanas — impacto direto no pipeline de vendas
- 🔴 Campo `budget_monthly` zerado no sistema — pacing impossível de calcular com precisão
- ⚠️ Token de API potencialmente inválido ou com permissões insuficientes

📅 **Pacing**
Com 87,1% de julho já decorrido e €0 gastos na conta, o mês de julho encerrará com aproveitamento zero do budget — independentemente de qual seja o valor planejado. Os últimos 4 dias do mês (28–31/07) não são suficientes para recuperar um mês inteiro de inatividade. A ação imediata é reativar a conta hoje e entender se o budget não utilizado em julho pode ser redistribuído para agosto, ou se é necessário compensar com budget maior no próximo mês para manter a meta de leads.

😴 **Fadiga de Criativos**
Irrelevante no momento — sem impressões, não há frequência acumulada. Paradoxalmente, se a conta retomar a veiculação com os mesmos criativos do período anterior, o histórico de frequência pode estar "zerado" pelo hiato, o que pode beneficiar a entrega inicial.

🎨 **Criativos**
- **Vencedor principal:** Não identificável — sem dados de veiculação
- **Para pausar:** N/A
- **Dados insuficientes:** Todos os criativos da conta — aguardar reativação e acúmulo mínimo de dados (5+ leads por criativo) antes de qualquer decisão

🎯 **Ad Sets & Públicos**
Sem ad sets ativos detectados. Quando a conta for reativada, revisar segmentações — após período de inatividade, o algoritmo do Meta precisa de fase de reaprendizado (tipicamente 3–7 dias) antes de atingir performance estável. Evitar alterações nos ad sets durante essa fase.

---

🚀 **PRÓXIMOS PASSOS**
- 🔴 **[HOJE — urgente]** Acessar o Meta Business Manager e verificar status da conta: pagamento, políticas e campanhas pausadas
- 🔴 **[HOJE]** Validar token de API e permissões da conta — confirmar se o problema é de veiculação real ou de coleta de dados
- 🟡 **[24h]** Se a conta for reativada, configurar budget diário adequado para os últimos dias de julho e já planejar agosto com budget compensatório
- 🟡 **[24–48h]** Registrar budget mensal no sistema de relatórios para habilitar cálculo correto de pacing nas próximas semanas
- 🟢 **[Esta semana]** Após reativação, monitorar diariamente nos primeiros 3–5 dias para confirmar que o algoritmo entrou em fase de aprendizado e os leads começaram a chegar