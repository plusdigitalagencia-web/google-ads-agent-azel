# Relatório Meta Ads — Onvoix
**Período atual:** 30/07/2026 a 05/08/2026
**Período anterior:** 23/07/2026 a 29/07/2026
**Gerado em:** 06/08/2026 | **Conta:** act_1297650828540575

---

## Resumo Executivo

| Métrica | Atual | Anterior | Variação |
|---|---|---|---|
| Gasto | $227,04 | $122,24 | +$104,80 (+85,7%) 📈 |
| Leads | 270 | 150 | +120 (+80,0%) 📈 |
| CPL | $0,84 | $0,81 | +$0,03 (+3,7%) 🟡 |
| CPM | $3,21 | $3,77 | -$0,56 (-14,9%) 📈 |
| CTR | 3,52% | 5,33% | -1,81 p.p. (-34,0%) 📉 |
| Frequência | 1,60 | 1,27 | +0,33 (+26,0%) 🟡 |

> **Leitura rápida:** A conta escalonou fortemente — gasto +86%, leads +80%. O volume é saudável e o CPL se manteve praticamente estável ($0,84 vs $0,81). A queda de CTR (5,33% → 3,52%) reflete a mudança de mix: criativos de imagem com CTR menor passaram a dominar o budget. CPM caiu 15%, o que compensou parcialmente a perda de CTR e manteve o CPL controlado.

---

## Módulo 1 — Auditoria de Campanhas e Anúncios

### Campanhas

| Campanha | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| Site - México — Registro | $227,04 | 270 | $0,84 | 3,52% | $3,21 | 1,60 | 🟢 OK |

> CPL médio da conta: **$0,84**. Threshold 🟡 ATENÇÃO: >$1,09. Threshold 🔴 CRÍTICO: >$1,68.

---

### Anúncios por Campanha — Site - México — Registro

> ⚠️ **Nota sobre duplicação de nomes:** Os dados contêm dois registros "Ima 02 — Cópia" e dois registros "Ima 03 — Cópia" — cada par está em ad sets diferentes (México amplo vs México amplo Evento Onboarding). Para clareza, serão identificados como **[amplo]** e **[Onboarding]** respectivamente.

| Anúncio | Ad Set | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|---|
| Ima 03 — Cópia [Onboarding] | Onboarding | $4,67 | 10 | **$0,47** | 2,96% | $3,07 | 1,16 | 🟢 OK |
| VID 01 — Cópia [Onboarding] | Onboarding | $16,30 | 28 | **$0,58** | 6,38% | $4,49 | 1,14 | 🟢 OK |
| Ima 02 — Cópia [Onboarding] | Onboarding | $75,32 | 100 | **$0,75** | 3,42% | $3,20 | 1,20 | 🟢 OK |
| Ima 04 — Cópia [Onboarding] | Onboarding | $104,17 | 111 | **$0,94** | 2,42% | $2,69 | 1,73 | 🟢 OK |
| VID 01 — Cópia [amplo] | México amplo | $23,38 | 19 | $1,23 | 16,49% | $8,68 | 1,07 | 🟡 ATENÇÃO |
| Ima 02 — Cópia [amplo] | México amplo | $2,95 | 2 | $1,48 | 4,49% | $5,76 | 1,20 | ⚠️ insuf. |
| Ima 03 — Cópia [amplo] | México amplo | $0,01 | 0 | — | 0,00% | $3,33 | 1,00 | ⚠️ insuf. |
| Ima 01 — Cópia [Onboarding] | Onboarding | $0,24 | 0 | — | 2,11% | $2,53 | 1,12 | ⚠️ insuf. |

> Criativos com gasto < $3 ou leads < 3: dados insuficientes para decisão — monitorar.

---

## Módulo 2 — Diagnóstico de CPL (Causa Raiz)

### Site - México — Registro

**CPL atual: $0,84 (+3,7% vs semana anterior)**

O CPL subiu marginalmente, mas a causa raiz não é deterioração do criativo principal — é uma **mudança de mix de tráfego**:

| Fator | Semana Anterior | Semana Atual | Impacto no CPL |
|---|---|---|---|
| CPM | $3,77 | $3,21 | ✅ Melhora (-15%) |
| CTR | 5,33% | 3,52% | ❌ Piora (-34%) |
| Frequência | 1,27 | 1,60 | ⚠️ Subindo |

**Decomposição:**
- **O CPM caiu 15%:** O ad set "México amplo Evento Onboarding" ($200,70 — 88% do budget) possui CPM muito baixo ($2,98), indicando público mais amplo e barato.
- **O CTR caiu 34%:** Os criativos de imagem que dominam o Onboarding têm CTR entre 2,42%–3,42%, bem abaixo do VID 01 (6,38%). O mix se deslocou de vídeo (alta taxa de clique) para imagem (menor CTR, mas CPM menor ainda compensou).
- **Resultado líquido:** CPM mais barato compensou CTR menor → CPL ficou praticamente estável.
- **Risco futuro:** Se a frequência continuar subindo (já em 1,60), o CTR tende a cair mais sem contrapartida de CPM menor, pressionando o CPL para cima.

---

## Módulo 3 — Detecção de Anomalias

| Tipo | Anúncio | Detalhe | Ação |
|---|---|---|---|
| 🟡 CPM elevado vs conta | VID 01 — Cópia [amplo] | CPM $8,68 vs média da conta $3,21 (+170%) | Monitorar ROI do ad set México amplo; avaliar pausar se CPL se mantiver >$1,20 |
| 🟡 CTR muito alto sem volume | VID 01 — Cópia [amplo] | CTR 16,49% com apenas $23 gastos e 19 leads | Dados estatisticamente cedo; aguardar mais volume antes de escalar |
| ⚠️ Gasto residual sem leads | Ima 03 — Cópia [amplo] | $0,01 gasto, 0 leads, 0% CTR | Verificar se está ativo por engano; pausar se não houver entrega planejada |
| ⚠️ Gasto residual sem leads | Ima 01 — Cópia [Onboarding] | $0,24 gasto, 0 leads | Gasto insuficiente para conclusão; monitorar entrega |
| 🟡 Concentração de budget | Ima 04 + Ima 02 [Onboarding] | $179,49 = 79% do gasto total em 2 criativos | Saudável em volume, mas risco se um deles degradar |

---

## Módulo 4 — Pacing Monitor

| Parâmetro | Valor |
|---|---|
| Dia do mês | 6 de 31 (19,4% decorrido) |
| Gasto até agora | $227,04 |
| Projeção mensal | $973,03 |
| Budget mensal | $500,00 |
| Status | 🔴 ACELERADO |

**Projeção vs Budget:** +$473,03 (+94,6% acima do budget)

> **Análise:** No ritmo atual, agosto encerrará com ~$973 gastos — quase o **dobro** do budget de $500. Com apenas 19,4% do mês decorrido, já foram gastos $227 (45,4% do budget mensal). O principal driver é o ad set "México amplo Evento Onboarding" com $200,70 em 7 dias. Ação imediata necessária: revisar o budget diário da campanha ou definir teto de gasto semanal para não ultrapassar o limite mensal.

---

## Módulo 5 — Fadiga de Criativos

| Anúncio | Freq | CTR | Leads | Status | Recomendação |
|---|---|---|---|---|---|
| VID 01 — Cópia [Onboarding] | 1,14 | 6,38% | 28 | 🟢 OK | Manter |
| VID 01 — Cópia [amplo] | 1,07 | 16,49% | 19 | 🟢 OK | Manter; aguardar volume |
| Ima 03 — Cópia [Onboarding] | 1,16 | 2,96% | 10 | 🟢 OK | Manter |
| Ima 02 — Cópia [amplo] | 1,20 | 4,49% | 2 | 🟢 OK | Dados insuficientes |
| Ima 02 — Cópia [Onboarding] | 1,20 | 3,42% | 100 | 🟢 OK | Manter; monitorar na semana que vem |
| Ima 01 — Cópia [Onboarding] | 1,12 | 2,11% | 0 | 🟢 OK | Dados insuficientes |
| Ima 03 — Cópia [amplo] | 1,00 | 0,00% | 0 | 🟢 OK | Verificar entrega |
| Ima 04 — Cópia [Onboarding] | 1,73 | 2,42% | 111 | 🟡 Monitorar | Frequência subindo; atenção se ultrapassar 2,0 na próxima semana |

> **Resumo:** Nenhum criativo em fadiga neste momento. Ima 04 — Cópia [Onboarding] é o único que requer monitoramento por frequência (1,73) combinada com o menor CTR dos ativos principais (2,42%). Com o escalonamento atual de budget, pode chegar à zona de atenção (≥2,5) rapidamente.

---

## Módulo 6 — Análise de Copy e Criativos

### 🏆 Criativos Vencedores

| Posição | Anúncio | CPL | Leads | Gasto | Formato | Obs |
|---|---|---|---|---|---|---|
| 🥇 1º | **Ima 03 — Cópia [Onboarding]** | $0,47 | 10 | $4,67 | Imagem | Melhor CPL com volume mínimo atingido |
| 🥈 2º | **VID 01 — Cópia [Onboarding]** | $0,58 | 28 | $16,30 | Vídeo | Excelente CTR (6,38%) + CPL baixo |
| 🥉 3º | **Ima 02 — Cópia [Onboarding]** | $0,75 | 100 | $75,32 | Imagem | Maior volume absoluto; CPL saudável |

**Ima 03 — Cópia [Onboarding]:** CPL $0,47 com 10 leads — melhor eficiência da conta. Gasto ainda baixo ($4,67), mas já atingiu o mínimo estatístico de 5 leads. Candidato a receber mais budget gradualmente.

**VID 01 — Cópia [Onboarding]:** CPL $0,58 com 28 leads — melhor equilíbrio entre eficiência e volume. CTR de 6,38% indica forte relevância criativa. Este é o criativo com maior confiança estatística entre os eficientes.

**Ima 02 — Cópia [Onboarding]:** CPL $0,75 com 100 leads — maior volume da conta. Confiável para escala.

### ⏸️ Criativos para Pausar / Monitorar

| Anúncio | Motivo |
|---|---|
| **Ima 03 — Cópia [amplo]** | $0,01 gasto, 0 leads, 0% CTR — entrega praticamente nula; verificar se está ativo por engano |
| **Ima 02 — Cópia [amplo]** | Apenas 2 leads com $2,95 gastos — dados insuficientes; CPL $1,48 ainda não é conclusivo, mas o ad set [amplo] opera com CPM muito mais caro ($8,21 vs $2,98) |

### ⏳ Dados Insuficientes — Aguardar

- **Ima 01 — Cópia [Onboarding]** — $0,24 gasto, 0 leads
- **VID 01 — Cópia [amplo]** — 19 leads com CPL $1,23 🟡 ATENÇÃO; aguardar volume mínimo, mas ad set [amplo] tem CPM estruturalmente mais caro

---

## Módulo 7 — Análise de Ad Sets e Públicos

| Ad Set | Gasto | Leads | CPL | CTR | CPM | Freq | Status |
|---|---|---|---|---|---|---|---|
| México amplo Evento Onboarding | $200,70 | 249 | **$0,81** | 2,99% | $2,98 | 1,64 | 🟢 OK |
| México amplo | $26,34 | 21 | $1,25 | 14,56% | $8,21 | 1,09 | 🟡 ATENÇÃO |

### Observações

**México amplo Evento Onboarding** é o motor da conta: representa 88% do gasto e 92% dos leads. CPM muito competitivo ($2,98), indicando que o uso de evento de conversão (Onboarding) está permitindo ao algoritmo encontrar usuários mais baratos. CPL $0,81 — está abaixo da média da conta.

**México amplo** opera com CPM quase **3x mais caro** ($8,21 vs $2,98). O CTR excepcionalmente alto (14,56%) sugere que o público está clicando mais, mas o custo por clique ainda resulta em CPL 54% mais caro ($1,25 vs $0,81). Embora ainda dentro do threshold 🟡 ATENÇÃO, o ad set precisa de justificativa estratégica para existir com este diferencial de CPM.

**Sobreposição:** Ambos os ad sets usam "México amplo" como base de público. Há risco de sobreposição de audiência — recomendável verificar no Audience Overlap do Gerenciador de Anúncios e, se confirmado, considerar exclusões ou consolidação.

---

## Plano de Ação

| Prioridade | Ação | Impacto | Prazo |
|---|---|---|---|
| 🔴 P1 | **Reduzir budget diário da campanha** para alinhar projeção ao budget de $500/mês (~$16/dia restantes) — pacing atual projeta $973 | Evitar estouro de budget em 2x | Hoje |
| 🔴 P2 | **Pausar Ima 03 — Cópia [amplo]** ($0,01 gasto, 0 leads, 0% CTR) — verificar se está rodando por erro | Eliminar desperdício | Hoje |
| 🟡 P3 | **Aumentar budget gradual do Ima 03 — Cópia [Onboarding]** — melhor CPL da conta ($0,47, 10 leads); testar com +50% de verba direcionada ao ad set Onboarding | Potencial redução de CPL médio | 24–48h |
| 🟡 P4 | **Investigar sobreposição de público** entre ad sets "México amplo" e "México amplo Evento Onboarding" no Audience Overlap | Evitar leilão interno e inflação de CPM | 24–48h |
| 🟡 P5 | **Avaliar pausar ad set México amplo** — CPM $8,21 vs $2,98 do Onboarding; se o objetivo é volume de leads a menor CPL, o Onboarding domina em todos os KPIs | Otimização de eficiência | 48–72h |
| 🟢 P6 | **Criar alerta de frequência para Ima 04 — Cópia [Onboarding]** — freq 1,73 com maior gasto absoluto; preparar criativo substituto preventivamente | Evitar fadiga futura | Esta semana |

---

## BLOCO TRELLO

---

**Meta Ads Onvoix — 06/08/2026**
**Gasto:** $227,04 | **Leads:** 270 | **CPL:** $0,84
**Variação vs semana anterior:** CPL +3,7% 🟡 | Leads +80,0% 📈
**Pacing:** 🔴 ACELERADO — Projeção $973 vs Budget $500 (19,4% do mês decorrido)

---

### 📌 CONTEXTO DA SEMANA

O volume da conta mais do que dobrou em gasto ($122 → $227) com escalonamento concentrado no ad set "México amplo Evento Onboarding", que passou a receber $200 dos $227 totais. Novos criativos de imagem (Ima 02, Ima 03, Ima 04) foram introduzidos neste ad set e passaram a dominar a entrega, substituindo o VID 01 como criativo principal. Essa mudança de mix explica tanto a queda de CTR quanto a manutenção do CPL.

---

### 📊 PANORAMA DA SEMANA

**🔍 Campanhas & Anúncios**
Apenas uma campanha ativa: "Site - México — Registro", com 8 anúncios rodando em 2 ad sets. O ad set "México amplo Evento Onboarding" domina completamente a entrega (88% do gasto, 92% dos leads). Os criativos mais performáticos são Ima 02 [Onboarding] (100 leads, CPL $0,75), Ima 04 [Onboarding] (111 leads, CPL $0,94) e VID 01 [Onboarding] (28 leads, CPL $0,58). O ad set "México amplo" opera em paralelo com CPM estruturalmente mais caro, gerando leads a $1,25.

**📉 Causa Raiz do CPL**
O CPL subiu marginalmente (+3,7%) não por deterioração criativa, mas por mudança de mix: criativos de imagem com CTR menor (2,42%–3,42%) assumiram a maior parte do budget, reduzindo o CTR médio da conta de 5,33% para 3,52%. A compensação veio do CPM, que caiu 15% ($3,77 → $3,21) — o algoritmo do ad set Onboarding está encontrando tráfego mais barato. O equilíbrio resultou em CPL quase idêntico ao da semana anterior.

**⚠️ Anomalias**
- 🟡 Ad set "México amplo" opera com CPM $8,21 — 175% acima da média da conta ($3,21), gerando CPL $1,25 vs $0,81 do Onboarding
- 🟡 VID 01 — Cópia [amplo]: CTR de 16,49% com apenas $23 gastos — estatisticamente cedo para conclusão, não escalar ainda
- ⚠️ Ima 03 — Cópia [amplo]: $0,01 gasto, 0 leads, 0% CTR — verificar se está ativo por engano

**📅 Pacing**
🔴 CRÍTICO: No ritmo atual, agosto encerrará com $973 gastos contra um budget de $500 — **94,6% acima do planejado**. Com apenas 6 dias de mês, já foram consumidos $227 (45,4% do budget total). A ação mais urgente da semana é ajustar o budget diário para ~$16/dia no restante do mês (ou revisar o budget aprovado com o cliente, caso o volume de leads justifique o investimento extra).

**😴 Fadiga de Criativos**
Nenhum criativo em fadiga. Toda a conta está abaixo de 1,8. O único que merece monitoramento é Ima 04 — Cópia [Onboarding] com frequência 1,73 — dado que consome $104/semana, pode chegar à zona de atenção (≥2,5) nas próximas 2–3 semanas se o pacing continuar acelerado.

**🎨 Criativos**
- **Vencedor principal:** Ima 03 — Cópia [Onboarding] — CPL $0,47 com 10 leads (imagem) — melhor eficiência da conta, gasto ainda baixo mas já estatisticamente válido
- **Candidato a escalar:** VID 01 — Cópia [Onboarding] — CPL $0,58 com 28 leads (vídeo) — maior confiança estatística entre os eficientes
- **Volume sólido:** Ima 02 — Cópia [Onboarding] — CPL $0,75 com 100 leads — pilar de volume
- **Para pausar:** Ima 03 — Cópia [amplo] — $0,01 gasto, 0 leads, 0% CTR (possível erro de entrega)
- **Dados insuficientes (aguardar):** Ima 01 — Cópia [Onboarding], Ima 02 — Cópia [amplo]

**🎯 Ad Sets & Públicos**
"México amplo Evento Onboarding" demonstra CPM muito competitivo ($2,98) com espaço para escala — se o budget for aumentado, este é o ad set a priorizar. "México amplo" opera com CPM 3x mais caro sem vantagem clara de CPL — avaliar encerramento. Há risco de sobreposição entre os dois ad sets por ambos usarem a mesma base de público "México amplo" — verificar Audience Overlap antes de qualquer decisão de escala.

---

### 🚀 PRÓXIMOS PASSOS

- 🔴 **[HOJE] Ajustar budget diário da campanha** para ~$16/dia para não ultrapassar $500 no mês — ou alinhar com o cliente se o CAC atual justifica aumentar o budget aprovado
- 🔴 **[HOJE] Pausar Ima 03 — Cópia [amplo]** — $0,01 gasto, 0% CTR, 0 leads; verificar se está ativo por erro
- 🟡 **[24–48h] Direcionar budget incremental ao Ima 03 + VID 01 no ad set Onboarding** — CPLs de $0,47 e $0,58 merecem teste de escala gradual
- 🟡 **[24–48h] Verificar sobreposição de público** entre os dois ad sets via Audience Overlap e avaliar pausar "México amplo" se confirmada sobreposição significativa
- 🟢 **[Esta semana] Preparar criativo alternativo ao Ima 04 — Cópia** preventivamente — frequência 1,73 com $104/semana de gasto pode atingir fadiga nas próximas 2 semanas

---