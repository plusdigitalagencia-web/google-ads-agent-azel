# Relatório Meta Ads — Leblon Real Estate
**Período atual:** 30/07/2026 a 05/08/2026
**Período anterior:** 23/07/2026 a 29/07/2026
**Gerado em:** 06/08/2026 | **Conta:** act_1187011709535726

---

## Resumo Executivo

| Métrica | Atual | Anterior | Variação |
|---|---|---|---|
| Gasto | €287,24 | €297,71 | -3,5% 🟢 |
| Leads | 28 | 22 | +27,3% 🟢 |
| CPL | €10,26 | €13,53 | -24,2% 🟢 |
| CPM Médio | €11,24 | €13,01 | -13,6% 🟢 |
| CTR Médio | 2,13% | 2,03% | +4,9% 🟢 |
| Frequência Média | 1,88 | 1,81 | +3,9% 🟡 |

> **Semana positiva:** o CPL caiu 24% com gasto praticamente estável — melhora real de eficiência. A campanha [CPL][EUROPA] foi a principal responsável, triplicando os leads (10 → 16) com CPL €8,68 vs €14,01 anterior. O CPM médio caiu €1,77, contribuindo para a melhora.

---

## Módulo 1 — Auditoria de Campanhas e Anúncios

### Campanhas

| Campanha | Gasto | Leads | CPL | CPL Ant. | Δ CPL | CTR | CPM | Freq. | Status |
|---|---|---|---|---|---|---|---|---|---|
| [CPL][EUROPA] | €138,89 | 16 | €8,68 | €14,01 | -38,0% 🟢 | 2,32% | €10,23 | 2,04 | 🟢 OK |
| DK - [CPL] [MEXICO] [FORMS] [BOF] [09/10] | €148,35 | 12 | €12,36 | €13,13 | -5,9% 🟢 | 1,95% | €12,25 | 1,72 | 🟢 OK |

> **Média da conta:** €10,26. Threshold 🟡 = €13,34 | Threshold 🔴 = €20,52
> Ambas as campanhas operam abaixo do threshold de atenção.

---

### Anúncios por Campanha

#### DK - [CPL] [MEXICO] [FORMS] [BOF] [09/10]

| Anúncio | Gasto | Leads | CPL | CTR | CPM | Freq. | Status |
|---|---|---|---|---|---|---|---|
| AD10 - [IMG] [PROPRIEDADES PREMIUM] — Cópia | €143,01 | 12 | €11,92 | 1,95% | €11,95 | 1,71 | 🟢 OK |
| AD15 - [IMG] [para unos pocos] novo | €5,34 | 0 | — | 2,13% | €37,87 | 1,10 | 🔴 CRÍTICO |

#### [CPL][EUROPA]

| Anúncio | Gasto | Leads | CPL | CTR | CPM | Freq. | Status |
|---|---|---|---|---|---|---|---|
| AD06 | €42,09 | 6 | €7,02 | 2,04% | €10,75 | 1,74 | 🟢 OK |
| AD07 | €94,62 | 10 | €9,46 | 2,46% | €9,91 | 1,77 | 🟢 OK |
| AD05 | €1,41 | 0 | — | 0,00% | €14,84 | 1,10 | ⚪ Insuficiente |
| AD010 (€0,55) | €0,55 | 0 | — | 0,00% | €30,56 | 1,00 | ⚪ Insuficiente |
| AD010 (€0,22) | €0,22 | 0 | — | 0,00% | €44,00 | 1,00 | ⚪ Insuficiente |

> ⚠️ **Nota sobre AD010:** aparecem duas entradas com o mesmo nome na campanha [CPL][EUROPA] — gastos de €0,55 e €0,22. Recomenda-se verificar se são duplicatas ou anúncios distintos com nomenclatura incorreta.

---

## Módulo 2 — Diagnóstico de CPL (Causa Raiz)

### [CPL][EUROPA] — CPL caiu 38% (€14,01 → €8,68) 🟢

**Causa raiz: melhora combinada de CPM + CTR + volume de criativos eficientes**

- CPM recuou de €11,18 → €10,23 (-8,5%): custo de exibição mais barato nesta semana
- CTR subiu de 1,93% → 2,32% (+20%): melhora significativa de engajamento
- **AD07** entrou em ritmo com 10 leads a €9,46 — na semana anterior gerou apenas 3 leads a €20,30 com menos budget
- **AD06** contribuiu com 6 leads a €7,02 — semana anterior estava em fase inicial (€3,31, sem leads), agora com volume real
- A combinação dos dois criativos funcionando simultaneamente aumentou o volume e reduziu o CPL médio da campanha

### DK - [CPL] [MEXICO] [FORMS] [BOF] [09/10] — CPL caiu 6% (€13,13 → €12,36) 🟢

**Causa raiz: CPM mais barato, mas eficiência de conversão praticamente estável**

- CPM caiu de €14,84 → €11,95 (-19,5%): melhora relevante no custo de entrega
- CTR recuou de 2,14% → 1,95% (-9%): leve piora na qualidade do clique — contém parte do ganho do CPM
- Volume de leads idêntico ao da semana anterior (12 leads): a campanha está consistente mas não crescendo
- **AD15** consome €5,34 sem gerar nenhum lead, com CPM de €37,87 — 3x acima da média da conta — drenou ~3,6% do budget da campanha sem retorno

---

## Módulo 3 — Detecção de Anomalias

| Tipo | Anúncio | Detalhe | Ação Recomendada |
|---|---|---|---|
| 🔴 CPM anômalo + 0 leads | AD15 - [IMG] [para unos pocos] novo | CPM €37,87 (3,4× a média da conta €11,24) com €5,34 gastos e 0 leads | Pausar imediatamente — CPM alto indica rejeição de entrega pelo algoritmo |
| 🔴 CPM anômalo + 0 leads | AD010 (€0,55) | CPM €30,56 com 0 leads | Dados insuficientes, mas CPM é 2,7× a média — monitorar; não escalar |
| 🔴 CPM anômalo + 0 leads | AD010 (€0,22) | CPM €44,00 com 0 leads | Dados insuficientes — verificar nome duplicado; não escalar |
| ⚠️ Nomenclatura duplicada | AD010 (dois registros) | Dois anúncios "AD010" na mesma campanha [CPL][EUROPA] | Verificar no Gerenciador se são anúncios distintos; corrigir nomenclatura |
| ⚠️ Melhora abrupta de CPL (AD07) | AD07 | CPL caiu de €20,30 → €9,46 (-53%) com volume triplicado | Positivo — monitorar se sustenta; pode ser variação de período |
| ⚠️ Ad Set com 0 leads e CPM alto | #2 - [PS - Cidades x Rico X México] | CPM €37,87, €5,34 gastos, 0 leads | Pausar ou revisar — espelha o problema do AD15 |

---

## Módulo 4 — Pacing Monitor

| Parâmetro | Valor |
|---|---|
| Dia do mês | 6 de 31 (19,4% decorrido) |
| Gasto acumulado na semana | €287,24 |
| Projeção mensal (ritmo atual) | €1.231,03 |
| Budget mensal estimado | €1.500,00 |
| Diferença projeção vs budget | -17,9% |
| Status | 🟡 LENTO |

> **Análise:** No ritmo atual, agosto encerrará com €1.231 — €269 abaixo do budget de €1.500. A principal razão é que o gasto diário médio (~€41/dia nesta semana) está abaixo do necessário (~€48,4/dia para esgotar o budget). O ad set **#2 - [PS - Cidades x Rico X México]** — que gerou 0 leads e CPM anômalo — consome budget ineficientemente mas não resolve o pacing. A alavanca correta é aumentar o budget diário dos ad sets eficientes ([ALE][BEL][HOL] e #2-[ALE][BEL][HOL]) ou criar novo ad set/campanha com audience testada.

**Ação concreta:** aumentar budget diário da campanha [CPL][EUROPA] em ~€10-15/dia para corrigir o déficit de ritmo sem comprometer eficiência.

---

## Módulo 5 — Fadiga de Criativos

| Anúncio | Freq. Atual | Freq. Ant. | CTR | Leads | Status | Recomendação |
|---|---|---|---|---|---|---|
| AD07 | 1,77 | 1,57 | 2,46% | 10 | 🟢 OK | Manter — frequência saudável, melhor CTR da conta |
| AD06 | 1,74 | 1,10* | 2,04% | 6 | 🟢 OK | Manter — frequência baixa, espaço para crescer |
| AD10 - [IMG] [PROPRIEDADES PREMIUM] — Cópia | 1,71 | 1,69 | 1,95% | 12 | 🟢 OK | Manter — estável, principal entregador do México |
| [CPL][EUROPA] (campanha agregada) | 2,04 | 1,93 | 2,32% | 16 | 🟡 Monitorar | Frequência subindo — acompanhar semana que vem |
| AD15 - [IMG] [para unos pocos] novo | 1,10 | — | 2,13% | 0 | 🔴 CRÍTICO | Baixa frequência mas CPM altíssimo — problema de entrega, não fadiga |
| AD05 | 1,10 | 1,08 | 0,00% | 0 | ⚪ Insuficiente | Gasto <€2 — sem base para análise |

> *AD06 estava em fase inicial na semana anterior (€3,31 de gasto, freq. 1,10)

**Escala de referência:** < 1,8 = OK | 1,8–2,5 = Monitorar | 2,5–3,5 = Atenção | > 3,5 = Fadiga crítica

> ⚠️ **Nota sobre o sumário:** os dados agregados do summary indicam `freq_s: 3,76` e `avg_freq: 1,88`. O valor 3,76 parece ser a soma das frequências das duas campanhas (não a média ponderada), enquanto 1,88 representa a média real por campanha. Nenhum criativo individual está em fadiga — a frequência média de 1,88 está dentro da faixa saudável.

---

## Módulo 6 — Análise de Copy e Criativos

### 🏆 Criativos Vencedores (mínimo 5 leads)

**1º lugar — AD06 ([CPL][EUROPA])**
- CPL €7,02 com **6 leads** | Gasto €42,09 | CTR 2,04% | CPM €10,75 | Freq. 1,74
- Melhor CPL da conta nesta semana
- Frequência baixa = amplo espaço para escala sem risco de fadiga
- Ad set #2-[ALE][BEL][HOL] com €42,31 — indica que o criativo está bem calibrado para o público europeu
- **Recomendação:** testar aumento de budget no ad set #2-[ALE][BEL][HOL]

**2º lugar — AD07 ([CPL][EUROPA])**
- CPL €9,46 com **10 leads** | Gasto €94,62 | CTR 2,46% | CPM €9,91 | Freq. 1,77
- Maior volume de leads da conta; melhor CTR geral (2,46%)
- CPM mais barato de todos os criativos ativos (€9,91)
- Na semana anterior: 3 leads a €20,30 — melhora expressiva e consistente com o volume maior
- **Recomendação:** manter como principal entregador da [CPL][EUROPA]; monitorar se CPL sustenta com escala

**3º lugar — AD10 - [IMG] [PROPRIEDADES PREMIUM] — Cópia (México)**
- CPL €11,92 com **12 leads** | Gasto €143,01 | CTR 1,95% | CPM €11,95 | Freq. 1,71
- Único criativo ativo no México com resultado confirmado — consistente (12 leads nas duas semanas)
- CPL melhorou (€13,13 → €11,92) graças à queda do CPM
- **Recomendação:** manter; avaliar refresh de copy para melhorar CTR (abaixo de 2% é fraco comparado à Europa)

---

### 🔴 Criativos para Pausar

| Anúncio | Motivo |
|---|---|
| AD15 - [IMG] [para unos pocos] novo | €5,34 gastos, 0 leads, CPM €37,87 (3,4× a média) — algoritmo não consegue entregar com eficiência; pausar e revisar criativo/público |
| AD05 ([CPL][EUROPA]) | €1,41 gastos, 0 leads, CTR 0% — sem nenhuma interação; dados insuficientes mas tendência ruim (semana anterior: €0,42 e 0 leads também) |

### ⚪ Dados Insuficientes — Aguardar

- **AD010** (ambas as entradas): gasto total de €0,77, CPMs anômalos (€30–44) — verificar nomenclatura duplicada antes de qualquer decisão

---

## Módulo 7 — Análise de Ad Sets e Públicos

| Ad Set | Campanha | Gasto | Leads | CPL | CTR | CPM | Freq. | Status |
|---|---|---|---|---|---|---|---|---|
| [ALE][BEL][HOL] | [CPL][EUROPA] | €96,58 | 10 | €9,66 | 2,43% | €10,00 | 1,78 | 🟢 OK |
| #2 - [ALE][BEL][HOL] | [CPL][EUROPA] | €42,31 | 6 | €7,05 | 2,04% | €10,80 | 1,74 | 🟢 OK |
| [PS - Cidades x Rico X México] | DK - MEXICO | €143,01 | 12 | €11,92 | 1,95% | €11,95 | 1,71 | 🟢 OK |
| #2 - [PS - Cidades x Rico X México] | DK - MEXICO | €5,34 | 0 | — | 2,13% | €37,87 | 1,10 | 🔴 CRÍTICO |

**Observações:**

- **Sobreposição de público:** [ALE][BEL][HOL] e #2-[ALE][BEL][HOL] segmentam os mesmos países (Alemanha, Bélgica, Holanda) dentro da mesma campanha. Isso cria **competição de leilão interno** — os dois ad sets disputam o mesmo inventário, o que pode inflar o CPM de ambos. Recomenda-se avaliar se a separação está baseada em segmentação diferente (interesse vs. lookalike, por exemplo) ou se são de fato públicos sobrepostos.
- **#2-[PS - Cidades x Rico X México]:** CPM de €37,87 vs €11,95 do principal — 3,2× mais caro para o mesmo público (México). Indica problema de entrega ou audience muito restrita. Pausar.
- **CPMs europeus** (€10,00–€10,80) estão bem abaixo dos mexicanos (€11,95), o que explica parte da vantagem de CPL da Europa nesta semana.

---

## Plano de Ação

| Prioridade | Ação | Impacto | Prazo |
|---|---|---|---|
| 🔴 P1 | Pausar AD15 - [IMG] [para unos pocos] novo e ad set #2-[PS - Cidades x Rico X México] — CPM €37,87, 0 leads, €5,34 desperdiçados | Elimina vazamento de budget; redireciona verba para criativos eficientes | Hoje |
| 🔴 P2 | Aumentar budget diário de [CPL][EUROPA] em €10–15/dia para corrigir pacing 🟡 LENTO (projeção €1.231 vs budget €1.500) | Recupera ~€270 de budget subutilizado em agosto | Hoje |
| 🟡 P3 | Investigar nomenclatura duplicada "AD010" na campanha [CPL][EUROPA] — dois anúncios com mesmo nome, CPMs anômalos (€30–44) | Evita confusão de relatório; identifica se há verba sendo desperdiçada | 24h |
| 🟡 P4 | Verificar sobreposição de público entre [ALE][BEL][HOL] e #2-[ALE][BEL][HOL] — mesma segmentação geográfica pode gerar competição interna de leilão | Potencial redução de CPM e melhora de eficiência | 24–48h |
| 🟡 P5 | Desenvolver novo criativo para campanha México — AD10 está sozinho, CTR de 1,95% tem espaço para melhora; testar variação de copy/angle | Reduz dependência de um único criativo; potencial de CPL abaixo de €10 | 48–72h |
| 🟢 P6 | Monitorar AD06 e AD07 na semana seguinte para confirmar sustentabilidade do CPL abaixo de €9 com escala | Valida se é tendência real antes de escalar orçamento agressivamente | Próxima semana |

---

## Bloco Trello

---

**Meta Ads Leblon Real Estate — 06/08/2026**
**Gasto:** €287,24 | **Leads:** 28 | **CPL:** €10,26
**Variação vs semana anterior:** CPL -24,2% 🟢 | Leads +27,3% 🟢
**Pacing:** 🟡 LENTO — Projeção €1.231 vs Budget €1.500 (19,4% do mês decorrido)

---

📌 **CONTEXTO DA SEMANA**
A conta tinha apenas 2 campanhas ativas nesta semana — sem mudanças estruturais relevantes. O movimento principal foi o amadurecimento dos criativos AD06 e AD07 na campanha [CPL][EUROPA]: ambos estavam em fase inicial na semana anterior (poucos euros gastos, sem volume) e desta vez receberam budget real. Isso explica grande parte da melhora de resultado. Paralelamente, um novo anúncio (AD15) foi adicionado à campanha México mas entregou com CPM altíssimo (€37,87) e sem nenhum lead.

---

📊 **PANORAMA DA SEMANA**

🔍 **Campanhas & Anúncios**
Duas campanhas ativas: **[CPL][EUROPA]** (Alemanha/Bélgica/Holanda) e **DK-México** (Cidades ricas do México). A Europa liderou com 16 leads e CPL €8,68, sustentada por AD07 (10 leads, €9,46) e AD06 (6 leads, €7,02) — os dois principais criativos da conta no momento. O México entregou 12 leads estáveis pelo AD10, mas o novo criativo AD15 consumiu €5,34 sem retorno algum.

📉 **Causa Raiz do CPL**
O CPL da conta caiu de €13,53 para €10,26 por dois motivos combinados: (1) o CPM médio caiu €1,77 — o algoritmo encontrou entrega mais barata, especialmente na Europa onde o CPM chegou a €9,91; (2) o AD06 e AD07 da [CPL][EUROPA] entraram em volume real ao mesmo tempo, com CTR acima de 2%, o que baixou o custo por conversão da campanha de €14,01 para €8,68. Na semana anterior, a Europa ainda estava "testando" esses criativos — desta vez eles entregaram resultado concreto.

⚠️ **Anomalias**
- 🔴 AD15 ([IMG] [para unos pocos] novo) — €5,34 gastos, 0 leads, CPM €37,87 (3,4× a média da conta). O algoritmo não está conseguindo entregar o anúncio com eficiência — sinal claro de problema no criativo ou no público-alvo do ad set #2-[PS-Cidades x Rico x México], que tem CPM idêntico.
- ⚠️ Dois anúncios "AD010" na campanha Europa com CPMs de €30–44 e gasto mínimo (€0,77 total) — verificar se é erro de nomenclatura ou duplicata real.

📅 **Pacing**
No ritmo atual (€41/dia), agosto encerrará com ~€1.231 — €269 abaixo do budget de €1.500, aproveitando apenas 82% da verba disponível. Parte da perda vem do ad set #2-México com CPM anômalo consumindo budget sem gerar leads. A ação correta não é apenas pausar os ineficientes: é aumentar o budget diário da [CPL][EUROPA] em €10–15/dia, que hoje está convertendo bem a €8,68/lead e tem frequência baixa (1,78–2,04) com espaço de escala.

😴 **Fadiga de Criativos**
Situação saudável: todos os criativos ativos com resultado estão abaixo de 1,80 de frequência. A campanha Europa como um todo está em 2,04 — zona de monitoramento, mas ainda longe de fadiga. Nenhuma ação necessária esta semana; verificar novamente se a frequência da Europa ultrapassar 2,5 na próxima semana.

🎨 **Criativos**
- 🏆 **Vencedor principal:** AD06 — CPL **€7,02 com 6 leads** (imagem, Europa)
- 📈 **Melhor volume:** AD07 — CPL €9,46 com **10 leads** (Europa) — candidato a escalar com aumento de budget
- ✅ **Estável:** AD10 - [IMG] [PROPRIEDADES PREMIUM] — CPL €11,92 com **12 leads** (México) — único criativo ativo no México com resultado
- 🔴 **Pausar imediatamente:** AD15 - [IMG] [para unos pocos] novo — €5,34 gastos, 0 leads, CPM €37,87
- ⏳ **Dados insuficientes (aguardar):** AD05, AD010 (ambas as entradas)

🎯 **Ad Sets & Públicos**
CPMs europeus (~€10) estão abaixo dos mexicanos (~€12), favorecendo o CPL da Europa. Existe um risco de sobreposição entre [ALE][BEL][HOL] e #2-[ALE][BEL][HOL] — dois ad sets targeting os mesmos países na mesma campanha podem competir no leilão e inflar CPMs mutuamente. Verificar se há diferença real de segmentação entre eles.

---

🚀 **PRÓXIMOS PASSOS**
- 🔴 Pausar AD15 e ad set #2-[PS - Cidades x Rico x México] — CPM €37,87, 0 leads, €5,34 desperdiçados — **hoje**
- 🔴 Aumentar budget diário de [CPL][EUROPA] em €10–15/dia para corrigir pacing 🟡 LENTO e recuperar os €269 de budget subutilizado — **hoje**
- 🟡 Investigar e corrigir nomenclatura duplicada "AD010" na campanha Europa — **24h**
- 🟡 Verificar sobreposição de público entre [ALE][BEL][HOL] e #2-[ALE][BEL][HOL] para eliminar competição interna de leilão — **24–48h**
- 🟢 Desenvolver novo criativo para o México (AD10 está sozinho com CTR abaixo de 2%) e testar variação de angle/copy — **até 72h**

---