# Relatório Meta Ads - Luxe Icon LTD
**Período atual:** 30/07/2026 a 05/08/2026
**Período anterior:** 23/07/2026 a 29/07/2026
**Gerado em:** 06/08/2026 | **Conta:** act_412122005210742

---

## Resumo Executivo

| Métrica | Atual | Anterior | Variação |
|---|---|---|---|
| Gasto | €387,85 | €310,52 | +€77,33 (+24,9%) 📈 |
| Leads | 36 | 34 | +2 (+5,9%) 📈 |
| CPL | €10,77 | €9,13 | +€1,64 (+18,0%) 🔴 |
| CPM | €10,08 | €9,35 | +€0,73 (+7,8%) 🔴 |
| CTR | 2,76% | 2,23% | +0,53pp (+23,8%) 📈 |
| Frequência | 2,20 | 2,34 | -0,14 (-6,0%) 🟢 |

> **Leitura rápida:** O gasto cresceu 25% mas os leads cresceram apenas 6%, o que explica o CPL +18%. O CTR melhorou — sinal de que os novos criativos de agosto capturam atenção — mas o CPM também subiu, pressionando o custo por lead. A deterioração de Rc1-jun (CPL €8,12 → €21,55) é a principal causa raiz do problema.

---

## Módulo 1 - Auditoria de Campanhas e Anúncios

### Campanhas

| Campanha | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| DK - Leads - Forms - 11/03 | €387,85 | 36 | €10,77 | 2,76% | €10,08 | 2,20 | 🟡 ATENÇÃO |

> CPL médio da conta: €10,77. Threshold 🟡 = > €14,00 | Threshold 🔴 = > €21,54. A campanha está dentro do aceitável no agregado, mas esconde performance muito desigual entre anúncios.

---

### Anúncios por Campanha — DK - Leads - Forms - 11/03
*(ordenados por CPL crescente, anúncios com gasto relevante)*

| Anúncio | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| [RC VIDEO 2] [JULIO] | €158,12 | 25 | €6,32 | 3,54% | €9,53 | 1,52 | 🟢 OK |
| comprar mejor | €33,07 | 2 | €16,54 | 2,84% | €14,47 | 1,48 | 🟡 ATENÇÃO* |
| Rc1-jun | €193,95 | 9 | €21,55 | 2,12% | €10,05 | 1,99 | 🔴 CRÍTICO |
| Rc2-jun | €1,34 | 0 | — | 0,87% | €11,65 | 1,60 | ⚪ INSUFICIENTE |
| [RC VIDEO 1] [JULIO] | €0,66 | 0 | — | 0,00% | €8,35 | 1,22 | ⚪ INSUFICIENTE |
| [RC VIDEO 3] [JULIO] | €0,62 | 0 | — | 0,00% | €6,81 | 1,21 | ⚪ INSUFICIENTE |
| Rc9-jul | €0,09 | 0 | — | 0,00% | €5,62 | 1,00 | ⚪ INSUFICIENTE |

> *comprar mejor: apenas 2 leads, CPL acima da média — estatisticamente cedo para conclusão definitiva, mas CPM €14,47 já é sinal de atenção.
> ⚪ Anúncios com gasto < €3 são listados apenas para rastreabilidade — não embasam recomendações.

---

## Módulo 2 - Diagnóstico de CPL (Causa Raiz)

### Campanha: DK - Leads - Forms - 11/03

**CPL subiu de €9,13 → €10,77 (+18%)**

A causa raiz não é uma única variável — é uma combinação de três fatores simultâneos:

**1. Rc1-jun em colapso de performance (principal responsável)**
Esse anúncio consumiu €193,95 — 50% de todo o budget da semana — e entregou apenas 9 leads com CPL €21,55. Na semana anterior, o mesmo criativo gerou 25 leads a €8,12. A degradação é de 165% no CPL. O CTR permanece similar (2,12% vs 2,15%), o que descarta problema criativo de atenção. O CPM saltou de €8,05 → €10,05 (+25%), indicando que o algoritmo está encontrando dificuldade crescente para entregar esse anúncio ao público correto — sinal claro de **saturação de público** no ad set "02/Advantage S/Moda e Marcas/Abril", que opera com frequência 2,11.

**2. Distribuição de budget desfavorável**
O ad set "03/Vídeos Novos/Agosto" (que contém [RC VIDEO 2]) recebeu apenas €159,40 — o anúncio mais eficiente da conta — enquanto o ad set "02/Vídeos Novos/Abril" concentrou €228,45 com performance ruim. O Advantage+ provavelmente está mantendo Rc1-jun por histórico de conversões, mesmo com a performance atual deteriorada.

**3. CPM da conta em alta geral**
CPM médio subiu de €9,35 → €10,08 (+7,8%). Ainda não crítico, mas pressiona o CPL toda semana que não é compensado por CTR proporcional.

**Ponto positivo:** [RC VIDEO 2] [JULIO] demonstra que o problema não é de público nem de mercado — é de criativo específico envelhecendo. CPL €6,32 com 25 leads valida que a conta tem potencial real de eficiência.

---

## Módulo 3 - Detecção de Anomalias

| Tipo | Anúncio | Variação / Detalhe | Ação Recomendada |
|---|---|---|---|
| 🔴 CPL crítico + deterioração severa | Rc1-jun | CPL €8,12 → €21,55 (+165%) com CPM €8,05 → €10,05 (+25%) | Pausar imediatamente — budget desperdiçado |
| 🔴 Gasto sem leads (> €15) | Rc2-jun | €1,34 gastos, 0 leads, CTR caiu de 2,48% → 0,87% | Monitorar — gasto baixo, mas CTR colapsou |
| 🟡 CPM elevado estrutural | comprar mejor | CPM €14,47 vs média da conta €10,08 (+43%) | Investigar segmentação — CPM desproporcional |
| 🟡 Anúncios novos sem entrega relevante | [RC VIDEO 1], [RC VIDEO 3], Rc9-jul | Gasto < €1 cada — sem dados suficientes | Verificar se há erro de configuração ou restrição |
| 🟢 Criativo destaque | [RC VIDEO 2] [JULIO] | CPL €6,32 com 25 leads — estreia forte | Escalar budget no ad set 03 |

---

## Módulo 4 - Pacing Monitor

| Parâmetro | Valor |
|---|---|
| Dia do mês | 6 de 31 (19,4% decorrido) |
| Gasto acumulado em agosto | €387,85 |
| Projeção mensal (ritmo atual) | €1.662,21 |
| Budget mensal estimado | €3.000,00 |
| Diferença projeção vs budget | -€1.337,79 (-44,6%) |
| Status | 🔴 RITMO MUITO LENTO |

> **Alerta:** No ritmo atual, agosto encerrará com apenas €1.662 gastos de um budget de €3.000 — aproveitamento de 55,4%. Com apenas 6 dias de mês decorridos e uma semana de dados, ainda há margem para correção, mas é urgente: o budget diário precisa subir ou novos criativos/ad sets precisam ser ativados para absorver o investimento planejado. A concentração em apenas uma campanha com um ad set ineficiente é o principal fator limitante.

---

## Módulo 5 - Fadiga de Criativos

| Anúncio | Frequência | CTR | Leads | Status | Recomendação |
|---|---|---|---|---|---|
| [RC VIDEO 2] [JULIO] | 1,52 | 3,54% | 25 | 🟢 Saudável | Escalar — muito espaço para crescer |
| comprar mejor | 1,48 | 2,84% | 2 | 🟢 Saudável | Aguardar mais dados |
| Rc1-jun | 1,99 | 2,12% | 9 | 🟢 Freq OK / 🔴 CPL crítico | Fadiga não é o problema — é saturação de público |
| Rc2-jun | 1,60 | 0,87% | 0 | 🟡 Monitorar CTR | CTR colapsou — criativo perdendo relevância |
| [RC VIDEO 1] [JULIO] | 1,22 | 0,00% | 0 | ⚪ Dados insuficientes | Verificar entrega |
| [RC VIDEO 3] [JULIO] | 1,21 | 0,00% | 0 | ⚪ Dados insuficientes | Verificar entrega |
| Rc9-jul | 1,00 | 0,00% | 0 | ⚪ Dados insuficientes | Verificar entrega |

> **Nota importante:** Nenhum criativo com entrega relevante está em zona de fadiga por frequência. Rc1-jun tem freq 1,99 — tecnicamente OK — mas o CPL triplicou, sugerindo que o público que converte já foi esgotado no ad set "02/Abril", não sendo problema de frequência exibida, mas de esgotamento do segmento convertível.

---

## Módulo 6 - Análise de Copy e Criativos

### 🏆 Criativo Vencedor

**[RC VIDEO 2] [JULIO]**
- CPL €6,32 com **25 leads** — resultado com alta significância estatística
- CTR 3,54% (o maior de toda a conta — +28% acima da média)
- CPM €9,53 — eficiente, abaixo da média da conta
- Frequência 1,52 — amplo espaço para escala sem risco de fadiga
- **Conclusão:** É o criativo de referência da conta nesta semana. Deve receber aumento de budget prioritário.

### 🔄 Candidato a Monitorar (dados insuficientes)

**comprar mejor**
- CPL €16,54 com apenas **2 leads** — *estatisticamente cedo para conclusão*
- CPM €14,47 é preocupante (43% acima da média) — pode indicar problema de segmentação ou criativo pouco relevante para o público
- CTR 2,84% é razoável — o problema está na conversão pós-clique ou no CPM alto
- **Aguardar mais 3-5 leads antes de qualquer decisão de escala ou pausa**

### ❌ Criativos para Pausar

**Rc1-jun** — 🔴 PAUSAR IMEDIATAMENTE
- CPL explodiu de €8,12 → €21,55 (+165%) consumindo €193,95 (50% do budget)
- CPM subiu 25% — algoritmo sinalizando esgotamento do público convertível no ad set 02
- Criativo antigo (junho) — ciclo de vida esgotado nesse público
- **Impacto direto:** pausar libera ~€27/dia para redistribuir ao [RC VIDEO 2]

**Rc2-jun** — pausar (gasto baixo, mas CTR colapsou de 2,48% → 0,87%)

### ⏳ Aguardar (dados insuficientes para decidir)
[RC VIDEO 1] [JULIO] | [RC VIDEO 3] [JULIO] | Rc9-jul — cada um com menos de €1 gasto. Verificar se há restrição de entrega antes de qualquer julgamento de performance.

---

## Módulo 7 - Análise de Ad Sets e Públicos

| Ad Set | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| 03/ Advantage S/ Moda e Marcas / 7M / Vídeos Novos/ Agosto | €159,40 | 25 | €6,38 | 3,51% | €9,51 | 1,54 | 🟢 OK |
| 02/ Advantage S/ Moda e Marcas / 7M / Vídeos Novos/ Abril | €228,45 | 11 | €20,77 | 2,19% | €10,52 | 2,11 | 🔴 CRÍTICO |

**Observações:**

- **Ad Set 03 (Agosto)** é o motor da conta nesta semana: CPL €6,38, frequência baixa (1,54), CTR excelente (3,51%). Recebeu apenas 41% do budget — inversamente proporcional à sua eficiência. Há amplo espaço para aumento de budget sem risco de saturação.

- **Ad Set 02 (Abril)** está consumindo 59% do budget com CPL 3,2x maior que o Ad Set 03. O nome "Abril" sugere que este público vem sendo trabalhado há mais tempo — o que corrobora a hipótese de esgotamento do segmento convertível, não de fadiga criativa por frequência. A combinação de CPM mais alto (€10,52) e CTR mais baixo (2,19%) aponta para público menos responsivo.

- **Sobreposição de público:** Ambos os ad sets usam o mesmo interesse base ("Moda e Marcas / 7M"). Se rodando simultaneamente, há risco de sobreposição de audiência. Recomenda-se verificar no Audience Overlap Tool — com dois ad sets do mesmo público, o Advantage+ pode estar em competição interna, elevando CPM artificialmente.

- **Criativos inativos nos ad sets:** [RC VIDEO 1], [RC VIDEO 3] e Rc9-jul com gasto irrisório podem estar sendo suprimidos pelo Advantage+ em favor de [RC VIDEO 2]. Isso é esperado, mas vale confirmar se há restrições de aprovação ou problemas técnicos.

---

## Plano de Ação

| Prioridade | Ação | Impacto | Prazo |
|---|---|---|---|
| 🔴 P1 | Pausar Rc1-jun — libera ~€27/dia consumido sem eficiência | CPL médio da campanha deve cair para ~€7-8 | Hoje |
| 🔴 P2 | Aumentar budget do Ad Set 03 (Agosto) em 40-60% para absorver verba liberada do Rc1-jun | Mais leads a €6,32 — reduz CPL geral da conta | Hoje |
| 🔴 P3 | Pausar Rc2-jun — gasto baixo mas CTR colapsado, sem sinal de recuperação | Elimina ruído nos dados do ad set | Hoje |
| 🟡 P4 | Verificar entrega de [RC VIDEO 1], [RC VIDEO 3] e Rc9-jul — possível erro de configuração ou restrição de aprovação | Pode revelar criativos potencialmente bons travados | Hoje / amanhã |
| 🟡 P5 | Verificar sobreposição de público entre Ad Set 02 e Ad Set 03 via Audience Overlap | Pode estar inflando CPM artificialmente | 24-48h |
| 🟡 P6 | Avaliar encerramento ou renovação do Ad Set 02 (Abril) com criativo novo | Público antigo esgotado — novo criativo pode reativar segmento | Esta semana |
| 🟢 P7 | Monitorar comprar mejor por mais 3-5 leads antes de decidir sobre escala ou pausa (CPM alto em observação) | Decisão com significância estatística | 48-72h |
| 🟢 P8 | Criar variações de [RC VIDEO 2] para pipeline de testes — replicar elementos vencedores | Antecipa próximo criativo vencedor quando RC VIDEO 2 saturar | Próxima semana |

---

## BLOCO TRELLO

---

**Meta Ads Luxe Icon LTD — 06/08/2026**
**Gasto:** €387,85 | **Leads:** 36 | **CPL:** €10,77
**Variação vs semana anterior:** CPL +18,0% 🔴 | Leads +5,9% 📈
**Pacing:** 🔴 RITMO LENTO — Projeção €1.662 vs Budget €3.000 (19,4% do mês decorrido)

---

📌 **CONTEXTO DA SEMANA**
Dois novos ad sets de "Vídeos Novos" foram ativados (Abril e Agosto), com criativos [RC VIDEO 1], [RC VIDEO 2] e [RC VIDEO 3] introduzidos. O grande impacto desta semana foi a deterioração severa de Rc1-jun, que operou bem por semanas e entrou em colapso de eficiência — provavelmente porque o ciclo de vida do criativo no público do Ad Set 02 (Abril) se esgotou. Isso criou uma situação paradoxal: a conta tem um criativo excelente rodando ([RC VIDEO 2]) mas a maior parte do budget foi consumida pelo criativo mais ineficiente.

---

📊 **PANORAMA DA SEMANA**

🔍 **Campanhas & Anúncios**
A conta opera com uma única campanha ativa (DK - Leads - Forms - 11/03) e dois ad sets. O Ad Set 03/Agosto está saudável e é responsável por 69% dos leads com apenas 41% do budget. O Ad Set 02/Abril concentrou 59% dos gastos e gerou apenas 31% dos leads, puxado pelo colapso de Rc1-jun. Os três criativos novos ([RC VIDEO 1], [RC VIDEO 3], Rc9-jul) praticamente não receberam entrega — cada um com menos de €1 gasto.

📉 **Causa Raiz do CPL**
O CPL subiu de €9,13 → €10,77 (+18%) principalmente porque Rc1-jun — que na semana passada gerou 25 leads a €8,12 — desta vez gerou apenas 9 leads a €21,55, consumindo 50% do budget total. O CTR do criativo mal se alterou (2,15% → 2,12%), mas o CPM subiu 25% (€8,05 → €10,05): o algoritmo está pagando mais caro para entregar ao público do Ad Set 02, porque os usuários convertíveis nesse segmento já foram alcançados. O ponto positivo é que [RC VIDEO 2] entregou CPL €6,32 com 25 leads — provando que o público geral ainda está respondendo bem quando o criativo é relevante.

⚠️ **Anomalias**
- 🔴 **Rc1-jun:** CPL explodiu +165% (€8,12 → €21,55) com CPM +25% — consumiu €193,95 com resultado pobre. Pausar hoje.
- 🔴 **Rc2-jun:** CTR colapsou de 2,48% → 0,87%, 0 leads. Sem sinal de recuperação.
- 🟡 **comprar mejor:** CPM €14,47 é 43% acima da média da conta — estruturalmente caro para o público que está atingindo.
- 🟡 **[RC VIDEO 1], [RC VIDEO 3], Rc9-jul:** gasto irrisório (< €1 cada) — verificar se há erro de configuração, restrição de aprovação ou se estão sendo suprimidos pelo Advantage+.

📅 **Pacing**
No ritmo atual, agosto encerrará com €1.662 de €3.000 gastos — apenas 55% do budget aproveitado. Com 19% do mês decorrido, ainda há janela de correção, mas é urgente. A principal causa é a ineficiência do Ad Set 02 limitando a entrega rentável: o algoritmo reduz naturalmente o volume quando o CPL sobe. A ação imediata é pausar Rc1-jun e redirecionar o budget para o Ad Set 03, que tem espaço de escala real com frequência 1,54. Aumentar o budget diário do Ad Set 03 em 40-60% é o caminho mais rápido para absorver o investimento planejado com eficiência.

😴 **Fadiga de Criativos**
Frequências gerais sob controle — nenhum criativo com entrega relevante está acima de 2,0. [RC VIDEO 2] opera em 1,52 com amplo espaço de escala. Rc1-jun tem freq 1,99 (formalmente OK), mas o problema não é fadiga de exibição — é esgotamento do segmento convertível no Ad Set 02, que opera desde abril.

🎨 **Criativos**
**Vencedor principal:** [RC VIDEO 2] [JULIO] — CPL €6,32 com **25 leads** (vídeo) ✅ Significância estatística confirmada
**Para pausar:** Rc1-jun — CPL €21,55, degradação de 165%, 50% do budget consumido com resultado ruim
**Para pausar:** Rc2-jun — CTR colapsado, 0 leads
**Dados insuficientes (aguardar):** [RC VIDEO 1] [JULIO], [RC VIDEO 3] [JULIO], Rc9-jul, comprar mejor (apenas 2 leads)

🎯 **Ad Sets & Públicos**
Ad Set 03/Agosto: CPM €9,51, frequência 1,54 — excelente espaço para escala, é onde [RC VIDEO 2] roda. Ad Set 02/Abril: CPM €10,52, CPL €20,77 — público possivelmente esgotado. Atenção: ambos os ad sets usam a mesma base de público (Moda e Marcas / 7M), o que pode gerar sobreposição e inflação de CPM — verificar Audience Overlap antes de escalar.

---

🚀 **PRÓXIMOS PASSOS**
- 🔴 **[HOJE — URGENTE]** Pausar Rc1-jun: libera ~€27/dia consumido a CPL €21,55
- 🔴 **[HOJE — URGENTE]** Aumentar budget Ad Set 03/Agosto em +40-60%: redireciona verba para o criativo mais eficiente da conta (CPL €6,32)
- 🔴 **[HOJE]** Pausar Rc2-jun: CTR colapsado, sem perspectiva de recuperação
- 🟡 **[24-48h]** Verificar entrega e possível restrição de [RC VIDEO 1], [RC VIDEO 3] e Rc9-jul — podem estar travados por aprovação
- 🟡 **[48h]** Checar sobreposição de público entre Ad Sets 02 e 03 — risco de competição interna inflando CPM
- 🟢 **[Próxima semana]** Criar variações criativas baseadas em [RC VIDEO 2] para alimentar pipeline de testes — antecipar substituição quando saturar

---