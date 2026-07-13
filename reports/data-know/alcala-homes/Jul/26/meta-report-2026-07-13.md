# Relatório Meta Ads - Alcala Homes
**Período atual:** 06/07/2026 a 12/07/2026
**Período anterior:** 29/06/2026 a 05/07/2026
**Gerado em:** 13/07/2026 | **Conta:** act\_574789065003576

---

> ⚠️ **ALERTA GERAL:** Nenhum dado de campanha, anúncio ou ad set foi encontrado nos dois períodos analisados. Gasto €0, leads 0, nenhuma campanha ativa. O relatório documenta o estado atual e orienta as ações de reativação.

---

## Resumo Executivo

| Métrica | Atual (06–12/07) | Anterior (29/06–05/07) | Variação |
|---|---|---|---|
| Gasto total | €0,00 | €0,00 | — |
| Leads | 0 | 0 | — |
| CPL médio | — | — | — |
| CPM médio | — | — | — |
| CTR médio | — | — | — |
| Frequência média | — | — | — |
| Campanhas ativas | 0 | 0 | — |
| Anúncios ativos | 0 | 0 | — |

> Não há variação calculável pois ambos os períodos registram atividade zero. A conta está inativa há pelo menos 14 dias consecutivos.

---

## Módulo 1 - Auditoria de Campanhas e Anúncios

### Campanhas

| Campanha | Status | Gasto | Leads | CPL | Observação |
|---|---|---|---|---|---|
| *(nenhuma campanha encontrada)* | — | — | — | — | Conta sem campanhas ativas |

### Anúncios por Campanha

| Anúncio | Status | Gasto | Leads | CPL | CTR | CPM | Freq. |
|---|---|---|---|---|---|---|---|
| *(nenhum anúncio encontrado)* | — | — | — | — | — | — | — |

> **Diagnóstico:** A API retornou arrays vazios para `campaigns_current`, `ad_sets_current` e `ads_current`. Isso indica que todas as campanhas estão pausadas, excluídas ou que nenhuma campanha foi criada ainda nesta conta no período analisado.

---

## Módulo 2 - Diagnóstico de CPL (Causa Raiz)

**Causa raiz identificada: Conta completamente inativa.**

Não há dados de entrega para diagnosticar CPM, CTR ou frequência. As hipóteses ordenadas por probabilidade são:

1. **🔴 Campanhas pausadas manualmente** — situação mais comum quando toda a conta para abruptamente. Verificar se houve decisão de pausa intencional pelo gestor ou cliente.
2. **🔴 Problema de pagamento / limite de crédito** — contas com cartão recusado ou limite atingido são pausadas automaticamente pelo Meta. Verificar em *Configurações de Pagamento* da conta `act_574789065003576`.
3. **🟡 Campanhas em revisão ou rejeitadas** — anúncios recusados pela política do Meta podem bloquear toda a campanha. Verificar aba *Qualidade da Conta* no Gerenciador de Anúncios.
4. **🟡 Período de estruturação** — a conta pode estar em fase de setup com campanhas ainda não publicadas.

> **Com €0 gasto e 42% do mês decorrido (dia 13 de 31), o budget mensal de €600 está inteiramente em risco de não ser utilizado.**

---

## Módulo 3 - Detecção de Anomalias

| Tipo | Elemento | Detalhe | Ação Recomendada |
|---|---|---|---|
| 🔴 CRÍTICO | Conta inteira | Gasto €0 — conta inativa por ≥14 dias consecutivos | Identificar causa e reativar imediatamente |
| 🔴 CRÍTICO | Pacing | 0% do budget executado com 41,9% do mês decorrido | Reativar campanhas ou realocar budget |
| 🟡 ATENÇÃO | Dados históricos | Semana anterior também zerada — padrão sugere pausa prolongada | Auditar histórico da conta (últimas 4 semanas) |

---

## Módulo 4 - Pacing Monitor

**Dia 13 de 31 do mês | 41,9% do período decorrido**

| Métrica | Valor |
|---|---|
| Gasto acumulado no mês | €0,00 |
| Projeção mensal (ritmo atual) | €0,00 |
| Budget mensal estimado | €600,00 |
| Diferença projeção vs budget | -€600,00 (-100%) |
| Status | 🔴 ACELERADO INVERSO — conta parada |

> **Interpretação:** Com 41,9% do mês consumido e €0 gasto, a projeção ao ritmo atual é de €0 no mês — 100% abaixo do budget de €600. Cada dia adicional de inatividade reduz a janela disponível para recuperar o volume de leads planejado para julho. **Reativação hoje ainda permite aproveitar ~58% do mês (≈18 dias)**, o que tornaria necessário um ritmo diário de €33,33/dia para executar o budget integralmente — €4,76/dia acima do ritmo normal de €19,35/dia. Avaliar se é viável ou se o budget de julho deve ser ajustado.

---

## Módulo 5 - Fadiga de Criativos

| Anúncio | Freq. | CTR | Leads | Status | Recomendação |
|---|---|---|---|---|---|
| *(nenhum dado disponível)* | — | — | — | — | Aguardar reativação da conta |

> Sem entrega ativa, não há métricas de frequência para analisar. Ao reativar, monitorar frequência a partir do 3.º dia — especialmente se os criativos anteriores já estavam rodando antes da pausa (público pode já ter visto os anúncios anteriormente, acelerando fadiga).

---

## Módulo 6 - Análise de Copy e Criativos

**Criativo Vencedor:** Não aplicável — nenhum anúncio com dados no período.

**Regra aplicada:** Para ser considerado vencedor, o criativo precisa de mínimo 5 leads. Sem entrega, nenhum criativo pode ser avaliado.

**Recomendações para reativação:**
- Verificar se há criativos aprovados e prontos para veicular na conta
- Priorizar criativos que historicamente geraram CPL abaixo da média da conta (necessário buscar dados de períodos anteriores a 29/06)
- Se não houver histórico de referência, lançar com 2–3 variações de copy/visual para gerar aprendizado rápido
- Evitar lançar apenas 1 criativo único — sem variação, não há como identificar o vencedor

---

## Módulo 7 - Análise de Ad Sets e Públicos

| Ad Set | Gasto | Leads | CPL | CPM | CTR | Freq. | Status |
|---|---|---|---|---|---|---|---|
| *(nenhum ad set encontrado)* | — | — | — | — | — | — | — |

> **Observação sobre públicos:** Sem dados ativos, não há análise de sobreposição possível. Ao reativar, garantir que os ad sets não competem entre si pelo mesmo público (especialmente relevante se houver segmentações por interesse + lookalike rodando simultaneamente na mesma conta). Considerar uso de *Audience Overlap Tool* antes de publicar.

---

## Plano de Ação

| Prioridade | Ação | Impacto | Prazo |
|---|---|---|---|
| 🔴 1 | Verificar status de pagamento da conta `act_574789065003576` — cartão, limite de crédito e faturas pendentes | Desbloqueia toda a conta | **Hoje (13/07)** |
| 🔴 2 | Auditar campanhas pausadas no Gerenciador de Anúncios — verificar motivo da pausa (manual, rejeição de anúncio, limite de gasto) | Identifica causa raiz real | **Hoje (13/07)** |
| 🔴 3 | Reativar campanhas existentes OU criar nova estrutura se não houver campanhas prontas | Retoma geração de leads | **Hoje (13/07)** |
| 🟡 4 | Ajustar expectativa de budget: com 18 dias restantes, definir se mantém €600 (ritmo €33/dia) ou reduz o target do mês | Evita underspend ou pressão excessiva no ritmo | **24h** |
| 🟡 5 | Auditar histórico de criativos pré-pausa para identificar os de melhor CPL e priorizar na reativação | Reduz tempo de aprendizado | **24–48h** |
| 🟢 6 | Configurar alerta automático de gasto no Meta Ads Manager (ex: alerta se gasto diário = €0 por 2 dias seguidos) | Previne situação similar no futuro | **Próximos 7 dias** |
| 🟢 7 | Estabelecer dashboard de pacing semanal para garantir que o budget mensal esteja sendo executado no ritmo correto | Gestão proativa de budget | **Próximos 7 dias** |

---

## BLOCO TRELLO

---

**Meta Ads Alcala Homes — 13/07/2026**
Gasto: €0 | Leads: 0 | CPL: —
Variação vs semana anterior: Sem variação calculável — ambas as semanas com gasto €0
Pacing: 🔴 CRÍTICO — Projeção €0 vs Budget €600 (41,9% do mês decorrido, dia 13 de 31)

---

**📌 CONTEXTO DA SEMANA**
A conta `act_574789065003576` está completamente inativa há pelo menos 14 dias consecutivos — tanto a semana atual (06–12/07) quanto a semana anterior (29/06–05/07) registraram gasto €0, 0 leads e nenhuma campanha ou anúncio ativo. A causa da pausa ainda precisa ser confirmada (ver Próximos Passos), mas o impacto é direto: 42% do budget mensal de €600 já foi "perdido" em termos de tempo disponível para veiculação. Com 18 dias restantes em julho, ainda é possível recuperar parte do volume, mas o ritmo diário necessário para executar o budget completo sobe de €19,35/dia para €33,33/dia — o que precisa ser avaliado com o cliente.

---

**📊 PANORAMA DA SEMANA**

**🔍 Campanhas & Anúncios**
Nenhuma campanha, ad set ou anúncio foi encontrado nos dados da semana atual nem da semana anterior. A API retornou arrays completamente vazios para os três níveis da estrutura (campanha, ad set, anúncio). Isso confirma que a conta está sem qualquer atividade de veiculação — seja por pausa manual, problema de pagamento ou ausência de estrutura publicada.

**📉 Causa Raiz do CPL**
O CPL não pode ser calculado pois não houve entrega. A causa raiz do problema não é criativa nem de público — é estrutural: a conta simplesmente não está veiculando. As hipóteses mais prováveis, em ordem de probabilidade, são: (1) campanhas pausadas manualmente sem data de reativação definida; (2) problema de pagamento com bloqueio automático pelo Meta; (3) anúncios rejeitados por violação de política que propagaram a pausa para toda a campanha. A causa precisa ser identificada hoje no Gerenciador de Anúncios antes de qualquer outra ação.

**⚠️ Anomalias**
- 🔴 **Conta inativa ≥14 dias:** Gasto €0 em dois períodos consecutivos — situação anormal que exige ação imediata
- 🔴 **Pacing com déficit de 100%:** 41,9% do mês decorrido com €0 executado dos €600 disponíveis — sem reativação hoje, o underspend de julho é praticamente certo
- 🟡 **Ausência de dados históricos recentes:** Sem duas semanas de dados comparáveis, não é possível avaliar tendência de CPL, fadiga de criativos ou eficiência de públicos

**📅 Pacing**
Dia 13 de 31 — 41,9% do mês consumido. Projeção ao ritmo atual: €0 (vs budget de €600). Para executar o budget integralmente nos 18 dias restantes, seria necessário um ritmo de €33,33/dia — 72% acima do ritmo normal de €19,35/dia. Recomendação: reativar hoje e definir com o cliente se o target de julho é executar os €600 integrais (exige ritmo acelerado) ou ajustar o budget do mês para um valor proporcional ao tempo restante (≈€348 para 18 dias no ritmo normal).

**😴 Fadiga de Criativos**
Não há dados de frequência disponíveis — nenhum anúncio veiculou no período. Atenção ao reativar: se os criativos já haviam sido exibidos antes da pausa, o público pode retomar com frequência acumulada mais alta, acelerando o ponto de fadiga. Monitorar frequência nos primeiros 3 dias pós-reativação.

**🎨 Criativos**
🏆 Vencedor principal: — (sem dados — nenhum criativo com 5+ leads no período)
🥈 Candidato a escalar: — (sem dados)
🔴 Para pausar: — (sem dados)
⏳ Dados insuficientes (aguardar reativação): todos os criativos da conta

**🎯 Ad Sets & Públicos**
Nenhum ad set ativo no período. Sem dados de CPM ou alcance para avaliar espaço de escala ou saturação de público. Ao reativar, verificar sobreposição entre segmentações antes de publicar — especialmente se houver múltiplos ad sets com interesse + lookalike simultâneos.

---

**🚀 PRÓXIMOS PASSOS**
- 🔴 **[HOJE — urgente]** Acessar *Configurações de Pagamento* da conta `act_574789065003576` e verificar se há cartão recusado, limite de crédito atingido ou fatura pendente bloqueando a conta
- 🔴 **[HOJE — urgente]** Auditar o Gerenciador de Anúncios para identificar o motivo exato da pausa (manual? rejeição de anúncio? limite de gasto de campanha atingido?) e reativar imediatamente após identificar a causa
- 🟡 **[24h]** Alinhar com o cliente: manter meta de €600 para julho (ritmo €33/dia nos 18 dias restantes) ou ajustar budget proporcional (≈€348)? Definir expectativa realista de leads para o mês
- 🟡 **[24–48h]** Auditar criativos pré-pausa para priorizar os de melhor CPL histórico na reativação — evitar lançar criativo único sem variação
- 🟢 **[Próximos 7 dias]** Configurar alerta automático no Meta Ads Manager para notificar se o gasto diário zerar por 2 dias consecutivos — prevenir recorrência desta situação sem visibilidade

---