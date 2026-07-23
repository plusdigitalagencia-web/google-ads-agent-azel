# Relatório Meta Ads - Alcala Homes
**Período atual:** 16/07/2026 a 22/07/2026
**Período anterior:** 09/07/2026 a 15/07/2026
**Gerado em:** 23/07/2026 | **Conta:** act_574789065003576

---

## Resumo Executivo

| Métrica | Atual | Anterior | Variação |
|---|---|---|---|
| Gasto | €156,92 | €280,60 | -44,1% 📉 |
| Leads | 11 | 64 | -82,8% 📉 |
| CPL | €14,27 | €4,38 | +225,8% 📉 |
| CPM médio | €17,95 | €13,05 | +37,5% 📉 |
| CTR médio | 1,48% | 2,22% | -33,3% 📉 |
| Frequência média | 1,81 | 1,67 | +8,4% ↗️ |
| Campanhas ativas | 1 | 2 | -1 ⚠️ |

> ⚠️ **Alerta crítico:** A campanha "Vietnam \| RevoTravel \| I TG 02" esteve ativa na semana anterior e gerou 59 de 64 leads (92%) ao CPL de €2,59. O encerramento/pausa dessa campanha explica diretamente a queda de 82,8% em leads e a disparada do CPL de €4,38 para €14,27.

---

## Módulo 1 - Auditoria de Campanhas e Anúncios

### Campanhas

| Campanha | Gasto | Leads | CPL | CTR | CPM | Freq. | Status |
|---|---|---|---|---|---|---|---|
| \[Data Know\] Bélgica+Hol+RU | €156,92 | 11 | €14,27 | 1,48% | €17,95 | 1,81 | 🟡 ATENÇÃO |
| Vietnam \| RevoTravel \| I TG 02 | €0 | 0 | — | — | — | — | ⛔ INATIVA |

> 🔴 **Nota crítica:** Com apenas 1 campanha ativa, a conta opera em modo de risco elevado. O CPL de €14,27 está 225% acima do CPL consolidado da semana anterior (€4,38). A média da conta nesta semana é €14,27 (única campanha ativa).

---

### Anúncios por Campanha

**Campanha: \[Data Know\] \[Form Meta Lead\] \[Bélgica+Hol+Reino Unido\] - 26/06/26**

| Anúncio | Gasto | Leads | CPL | CTR | CPM | Freq. | Status |
|---|---|---|---|---|---|---|---|
| img2_flats_in_madrid | €97,45 | 10 | €9,75 | 1,49% | €16,88 | 1,62 | 🟢 OK |
| img4_luxury_living_madrid | €25,63 | 1 | €25,63 | 1,85% | €19,81 | 1,36 | 🟡 ATENÇÃO |
| img5_madri_homes | €27,13 | 0 | — | 1,34% | €20,23 | 1,47 | 🔴 CRÍTICO |
| img1_looking_for_a_luxury | €2,76 | 0 | — | 0,63% | €17,36 | 1,25 | ⚪ Dados insuficientes |
| img3_invest_your_wealth | €3,95 | 0 | — | 0,00% | €22,57 | 1,28 | 🔴 CRÍTICO |

> **img5_madri_homes:** €27,13 gastos, 0 leads — ultrapassa o threshold de €15 sem conversão → 🔴 CRÍTICO
> **img3_invest_your_wealth:** €3,95 gastos, CTR 0,00% — ainda abaixo de €15, mas sem nenhum clique → sinal muito negativo
> **img1_looking_for_a_luxury:** €2,76 gastos — gasto < €3, não baseamos recomendações neste dado ainda

---

## Módulo 2 - Diagnóstico de CPL (Causa Raiz)

### Campanha: \[Data Know\] \[Form Meta Lead\] \[Bélgica+Hol+Reino Unido\]

**CPL atual: €14,27 vs CPL anterior nesta mesma campanha: €25,55**

Paradoxalmente, o CPL *desta campanha específica* melhorou semana a semana (de €25,55 para €14,27). Porém o CPL da conta explodiu porque a campanha Vietnam — que puxava a média para baixo com €2,59 — foi encerrada.

**Causa raiz do CPL elevado na conta:**
1. **Campanha Vietnam pausada/encerrada** → responsável por 59/64 leads (92%) na semana anterior. Sem ela, a conta opera só com o segmento de imóveis de luxo, cujo CPL estrutural é €9–25.
2. **Budget concentrado em criativos sem conversão:** €27,13 (img5) + €3,95 (img3) + €2,76 (img1) = €33,84 (21,6% do gasto semanal) com 0 leads gerados.
3. **CTR abaixo do período anterior:** 1,48% vs 2,22% da conta como um todo — indica que os criativos ativos não estão capturando atenção suficientemente. Mesmo o melhor criativo (img2) opera a 1,49%.
4. **CPM ligeiramente elevado:** €17,95 vs €16,88 do img2 — o sistema está distribuindo budget para criativos menos eficientes (img5 a €20,23 CPM), encarecendo o custo médio.
5. **Estrutura de 1 único ad set Advantage+:** sem possibilidade de comparar públicos ou isolar variáveis.

**Equação do CPL explicada:**
- €1.000 de CPM ÷ CTR 1,48% = CPC ~€1,21
- Taxa de conversão implícita: 11 leads / ~13.000 cliques estimados → taxa baixa, sugerindo que o formulário ou a proposta não ressoa com o público de Bélgica+Holanda+RU tão bem quanto o produto Vietnam ressoa com seu público.

---

## Módulo 3 - Detecção de Anomalias

| Tipo | Anúncio | Detalhe | Ação Recomendada |
|---|---|---|---|
| 🔴 Zero leads com gasto alto | img5_madri_homes | €27,13 gastos, 0 leads (threshold: >€15) | Pausar imediatamente |
| 🔴 CTR zero + gasto | img3_invest_your_wealth | CTR 0,00% com €3,95 gastos | Pausar — sem nenhum clique |
| 🔴 Campanha desaparecida | Vietnam \| RevoTravel \| I TG 02 | Gerava 59 leads/semana ao CPL €2,59 — ausente esta semana | Investigar causa e reativar se possível |
| 🟡 Budget mal distribuído | Ad Set Advantage+ | 21,6% do gasto em criativos com 0 leads | Revisar lógica de otimização do Advantage+ |
| ⚪ CPM anômalo (sem dado atual) | img1_looking_for_a_luxury | CPM era €57,14 na semana anterior (outlier extremo) — caiu para €17,36 atual | Monitorar; pode ter sido erro de leilão pontual |

> **Comparativo semana anterior:**
> - img2_flats_in_madrid: CPL melhorou de €23,30 → €9,75 (+CTR 1,33% → 1,49%) ✅
> - img4_luxury_living_madrid: CPL piorou de €18,25 → €25,63 (1 lead apenas) ⚠️
> - img5_madri_homes: manteve 0 leads com gasto maior (€17,94 → €27,13) 🔴 Piora confirmada

---

## Módulo 4 - Pacing Monitor

| Parâmetro | Valor |
|---|---|
| Dia do mês | 23 de 31 |
| % do mês decorrido | 74,2% |
| Gasto até agora (mês) | ~€443 (estimado) |
| Projeção mensal | €672,51 |
| Budget mensal | €600,00 |
| Diferença projeção vs budget | +12,1% |
| Status | 🔴 ACELERADO |

> **Análise:** A projeção de €672,51 supera o budget em €72,51 (+12,1%), ultrapassando o threshold de 10%. Com 74,2% do mês decorrido, o ritmo atual aponta para um estouro de budget. Ação necessária: reduzir o budget diário da campanha ativa em ~15% ou monitorar diariamente para pausar quando atingir €600.

---

## Módulo 5 - Fadiga de Criativos

| Anúncio | Freq. Atual | Freq. Anterior | CTR | Leads | Status | Recomendação |
|---|---|---|---|---|---|---|
| img2_flats_in_madrid | 1,62 | 1,75 | 1,49% | 10 | 🟢 OK | Manter — frequência saudável |
| img5_madri_homes | 1,47 | 1,39 | 1,34% | 0 | 🟢 OK (freq.) | Pausar por 0 leads, não por fadiga |
| img4_luxury_living_madrid | 1,36 | 1,36 | 1,85% | 1 | 🟢 OK | Aguardar mais dados |
| img3_invest_your_wealth | 1,28 | 1,38 | 0,00% | 0 | 🟢 OK (freq.) | Pausar por CTR zero |
| img1_looking_for_a_luxury | 1,25 | 1,17 | 0,63% | 0 | 🟢 OK | Dados insuficientes (€2,76) |

> **Conclusão:** Nenhum criativo apresenta fadiga por frequência nesta semana. Todas as frequências estão abaixo de 1,8. Os problemas de performance são de relevância/conversão, não de saturação de público.

**Escala de referência:** < 1,8 = OK | 1,8–2,5 = Monitorar | 2,5–3,5 = Atenção | > 3,5 = Fadiga

---

## Módulo 6 - Análise de Copy e Criativos

### 🏆 Criativo Vencedor

**img2_flats_in_madrid**
- CPL €9,75 com **10 leads** (único com volume suficiente para conclusão estatística)
- Gasto: €97,45 | CTR: 1,49% | CPM: €16,88 | Frequência: 1,62
- Evolução positiva: na semana anterior teve CPL €23,30 com apenas 3 leads — melhora de 58% no CPL
- **Formato:** Imagem
- **Por que funciona:** Mensagem direta ("flats in Madrid") com proposta clara para o público de Bélgica/Holanda/RU buscando imóveis. CPM mais baixo do grupo (€16,88) indica melhor relevância no leilão.

### 📊 Criativos com Dados Insuficientes (aguardar)

| Criativo | Gasto | Leads | Situação |
|---|---|---|---|
| img4_luxury_living_madrid | €25,63 | 1 | CPL €25,63 — apenas 1 lead, sem significância estatística |
| img1_looking_for_a_luxury | €2,76 | 0 | Gasto < €3 — não há base para conclusão |

### 🔴 Criativos para Pausar Imediatamente

| Criativo | Motivo | Gasto | Leads |
|---|---|---|---|
| img5_madri_homes | €27,13 gastos + 0 leads (>€15 sem conversão) — anomalia confirmada 2 semanas seguidas | €27,13 | 0 |
| img3_invest_your_wealth | CTR 0,00% — nenhum clique gerado; sem sinal de relevância | €3,95 | 0 |

> ⚠️ **Nota de consistência:** img5_madri_homes e img3_invest_your_wealth estão marcados como 🔴 CRÍTICO no Módulo 1 e como anomalias no Módulo 3 — não são candidatos a escala.

---

## Módulo 7 - Análise de Ad Sets e Públicos

### Ad Sets Ativos

| Ad Set | Campanha | Gasto | Leads | CPL | CTR | CPM | Freq. |
|---|---|---|---|---|---|---|---|
| 01/Advantage+ Compradores | Bélgica+Hol+RU | €156,92 | 11 | €14,27 | 1,48% | €17,95 | 1,81 |

### Observações

- **Único ad set ativo:** Sem possibilidade de comparação entre públicos. Se o Advantage+ não encontrar os compradores mais qualificados, todo o budget fica exposto ao risco.
- **Advantage+ Compradores:** O algoritmo está distribuindo budget de forma ineficiente — 21,6% do gasto foi para criativos com 0 leads. Isso pode indicar que o algoritmo ainda está em fase de aprendizado com os novos criativos ou que a sinalização de conversão é fraca (apenas 11 leads na semana).
- **CPM €17,95:** Coerente com público premium de imóveis de luxo em Bélgica/Holanda/RU. Não é anômalo para o segmento — o problema não está no custo de impressão, mas na taxa de conversão post-clique.
- **Sem risco de sobreposição:** Apenas 1 ad set ativo.
- **Recomendação:** Considerar criar um segundo ad set com público manual (interesses: imóveis, investimento imobiliário, expatriados) para comparar com o Advantage+.

---

## Plano de Ação

| Prioridade | Ação | Impacto | Prazo |
|---|---|---|---|
| 🔴 P1 | Pausar img5_madri_homes (€27,13 + 0 leads, 2 semanas sem conversão) | Elimina desperdício de ~17% do budget semanal | Hoje |
| 🔴 P2 | Pausar img3_invest_your_wealth (CTR 0,00%, sem relevância) | Elimina custo sem retorno | Hoje |
| 🔴 P3 | Investigar status da campanha Vietnam \| RevoTravel — reativar se possível | Potencial de recuperar 59 leads/semana ao CPL €2,59 | Hoje |
| 🔴 P4 | Reduzir budget diário em ~15% para evitar estouro (projeção €672 vs budget €600) | Controle de budget — evita gastar €72 além do aprovado | Hoje |
| 🟡 P5 | Aumentar budget do img2_flats_in_madrid (único vencedor com 10 leads) | Escalar o criativo que converte — potencial de dobrar leads | 24–48h |
| 🟡 P6 | Criar novos criativos para substituir os pausados (2–3 variações de img2) | Manter volume de teste sem desperdiçar em criativos mortos | 48–72h |
| 🟡 P7 | Criar ad set com público manual para comparar com Advantage+ | Isolar se o problema é o criativo ou o público | 48–72h |
| 🟢 P8 | Aguardar img4_luxury_living_madrid atingir 5+ leads antes de decisão | Evitar pausar criativo que pode ainda converter | Semana que vem |

---

## Bloco Trello

```
Meta Ads Alcala Homes - 23/07/2026
Gasto: €156,92 | Leads: 11 | CPL: €14,27
Variação vs semana anterior: CPL +225,8% 📉 | Leads -82,8% 📉
Pacing: 🔴 ACELERADO — Projeção €672,51 vs Budget €600,00 (74,2% do mês decorrido)
```

---

**📌 CONTEXTO DA SEMANA**

A mudança mais crítica desta semana foi o encerramento (ou pausa) da campanha "Vietnam | RevoTravel | I TG 02", que na semana anterior foi responsável por 59 dos 64 leads totais da conta ao CPL de €2,59. Com ela fora do ar, a conta opera agora exclusivamente com a campanha de imóveis de luxo para Bélgica/Holanda/RU, cujo CPL estrutural está entre €10–25 — um produto fundamentalmente mais caro de gerar leads. Isso cria a ilusão de colapso na conta, quando na verdade são dois produtos e mercados completamente distintos.

---

**📊 PANORAMA DA SEMANA**

**🔍 Campanhas & Anúncios**
Apenas 1 campanha ativa esta semana: [Data Know] [Form Meta Lead] [Bélgica+Hol+Reino Unido], com 1 ad set (Advantage+ Compradores) e 5 criativos rodando. Desses 5, apenas img2_flats_in_madrid está gerando resultado real (10 leads, CPL €9,75). Os demais dividem €56,47 de budget entre si e produziram apenas 1 lead combinados — uma ineficiência severa que está inflando o CPL médio da conta.

**📉 Causa Raiz do CPL**
O CPL de €14,27 tem duas causas principais. A primeira e mais impactante é estrutural: a campanha Vietnam, que puxava o CPL da conta para €4,38, está encerrada. A segunda é operacional: dentro da campanha ativa, 21,6% do budget semanal (€33,84) foi consumido por img5_madri_homes e img3_invest_your_wealth, que juntos geraram 0 leads. O criativo que funciona (img2) recebeu 62% do budget e gerou 91% dos leads — o Advantage+ está parcialmente acertando, mas ainda distribui demais para criativos ineficientes. O CPM de €17,95 não é o problema; a taxa de conversão post-clique (CTR 1,48% com baixa conversão) é.

**⚠️ Anomalias**
- 🔴 img5_madri_homes: €27,13 gastos + 0 leads pela segunda semana consecutiva — pausa imediata
- 🔴 img3_invest_your_wealth: CTR 0,00% — nenhum usuário clicou; sem sinal de relevância
- 🔴 Campanha Vietnam desaparecida: ausência inexplicada nos dados — precisa de verificação urgente (era responsável por 92% dos leads da conta)
- 🟡 Budget mal alocado pelo Advantage+: 3 criativos com 0 leads absorvem 21% do gasto

**📅 Pacing**
No ritmo atual, julho encerrará com €672,51 gastos contra um budget de €600 — um estouro de €72 (+12,1%). Com 74,2% do mês decorrido já no dia 23/07, há apenas 8 dias restantes e ainda há margem de ~€157 disponível se o budget fosse respeitado linearmente (€443 gastos estimados até agora). Ação imediata: reduzir o budget diário da campanha ativa em aproximadamente 15% para os dias restantes do mês, ou estabelecer um cap de gasto diário de ~€19–20 para os 8 dias finais.

**😴 Fadiga de Criativos**
Nenhum criativo apresenta fadiga por frequência. Todas as frequências estão abaixo de 1,8 (img2 em 1,62, o mais alto). Os problemas de performance são de relevância e conversão — não de saturação do público. A conta tem espaço para servir os mesmos criativos por mais tempo sem risco de fadiga.

**🎨 Criativos**
- **Vencedor principal:** img2_flats_in_madrid — CPL €9,75 com **10 leads** (imagem) — único com significância estatística
- **Candidato a escalar:** img2_flats_in_madrid merece aumento de budget após pausar os criativos ineficientes
- **Para pausar:** img5_madri_homes — €27,13 com 0 leads por 2 semanas (anomalia confirmada); img3_invest_your_wealth — CTR 0,00%, sem nenhuma interação
- **Dados insuficientes (aguardar):** img4_luxury_living_madrid (1 lead), img1_looking_for_a_luxury (€2,76 gastos)

**🎯 Ad Sets & Públicos**
Único ad set ativo: Advantage+ Compradores, com CPM €17,95 — adequado para o segmento de imóveis de luxo em mercados premium (Bélgica, Holanda, Reino Unido). Não há risco de sobreposição com 1 único ad set. O maior risco é a falta de redundância: se o Advantage+ errar na alocação, não há ad set alternativo para compensar. Recomenda-se criar um segundo ad set com público manual para teste.

---

**🚀 PRÓXIMOS PASSOS**
- 🔴 Pausar img5_madri_homes e img3_invest_your_wealth hoje — eliminam €31+ de desperdício/semana
- 🔴 Investigar e reativar campanha Vietnam | RevoTravel — era responsável por 92% dos leads da conta ao CPL €2,59
- 🔴 Reduzir budget diário em ~15% para os próximos 8 dias — evitar estouro de €72 acima do budget aprovado
- 🟡 Realocar budget liberado dos criativos pausados para img2_flats_in_madrid (único vencedor confirmado) e testar 2–3 novas variações criativas
- 🟢 Criar ad set com público manual como alternativa ao Advantage+ para isolar variável de público vs. criativo