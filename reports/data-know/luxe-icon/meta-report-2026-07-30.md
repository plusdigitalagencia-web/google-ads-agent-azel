# Relatório Meta Ads - Luxe Icon LTD
**Período atual:** 23/07/2026 a 29/07/2026
**Período anterior:** 16/07/2026 a 22/07/2026
**Gerado em:** 30/07/2026 | **Conta:** act_412122005210742

---

## Resumo Executivo

| Métrica | Atual | Anterior | Variação |
|---|---|---|---|
| Gasto | €310,52 | €157,73 | +96,9% 📈 |
| Leads | 34 | 25 | +36,0% 📈 |
| CPL | €9,13 | €6,31 | +44,7% 🔴 |
| CPM | €9,35 | €7,73 | +21,0% 🔴 |
| CTR | 2,23% | 3,33% | -33,0% 🔴 |
| Frequência | 2,34 | 2,08 | +12,5% 🟡 |

> **Leitura rápida:** A conta cresceu em volume de leads (+36%) e gasto (+97%), mas o CPL piorou significativamente (+44,7%). O gasto quase dobrou enquanto os leads cresceram apenas um terço — sinal claro de ineficiência. A principal causa é a virada do mix de criativos: os anúncios de alta performance da semana anterior (RC-BD-Imagen-2026 com CPL €5,76 e Vídeo 2 com CPL €6,70) saíram de cena, e o budget foi absorvido majoritariamente por "Rc1-jun" e "descobrir_bolso", este último com CPL €16,67. O CTR caiu 33%, indicando criativos menos relevantes para a audiência atual.

---

## Módulo 1 - Auditoria de Campanhas e Anúncios

### Campanhas

| Campanha | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| DK - Leads - Forms - 11/03 | €310,52 | 34 | €9,13 | 2,23% | €9,35 | 2,34 | 🟡 ATENÇÃO |

> Única campanha ativa. CPL atual (€9,13) representa 1,45× o CPL anterior (€6,31), dentro da faixa de ATENÇÃO (1,3x–2x da referência histórica).

---

### Anúncios por Campanha — DK - Leads - Forms - 11/03

*(ordenados por CPL, criativos com leads primeiro)*

| Anúncio | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| Rc1-jun | €202,90 | 25 | €8,12 | 2,15% | €8,05 | 2,33 | 🟢 OK |
| descobrir_bolso | €100,04 | 6 | €16,67 | 2,56% | €13,91 | 1,42 | 🔴 CRÍTICO |
| Rc2-jun | €2,70 | 2 | €1,35 | 2,48% | €11,16 | 1,64 | ⚪ Dados insuficientes |
| comprar mejor | €2,74 | 1 | €2,74 | 1,25% | €8,59 | 1,29 | ⚪ Dados insuficientes |
| Rc9-jul | €2,14 | 0 | — | 2,45% | €8,73 | 1,34 | 🔴 CRÍTICO |

> **Rc9-jul:** €2,14 gastos, 0 leads. Gasto < €3 — mencionar mas não basear recomendações neste dado ainda.
> **Rc2-jun:** CPL aparente de €1,35 é promissor, mas com apenas 2 leads e €2,70 gastos é estatisticamente cedo para qualquer conclusão.
> **descobrir_bolso:** CPL de €16,67 representa 1,83× o CPL da conta — sozinho consumiu 32% do budget semanal gerando apenas 6 leads.

---

## Módulo 2 - Diagnóstico de CPL (Causa Raiz)

### Campanha: DK - Leads - Forms - 11/03

**CPL subiu de €6,31 → €9,13 (+44,7%). Por quê?**

**1. Virada de mix de criativos (causa principal)**
Os dois criativos mais eficientes da semana anterior — RC-BD-Imagen-2026 (CPL €5,76, 11 leads) e Vídeo 2 (CPL €6,70, 6 leads) — não aparecem na semana atual. Combinados, respondiam por 17 dos 25 leads anteriores com gasto médio por lead de ~€6,00. Sem eles, o budget foi redistribuído entre criativos mais caros.

**2. CPM encareceu (+21%): €7,73 → €9,35**
O CPM subiu mesmo dentro do mesmo ad set (Advantage+). Dois fatores prováveis: (a) a frequência crescendo de 2,08 → 2,34 indica que o algoritmo está batendo nas mesmas pessoas com menor eficiência de leilão; (b) descobrir_bolso opera com CPM €13,91 — 49% acima da média — puxando o CPM consolidado para cima.

**3. CTR caiu 33%: 3,33% → 2,23%**
A queda de CTR indica que os criativos ativos (especialmente Rc1-jun com 2,15%) geram menos interesse do que os criativos da semana anterior. RC-BD-Imagen-2026 rodou com CTR 3,43% e Vídeo 2 com 4,17%. A audiência Advantage+ está recebendo criativos menos persuasivos, resultando em mais impressões necessárias por lead.

**4. Concentração excessiva de budget em 1 criativo**
Rc1-jun absorveu 65% do gasto total (€202,90 de €310,52) com CTR de apenas 2,15%, enquanto o único criativo com CTR razoável (descobrir_bolso, 2,56%) tem CPM muito alto e CPL explosivo de €16,67.

**Equação do problema:**
`CPL = CPM / (CTR × CVR)` — CPM subiu, CTR caiu, e o resultado foi CPL quase 45% mais caro.

---

## Módulo 3 - Detecção de Anomalias

| Tipo | Anúncio | Variação / Dado | Ação |
|---|---|---|---|
| 🔴 Desaparecimento de criativos | RC-BD-Imagen-2026 | Era o melhor criativo da semana anterior (CPL €5,76, 11 leads) — ausente esta semana | Verificar se foi pausado manualmente ou por regra automática; reativar se possível |
| 🔴 Desaparecimento de criativos | Vídeo 2 | CPL €6,70 com 6 leads na semana anterior — ausente esta semana | Mesma verificação acima |
| 🔴 CPL crítico + CPM alto | descobrir_bolso | CPL €16,67 (1,83× a média), CPM €13,91 (49% acima da média), consumiu €100,04 | Pausar imediatamente — budget desperdiçado |
| 🟡 Zero leads com gasto | Rc9-jul | €2,14 gastos, 0 leads — gasto < €15, monitorar | Dar mais 2-3 dias ou pausar se não converter |
| 🟡 Frequência crescente | Rc1-jun | Frequência 2,33 — próximo da faixa de Atenção (2,5) | Monitorar nos próximos 7 dias; preparar criativo substituto |
| ⚪ CPL aparente baixíssimo | Rc2-jun | CPL €1,35 com apenas 2 leads e €2,70 gastos | Aguardar mais dados — estatisticamente cedo para qualquer conclusão |

---

## Módulo 4 - Pacing Monitor

| Parâmetro | Valor |
|---|---|
| Dia do mês | 30 de 31 |
| % do mês decorrido | 96,8% |
| Gasto semana atual | €310,52 |
| **Projeção mensal** | **€1.330,80** |
| **Budget mensal** | **€3.000,00** |
| Diferença | -€1.669,20 (-55,6%) |
| **Status** | 🔴 MUITO LENTO |

> **Análise crítica:** A menos de 4% do fim do mês, a conta vai encerrar julho com ~€1.331 gastos — **44,4% do budget mensal aprovado**. Isso representa €1.669 de budget não utilizado em um único mês. O subgasto sugere que a campanha pode ter ficado pausada ou com budget diário insuficiente por boa parte do mês, já que os €310,52 da última semana correspondem a ~44 leads e dificilmente explicam um mês inteiro.
>
> **Ação imediata para agosto:** revisar o budget diário e garantir que a campanha rode ininterruptamente. Considerar aumentar budget diário em agosto para compensar o ritmo e atingir os €3.000 mensais.

---

## Módulo 5 - Fadiga de Criativos

| Anúncio | Freq | CTR | Leads | Status | Recomendação |
|---|---|---|---|---|---|
| Rc1-jun | 2,33 | 2,15% | 25 | 🟡 Monitorar | Frequência próxima de 2,5 — preparar variação criativa para rotação |
| descobrir_bolso | 1,42 | 2,56% | 6 | 🟢 OK (freq) | Frequência saudável, mas CPL crítico — problema é eficiência, não fadiga |
| Rc2-jun | 1,64 | 2,48% | 2 | 🟢 OK | Frequência baixa, dados insuficientes |
| comprar mejor | 1,29 | 1,25% | 1 | 🟢 OK | Frequência baixa, dados insuficientes |
| Rc9-jul | 1,34 | 2,45% | 0 | 🟢 OK (freq) | Frequência baixa, problema é conversão |

> **Leitura geral:** Nenhum criativo está em fadiga severa (>3,5). O único em zona de atenção é Rc1-jun (2,33), que carrega 82% dos leads da semana. Se continuar sendo o único ativo com budget concentrado, pode atingir frequência crítica nas próximas 1-2 semanas. Prioridade: criar variações de Rc1-jun antes que sature.

---

## Módulo 6 - Análise de Copy e Criativos

### 🏆 Criativo Vencedor

**Rc1-jun** — CPL €8,12 com **25 leads** (65% do budget, formato a confirmar)
- Único criativo com volume estatisticamente relevante na semana atual
- CPL €8,12 está abaixo da média da conta esta semana (€9,13) — portanto eficiente dentro do contexto atual
- CTR 2,15% e CPM €8,05 — custo por impressão mais barato entre os criativos ativos
- **Ressalva:** frequência em 2,33 — monitorar sinais de saturação. Preparar variações.

### 📈 Candidato a Escalar (aguardar dados)

**Rc2-jun** — CPL aparente €1,35 com apenas **2 leads** e €2,70 gastos
- Estatisticamente cedo para conclusão — dados absolutamente insuficientes
- CTR (2,48%) e CPM (€11,16) não permitem projeção confiável
- Recomendação: aumentar orçamento gradualmente para €10–15 e observar por 5–7 dias antes de qualquer decisão

### 🔴 Criativos para Pausar

| Criativo | Motivo |
|---|---|
| **descobrir_bolso** | CPL €16,67 (1,83× a média), CPM €13,91 (49% acima da média) — consumiu €100,04 gerando apenas 6 leads. Detectado como anomalia no Módulo 3. Pausar imediatamente e realocar budget para Rc1-jun |
| **Rc9-jul** | €2,14 gastos, 0 leads. Gasto abaixo de €15 — dar mais 2-3 dias com monitoramento. Se não converter até €10 totais, pausar |

### ⚪ Dados Insuficientes

**comprar mejor** (€2,74, 1 lead) — aguardar volume mínimo antes de qualquer decisão.

### 🔍 Criativos ausentes (verificar urgente)

**RC-BD-Imagen-2026** e **Vídeo 2** foram os melhores criativos da semana anterior e desapareceram completamente. Reativar pode ser a ação de maior impacto imediato na conta.

---

## Módulo 7 - Análise de Ad Sets e Públicos

### Ad Sets Ativos

| Ad Set | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| 02/ Advantage S/Moda e Marcas / 7M / Vídeos Novos/ Abril | €310,52 | 34 | €9,13 | 2,23% | €9,35 | 2,34 | 🟡 ATENÇÃO |

**Observações:**

- **Apenas 1 ad set ativo** — toda a conta depende de um único conjunto de anúncios. Não há risco de sobreposição de públicos, mas há risco operacional alto: qualquer problema neste ad set paralisa toda a geração de leads.
- **Advantage+ Shopping (público amplo, 7M):** o algoritmo tem liberdade para otimizar dentro de um pool de 7 milhões de usuários. O CPM crescendo de €7,73 → €9,35 com frequência subindo sugere que o algoritmo está recirculando para usuários já vistos, possivelmente por falta de criativos novos para explorar novos segmentos dentro do público.
- **Frequência 2,34 no ad set:** considerando que é Advantage+, esta frequência consolidada indica que o público Moda e Marcas está começando a ser saturado. Novos criativos com ângulos diferentes são necessários para que o algoritmo encontre novos sub-segmentos.
- **Recomendação estrutural:** Avaliar criação de um segundo ad set com público diferente (ex: lookalike de leads convertidos ou público de interesse diferente) para reduzir dependência e testar CPMs.

---

## Plano de Ação

| Prioridade | Ação | Impacto | Prazo |
|---|---|---|---|
| 🔴 P1 | **Pausar "descobrir_bolso"** — CPL €16,67 detectado como anomalia (Módulo 3). Realocar €100/semana de budget para Rc1-jun | Alto — elimina criativo que desperdiçou €100 com CPL 83% acima da média | Hoje |
| 🔴 P2 | **Verificar e reativar RC-BD-Imagen-2026 e Vídeo 2** — desapareceram sem explicação. Eram responsáveis por 17 dos 25 leads da semana anterior com CPL médio ~€6,00 | Muito Alto — pode baixar CPL de volta para faixa de €6–7 | Hoje |
| 🟡 P3 | **Escalar Rc2-jun gradualmente** — aumentar orçamento para €10–15 e observar por 5–7 dias. Não escalar de forma agressiva com apenas 2 leads | Médio — CPL aparente promissor mas sem significância estatística | 24–48h |
| 🟡 P4 | **Monitorar Rc9-jul** — dar mais 2–3 dias. Se atingir €10 sem leads, pausar | Baixo/Médio — evitar desperdício de budget em criativo não conversivo | 48–72h |
| 🟡 P5 | **Criar variações de Rc1-jun** — frequência em 2,33, risco de saturação nas próximas semanas. Produzir 2–3 variações de copy/visual com mesmo ângulo vencedor | Alto (preventivo) — garante continuidade quando Rc1-jun saturar | Esta semana |
| 🟢 P6 | **Revisar budget diário para agosto** — julho encerrou com apenas 44% do budget utilizado (€1.331 de €3.000). Aumentar budget diário e garantir campanha ativa ininterruptamente | Alto (estrutural) — evitar repetição do subgasto em agosto | Antes de 01/08 |
| 🟢 P7 | **Criar segundo ad set com público diferente** — lookalike de leads ou interesse distinto para reduzir dependência do público único atual e combater crescimento de CPM | Médio-Alto (médio prazo) | Próxima semana |

---

## BLOCO TRELLO

---

**Meta Ads Luxe Icon LTD — 30/07/2026**
**Gasto:** €310,52 | **Leads:** 34 | **CPL:** €9,13
**Variação vs semana anterior:** CPL +44,7% 🔴 | Leads +36,0% 📈 | Gasto +96,9% 📈
**Pacing:** 🔴 MUITO LENTO — Projeção €1.330,80 vs Budget €3.000 (96,8% do mês decorrido)

---

📌 **CONTEXTO DA SEMANA**
Esta semana houve uma virada significativa no mix de criativos ativos. Os dois anúncios mais eficientes da semana anterior — RC-BD-Imagen-2026 (CPL €5,76, 11 leads) e Vídeo 2 (CPL €6,70, 6 leads) — desapareceram completamente da conta sem registro aparente nos dados. Com isso, o budget foi absorvido por criativos menos eficientes, em especial "descobrir_bolso" (CPL €16,67) que sozinho consumiu €100 gerando apenas 6 leads. Essa troca de mix explica a maior parte da deterioração do CPL.

---

📊 **PANORAMA DA SEMANA**

🔍 **Campanhas & Anúncios**
A conta opera com 1 única campanha ativa (DK - Leads - Forms - 11/03) e 1 único ad set (Advantage+ / Moda e Marcas / 7M). Dos 5 anúncios ativos, apenas Rc1-jun tem volume relevante — 25 leads, €202,90, CPL €8,12 — sendo responsável por 73% dos leads da semana. Os demais anúncios somam 9 leads com performance heterogênea, e "descobrir_bolso" é um dreno ativo de budget com CPL 83% acima da média da conta.

📉 **Causa Raiz do CPL**
O CPL subiu de €6,31 para €9,13 (+44,7%) por uma combinação de três fatores simultâneos: (1) os criativos mais eficientes da semana anterior saíram de rotação, privando a conta de seu motor principal de leads baratos; (2) o CPM encareceu 21% (€7,73 → €9,35), parcialmente puxado pelo CPM absurdo de €13,91 do "descobrir_bolso" e pela frequência crescente do público Advantage+; (3) o CTR caiu 33% (3,33% → 2,23%), indicando que os criativos ativos geram menos engajamento que os anteriores — mais impressões necessárias para cada lead. O resultado matemático inevitável é CPL mais alto.

⚠️ **Anomalias**
- 🔴 **RC-BD-Imagen-2026 e Vídeo 2 desapareceram** — eram os melhores criativos e sumiram sem explicação. Verificar urgente se foram pausados manualmente ou por regra automática.
- 🔴 **"descobrir_bolso" com CPL €16,67** — consumiu €100,04 (32% do budget semanal) entregando apenas 6 leads. CPM de €13,91 é 49% acima da média. Anomalia confirmada.
- 🟡 **Rc9-jul com 0 leads** em €2,14 gastos — gasto ainda abaixo de €15, monitorar antes de concluir.

📅 **Pacing**
Com 96,8% do mês decorrido, julho vai encerrar com ~€1.331 gastos de um budget de €3.000 — apenas 44% aproveitado. O subgasto de €1.669 sugere que a campanha ficou pausada ou com budget insuficiente por boa parte de julho. Para agosto, é crítico revisar o budget diário antes do dia 01/08 e garantir operação contínua da campanha. Se o budget mensal de €3.000 for mantido, o budget diário deve ser configurado para ~€97/dia e monitorado semanalmente.

😴 **Fadiga de Criativos**
A frequência geral está em 2,34 — dentro da zona de monitoramento mas ainda longe de fadiga severa. O ponto de atenção é Rc1-jun especificamente (freq 2,33), que concentra quase todo o budget. Se continuar sendo o único criativo relevante com budget concentrado, pode atingir a zona de atenção (2,5+) nas próximas 1-2 semanas. Criar variações agora é medida preventiva importante.

🎨 **Criativos**
**Vencedor principal:** Rc1-jun — CPL €8,12 com **25 leads** (formato a confirmar — maior volume relevante da semana)
**Candidato a escalar (aguardar):** Rc2-jun — CPL aparente €1,35, mas apenas 2 leads e €2,70 gastos. *Estatisticamente cedo para conclusão* — aumentar orçamento gradualmente e aguardar 5–7 dias.
**Para pausar:** descobrir_bolso — CPL €16,67, CPM €13,91, anomalia confirmada. Pausar hoje e realocar budget.
**Dados insuficientes (aguardar):** comprar mejor, Rc9-jul
**Verificar urgente (ausentes):** RC-BD-Imagen-2026, Vídeo 2 — reativar pode ser a ação de maior ROI desta semana.

🎯 **Ad Sets & Públicos**
CPM do público Advantage+ / Moda e Marcas / 7M subiu para €9,35, com frequência de 2,34 — sinais de que o algoritmo está recirculando para as mesmas pessoas. O pool de 7M tem espaço para crescer, mas precisa de novos criativos para explorar sub-segmentos frescos. A dependência de 1 único ad set é um risco operacional — qualquer problema paralisa toda a conta. Avaliar criação de segundo ad set com público distinto em agosto.

---

🚀 **PRÓXIMOS PASSOS**
- 🔴 **[HOJE] Pausar "descobrir_bolso"** — CPL €16,67, anomalia confirmada, dreno de €100/semana com apenas 6 leads
- 🔴 **[HOJE] Verificar e reativar RC-BD-Imagen-2026 e Vídeo 2** — desapareceram sem registro; reativar pode reduzir CPL de volta para ~€6
- 🟡 **[24–48h] Aumentar orçamento de Rc2-jun para €10–15** e monitorar por 5–7 dias antes de escalar
- 🟡 **[ANTES DE 01/08] Revisar budget diário para agosto** — julho encerrou com 44% do budget não utilizado; configurar ~€97/dia para agosto
- 🟢 **[ESTA SEMANA] Criar 2–3 variações de Rc1-jun** — frequência em 2,33, saturação possível nas próximas semanas; produzir variações preventivamente

---