# Relatório Meta Ads — Alcala Homes
**Período atual:** 30/07/2026 a 05/08/2026
**Período anterior:** 23/07/2026 a 29/07/2026
**Gerado em:** 06/08/2026 | **Conta:** act_574789065003576

---

## Resumo Executivo

| Métrica | Atual | Anterior | Variação |
|---|---|---|---|
| Gasto | €91,45 | €131,80 | -30,6% 🔴 |
| Leads | 1 | 10 | -90,0% 🔴 |
| CPL | €91,45 | €13,18 | +593,7% 🔴 |
| CPM Médio | €19,86 | €20,21 | -1,7% 🟢 |
| CTR Médio | 1,17% | 1,41% | -17,0% 🔴 |
| Frequência Média | 1,63 | 1,87 | -12,8% 🟢 |
| Campanhas ativas | 1 | 1 | — |
| Anúncios ativos | 4 | 5 | -1 🟡 |

> ⚠️ **Alerta crítico:** O CPL desta semana (€91,45) é **6,9× superior** à semana anterior (€13,18). Com apenas 1 lead em €91,45 de gasto, a conta está em situação crítica de eficiência. O desaparecimento do anúncio `img5_madri_homes` e a queda abrupta na taxa de conversão de `img2_flats_in_madrid` são os principais fatores.

---

## Módulo 1 — Auditoria de Campanhas e Anúncios

### Campanhas

| Campanha | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| [Data Know] [Form Meta Lead] [Bélgica+Hol+Reino Unido] - 26/06/26 | €91,45 | 1 | €91,45 | 1,17% | €19,86 | 1,63 | 🔴 CRÍTICO |

> **Nota:** CPL de €91,45 supera em **6,9× o CPL médio da semana anterior** (€13,18), ultrapassando amplamente o threshold de 2× para status CRÍTICO.

---

### Anúncios por Campanha — [Data Know] [Form Meta Lead] [Bélgica+Hol+Reino Unido]

*(Ordenados por CPL — sem leads aparecem ao final)*

| Anúncio | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| img2_flats_in_madrid | €56,26 | 1 | €56,26 | 1,12% | €17,54 | 1,47 | 🔴 CRÍTICO |
| img4_luxury_living_madrid | €26,35 | 0 | — | 1,35% | €23,70 | 1,38 | 🔴 CRÍTICO¹ |
| img3_invest_your_wealth | €7,18 | 0 | — | 1,24% | €29,67 | 1,27 | 🔴 CRÍTICO¹ |
| img1_looking_for_a_luxury | €1,66 | 0 | — | 0,00% | €38,60 | 1,19 | 🔴 CRÍTICO² |

> ¹ Gasto acima de €15 com 0 leads → threshold CRÍTICO atingido.
> ² Gasto abaixo de €3 — dados insuficientes para decisão, mas CPM de €38,60 e CTR 0,00% são sinais de alerta.
> ⚠️ **`img5_madri_homes` ausente nesta semana** — presente na semana anterior com 1 lead a €7,55 CPL. Verificar se foi pausado manualmente ou excluído do ad set.

---

## Módulo 2 — Diagnóstico de CPL (Causa Raiz)

### Campanha: [Data Know] [Form Meta Lead] [Bélgica+Hol+Reino Unido]

**CPL: €13,18 → €91,45 (+593,7%)**

A causa raiz **não é o CPM** — o CPM praticamente não se alterou (€20,21 → €19,86, queda de 1,7%). O problema está na **quebra da taxa de conversão pós-clique**.

| Fator | Semana Anterior | Semana Atual | Impacto |
|---|---|---|---|
| CPM | €20,21 | €19,86 | ✅ Estável — não é a causa |
| CTR | 1,41% | 1,17% | 🟡 Queda de 17% — contribui parcialmente |
| Leads gerados | 10 | 1 | 🔴 Causa principal |
| Taxa conv. clique→lead (estimada) | ~0,54% | ~0,07% | 🔴 Queda de ~87% |

**Análise detalhada por anúncio:**

- **`img2_flats_in_madrid`** foi o principal gerador na semana anterior (6 leads a €13,52 CPL). Nesta semana, com €56,26 gastos, gerou apenas 1 lead (CPL €56,26). O CTR subiu levemente (1,05% → 1,12%), indicando que o criativo ainda atrai cliques — mas algo **quebrou na conversão pós-clique**: possível problema no formulário nativo, saturação da oferta para o público ou mudança no algoritmo de entrega.

- **`img4_luxury_living_madrid`** teve €26,35 gastos com 0 leads. Na semana anterior gerava leads a €18,07 com CTR de 2,15% — o CTR desta semana caiu para 1,35%, sugerindo perda de relevância ou rotação desfavorável dentro do Advantage+.

- **`img5_madri_homes`** desapareceu dos dados atuais. Era o anúncio com melhor CTR da semana anterior (2,37%) e CPL de €7,55. A ausência dele **remove o criativo mais eficiente da conta**.

- **`img3_invest_your_wealth`** tem CPM cronicamente alto (€29,67 vs média de €19,86), indicando que este criativo enfrenta menos interesse do público — algoritmo entrega menos e cobra mais caro.

**Hipótese principal:** Combinação de (1) ausência do melhor criativo (`img5`), (2) quebra de conversão do criativo âncora (`img2`) e (3) orçamento concentrado em anúncios sem retorno (`img4` com €26,35 e 0 leads).

---

## Módulo 3 — Detecção de Anomalias

| Tipo | Anúncio | Variação | Ação Recomendada |
|---|---|---|---|
| 🔴 Desaparecimento de criativo | img5_madri_homes | Presente semana anterior (1 lead, CPL €7,55) → ausente nesta semana | Verificar urgentemente se foi pausado/excluído — era o melhor CTR da conta (2,37%) |
| 🔴 Colapso de conversão | img2_flats_in_madrid | CPL €13,52 → €56,26 (+316%) com gasto similar | Verificar formulário nativo Meta, landing/form preview, e rotação Advantage+ |
| 🔴 CPM anômalo alto | img1_looking_for_a_luxury | CPM €38,60 vs média da conta €19,86 (+94%) | Monitorar — gasto baixo (€1,66), mas sinal negativo de relevância; CTR 0,00% |
| 🔴 Gasto sem conversão | img4_luxury_living_madrid | €26,35 gastos, 0 leads (semana anterior: 2 leads) | Pausar ou limitar budget enquanto investiga |
| 🔴 Gasto sem conversão | img3_invest_your_wealth | €7,18 gastos, 0 leads (semana anterior: 1 lead a €6,63) | Monitorar — gasto ainda baixo, mas CPM alto persiste |
| 🟡 Queda de CTR conta | Conta geral | CTR 1,41% → 1,17% (-17%) com CPM estável | Criativos perdendo relevância — renovar copies e testar novos formatos |

---

## Módulo 4 — Pacing Monitor

| Parâmetro | Valor |
|---|---|
| Dia do mês | 6 de 31 (19,4% decorrido) |
| Gasto até agora (agosto) | €91,45 |
| Projeção mensal (ritmo atual) | €391,93 |
| Budget mensal estimado | €600,00 |
| Diferença projeção vs budget | -€208,07 (-34,7%) |
| Status | 🟡 LENTO |

> **Interpretação:** No ritmo atual, agosto encerrará com €391,93 de €600 aproveitados — apenas **65,3% do budget**. A principal causa é a ineficiência extrema desta semana: €91,45 gastos para apenas 1 lead faz o algoritmo possivelmente reduzir a entrega por sinais de baixa conversão. Se o budget diário não for ajustado e a conversão não for restaurada, o mês terminará com budget subutilizado **e** CPL elevado — o pior cenário possível.
>
> **Ação necessária:** Antes de aumentar ritmo de gasto, resolver a causa raiz da queda de conversão. Aumentar budget com CPL em €91,45 apenas acelerará o desperdício.

---

## Módulo 5 — Fadiga de Criativos

| Anúncio | Freq Atual | Freq Anterior | CTR | Leads | Status | Recomendação |
|---|---|---|---|---|---|---|
| img2_flats_in_madrid | 1,47 | 1,76 | 1,12% | 1 | 🟢 OK | Sem fadiga — problema está na conversão, não na frequência |
| img4_luxury_living_madrid | 1,38 | 1,42 | 1,35% | 0 | 🟢 OK | Sem fadiga — problema de relevância ou oferta, não frequência |
| img3_invest_your_wealth | 1,27 | 1,25 | 1,24% | 0 | 🟢 OK | Sem fadiga — CPM alto é o problema estrutural |
| img1_looking_for_a_luxury | 1,19 | 1,07 | 0,00% | 0 | 🟢 OK | Sem fadiga — mas CTR 0% é alerta de relevância |

> **Conclusão:** Fadiga de criativos **não é o problema desta semana**. Todas as frequências estão abaixo de 1,8 (threshold de monitoramento). O CPM estável confirma que não há saturação de público. O problema é de **conversão e eficiência dos criativos**, não de repetição excessiva.

---

## Módulo 6 — Análise de Copy e Criativos

### 🏆 Criativos Vencedores

> ⚠️ **Regra aplicada:** Nenhum criativo atingiu o mínimo de 5 leads nesta semana. Análise baseada em histórico acumulado (semanas atual + anterior).

**Melhor desempenho histórico (2 semanas):**

| Anúncio | Leads Totais | CPL Médio | Gasto Total | Avaliação |
|---|---|---|---|---|
| img2_flats_in_madrid | 7 (6 ant. + 1 atual) | ~€19,67 | €137,37 | Único com volume suficiente — mas com anomalia de conversão esta semana ⚠️ |
| img4_luxury_living_madrid | 2 (apenas anterior) | €18,07 | €62,50 | Estatisticamente cedo para conclusão |
| img5_madri_homes | 1 (apenas anterior) | €7,55 | €7,55 | Estatisticamente cedo — mas melhor CTR (2,37%) e CPL da conta. **Verificar urgente** |

**`img2_flats_in_madrid`** é o único com volume suficiente para análise, mas está marcado como anomalia no Módulo 3 (colapso de conversão esta semana). **Não recomendado para escalar até que a causa raiz seja investigada.**

### ⛔ Criativos para Pausar / Revisar

| Anúncio | Motivo |
|---|---|
| img4_luxury_living_madrid | €26,35 gastos com 0 leads nesta semana; marcado como anomalia no Módulo 3 — pausar ou reduzir budget enquanto investiga conversão |
| img1_looking_for_a_luxury | CTR 0,00% nesta semana, CPM €38,60 (94% acima da média da conta) — sem nenhuma tração; pausar |

### 📋 Dados Insuficientes (aguardar)

- `img3_invest_your_wealth` — CPM cronicamente alto, mas gasto ainda abaixo de €15 agregado; monitorar mais 3-5 dias antes de decisão
- `img5_madri_homes` — ausente nesta semana; verificar status antes de qualquer análise

---

## Módulo 7 — Análise de Ad Sets e Públicos

| Ad Set | Campanha | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|---|
| 01/Advantage + Compradores | [Data Know] [Form Meta Lead] [Bélgica+Hol+Reino Unido] | €91,45 | 1 | €91,45 | 1,17% | €19,86 | 1,63 | 🔴 CRÍTICO |

**Observações:**

- **Sobreposição de público:** Não há risco de sobreposição — apenas 1 ad set ativo.
- **Advantage+ Compradores:** O uso de Advantage+ Audience é positivo para escala, mas nesta semana o algoritmo parece estar entregando para segmentos com menor intenção de conversão. Com apenas 1 lead de sinal positivo recente, o algoritmo tem pouco dado para otimizar.
- **CPM (€19,86):** Está estável e dentro da normalidade para o público de Bélgica + Holanda + Reino Unido (mercado imobiliário de luxo internacional). Não é o gargalo.
- **Frequência (1,63):** Saudável — sem saturação do público. Há espaço para escala quando a conversão for restabelecida.
- **Risco:** Com apenas 1 sinal de conversão nesta semana, o Advantage+ pode entrar em modo de "reaprendizado" e piorar a entrega temporariamente. Qualquer mudança significativa no ad set deve ser feita com cautela.

---

## Plano de Ação

| Prioridade | Ação | Impacto | Prazo |
|---|---|---|---|
| 🔴 P1 | **Verificar e reativar `img5_madri_homes`** — melhor CTR (2,37%) e CPL (€7,55) da conta; ausência sem explicação é perda direta de eficiência | Alto — pode restaurar leads rapidamente | Hoje (06/08) |
| 🔴 P2 | **Auditar formulário nativo do `img2_flats_in_madrid`** — verificar preview do form, campos obrigatórios, mensagem de confirmação; CPL explodiu de €13,52 para €56,26 sem mudança de CPM | Alto — esse anúncio era responsável por 60% dos leads | Hoje (06/08) |
| 🔴 P3 | **Pausar `img1_looking_for_a_luxury`** — CTR 0,00%, CPM €38,60 (2× a média), 0 leads; consumindo budget sem retorno | Médio — libera €1-2/dia para anúncios mais eficientes | Hoje (06/08) |
| 🟡 P4 | **Pausar ou limitar budget de `img4_luxury_living_madrid`** — €26,35 com 0 leads nesta semana; anomalia confirmada no Módulo 3 | Médio — evita desperdício adicional enquanto investiga | Amanhã (07/08) |
| 🟡 P5 | **Criar 2-3 novos criativos para testar** — variações de copy de `img2` e `img5`; conta depende de 1-2 anúncios sem backup saudável | Alto (longo prazo) — reduz risco de dependência | 48-72h |
| 🟢 P6 | **NÃO aumentar budget diário agora** — pacing está lento (🟡), mas aumentar gasto com CPL em €91,45 só amplifica o problema; restaurar conversão primeiro | Preventivo | Aguardar resolução do P2 |

---

## BLOCO TRELLO

---

**Meta Ads Alcala Homes — 06/08/2026**
**Gasto:** €91,45 | **Leads:** 1 | **CPL:** €91,45
**Variação vs semana anterior:** CPL +593,7% 🔴 | Leads -90,0% 🔴
**Pacing:** 🟡 LENTO — Projeção €391,93 vs Budget €600,00 (19,4% do mês decorrido)

---

📌 **CONTEXTO DA SEMANA**
O anúncio `img5_madri_homes`, que na semana anterior apresentou o melhor CTR da conta (2,37%) e CPL de €7,55, desapareceu completamente dos dados desta semana sem explicação aparente. Simultaneamente, o anúncio principal `img2_flats_in_madrid` — responsável por 60% dos leads históricos — sofreu um colapso de conversão severo: mesmos níveis de gasto (€56 vs €81), mas apenas 1 lead ao invés de 6. Esses dois eventos combinados explicam praticamente toda a queda da semana.

---

📊 **PANORAMA DA SEMANA**

🔍 **Campanhas & Anúncios**
Apenas 1 campanha ativa (Bélgica + Holanda + Reino Unido) com 1 ad set Advantage+. Dos 4 anúncios em circulação, apenas `img2_flats_in_madrid` gerou algum resultado (1 lead a €56,26 CPL). Os outros 3 consumiram €35,19 combinados sem gerar nenhum lead — com destaque negativo para `img4_luxury_living_madrid` (€26,35 gastos, 0 leads) e `img1_looking_for_a_luxury` (CTR 0,00%, CPM €38,60).

📉 **Causa Raiz do CPL**
O CPM está estável (€19,86 vs €20,21) — não é o problema. O colapso vem da **quebra na taxa de conversão pós-clique**: estimativa de conversão clique→lead caiu de ~0,54% para ~0,07%, uma queda de 87%. As causas mais prováveis são: (1) problema técnico no formulário nativo do Meta para `img2`, (2) ausência do criativo mais eficiente (`img5`) que removia leads de baixo custo da média, e (3) budget mal distribuído pelo Advantage+ concentrando em `img4` sem retorno. O CTR da conta caindo 17% (1,41% → 1,17%) com CPM estável sugere também leve perda de relevância criativa.

⚠️ **Anomalias**
- 🔴 `img5_madri_homes` desapareceu — melhor CTR (2,37%) e CPL (€7,55) da conta; verificar se foi pausado ou excluído
- 🔴 `img2_flats_in_madrid`: CPL saltou de €13,52 para €56,26 (+316%) sem mudança de CPM — suspeita de problema no formulário
- 🔴 `img4_luxury_living_madrid`: €26,35 gastos, 0 leads (era €18,07 CPL na semana anterior)
- 🔴 `img1_looking_for_a_luxury`: CPM €38,60 (94% acima da média), CTR 0,00% — sem nenhuma tração

📅 **Pacing**
No ritmo atual, agosto encerrará com €391,93 de €600 aproveitados — apenas 65,3% do budget. A causa não é budget diário baixo, mas a ineficiência extrema: com CPL em €91,45, o algoritmo Meta recebe poucos sinais positivos de conversão e tende a reduzir naturalmente a entrega. **Atenção:** a ação correta aqui não é aumentar o budget diário — aumentar gasto agora apenas desperdiçaria mais verba com CPL tóxico. A prioridade é restaurar a conversão primeiro (investigar formulário, reativar `img5`), e só então avaliar aumento de ritmo.

😴 **Fadiga de Criativos**
Sem fadiga em nenhum criativo — todas as frequências abaixo de 1,63. O público de Bélgica + Holanda + Reino Unido ainda tem espaço saudável para ser explorado. O problema desta semana é de eficiência criativa e conversão, não de saturação de audiência.

🎨 **Criativos**
- **Vencedor histórico (único com volume):** `img2_flats_in_madrid` — 7 leads acumulados em 2 semanas, mas com anomalia crítica de conversão nesta semana; **não escalar até investigar formulário**
- **Candidato prioritário a reativar:** `img5_madri_homes` — CPL €7,55 e CTR 2,37% na semana anterior; estatisticamente cedo (1 lead), mas sinais promissores; verificar urgente
- **Para pausar:** `img1_looking_for_a_luxury` (CTR 0%, CPM 2× a média) e `img4_luxury_living_madrid` (€26,35 com 0 leads, anomalia confirmada)
- **Dados insuficientes (aguardar):** `img3_invest_your_wealth`

🎯 **Ad Sets & Públicos**
CPM estável em €19,86 para Advantage+ Compradores — público saudável e sem saturação (frequência 1,63). Não há sobreposição (1 único ad set). Com apenas 1 conversão nesta semana, o algoritmo Advantage+ tem sinal fraco para otimizar — restaurar conversão rapidamente é crítico para evitar que o ad set entre em modo de reaprendizado prolongado.

---

🚀 **PRÓXIMOS PASSOS**
- 🔴 **[Hoje] Verificar e reativar `img5_madri_homes`** — ausência injustificada do melhor criativo da conta
- 🔴 **[Hoje] Auditar formulário nativo de `img2_flats_in_madrid`** — abrir o form preview no Meta Ads Manager e testar submissão; CPL 4× maior sem mudança de CPM aponta para problema técnico
- 🔴 **[Hoje] Pausar `img1_looking_for_a_luxury`** — CTR 0,00%, CPM €38,60, 0 leads; liberação de budget para criativos eficientes
- 🟡 **[Amanhã] Pausar ou limitar `img4_luxury_living_madrid`** — €26,35 com 0 leads; redirecionar verba para `img2` e `img5` após confirmar formulário funcionando
- 🟢 **[48-72h] Desenvolver 2-3 novos criativos** — variações de `img2` e `img5` para reduzir dependência de criativos únicos e dar mais opções ao Advantage+

---