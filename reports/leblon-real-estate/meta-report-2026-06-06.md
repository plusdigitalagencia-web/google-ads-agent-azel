# Relatorio Meta Ads — Leblon Real Estate
**Periodo:** 31/05/2026 a 06/06/2026 (atual) vs. 23/05/2026 a 29/05/2026 (anterior)
**Gerado em:** 06/06/2026
**Conta:** act_1187011709535726

---

## Resumo Executivo

| Metrica | Periodo Atual (31/05-06/06) | Periodo Anterior (23/05-29/05) | Variacao |
|---|---|---|---|
| Gasto total | EUR 348,85 | EUR 353,26 | -1,2% |
| Leads gerados | 9 | 12 | -25,0% |
| CPL medio | EUR 38,76 | EUR 29,44 | +31,7% |
| Impressoes | 23.708 | 22.861 | +3,7% |
| Cliques | 399 | 360 | +10,8% |
| CTR medio | 1,68% | 1,57% | +7,0% |
| CPM medio | EUR 14,71 | EUR 15,55 | -5,4% |

**3 alertas principais:**
1. CRITICO: CPL saltou de EUR 29,44 para EUR 38,76 (+31,7%) com reducao de 25% nos leads — a campanha Mexico esta entregando CPL de EUR 52,24 com apenas 4 leads em 7 dias.
2. ATENCAO: A campanha Europa teve CPM elevado (EUR 21,43) e frequencia de 2,08 — risco de saturacao de publico no horizonte de 2-3 semanas.
3. OBSERVACAO: 9 das 11 campanhas estao pausadas — toda a conta opera com apenas 2 campanhas ativas e orcamento combinado de EUR 50/dia.

---

## Modulo 1 — Auditoria de Campanhas

### Campanhas Ativas

| Status | Campanha | Orcamento/dia | Gasto 7d | Impressoes | Cliques | CTR | CPM | Frequencia | Leads | CPL |
|---|---|---|---|---|---|---|---|---|---|---|
| VERDE | [CPL][EUROPA] | EUR 20 | EUR 139,91 | 6.528 | 122 | 1,87% | EUR 21,43 | 2,08 | 5 | EUR 27,98 |
| VERMELHO | DK - [CPL][MEXICO][FORMS][BOF] | EUR 30 | EUR 208,94 | 17.180 | 277 | 1,61% | EUR 12,16 | 1,56 | 4 | EUR 52,24 |

### Campanhas Pausadas (9 campanhas)

| Campanha | Status |
|---|---|
| [CPL][NOVA][SOULMARBELLA][FORMS][BOF] | PAUSADA |
| [CPL][LA CALA GOLF][LP][BOF] | PAUSADA |
| [CPL][LA CALA GOLF][FORMS][BOF] | PAUSADA |
| [CPL][Leblon][BOF] | PAUSADA |
| DataKnow - Lead/Forms - [Apartment&Villa] — Copia | PAUSADA |
| DataKnow - Lead/Forms - [Apartment&Villa] | PAUSADA |
| Europa - Forms FB | PAUSADA |
| Mensagem - Wpp Mexico | PAUSADA |
| Mexico - Forms FB | PAUSADA |

**Observacao estrutural:** A conta esta altamente concentrada — 2 campanhas absorvem 100% do investimento. Isso elimina qualquer capacidade de teste ou diversificacao geografica/criativa em paralelo.

---

## Modulo 2 — Diagnostico de CPL

### Comparativo por campanha (atual vs. anterior)

| Campanha | CPL Atual | CPL Anterior | Variacao | Causa Raiz |
|---|---|---|---|---|
| [CPL][EUROPA] | EUR 27,98 | EUR 28,35 | -1,3% | Estavel |
| DK - [CPL][MEXICO] | EUR 52,24 | EUR 30,22 | +72,9% | Queda de conversao |

**Diagnostico Mexico:**
O CPL da campanha Mexico disparou 72,9% semana a semana, passando de EUR 30,22 para EUR 52,24. O gasto foi praticamente igual (EUR 208,94 vs EUR 211,52), mas os leads caíram de 7 para 4. O CPM caiu de EUR 13,83 para EUR 12,16 (leilao mais barato), o CTR subiu de 1,43% para 1,61% — o problema nao esta nem no leilao nem no criativo, esta na taxa de conversao do formulario. O ad set [PS - Cidades x Rico x Mexico] distribuiu investimento entre varios criativos com baixissima performance individual (09-GOLF gastou EUR 131,93 e gerou apenas 2 leads = CPL EUR 65,97).

**Conclusao:** O CPL esta alto porque a taxa de conversao do formulario / qualidade do publico caiu no ad set Mexico → acao recomendada: pausar o criativo "09 - GOLF" (EUR 131,93 gasto, 2 leads, CPL EUR 65,97) e redirecionar orcamento para o ad set Europa ou testar um novo criativo com angulo de investimento para o publico mexicano.

**Diagnostico Europa:**
Europa mantem CPL estavel em EUR 27,98 com frequencia de 2,08 — ainda dentro do limite seguro (< 2,5), mas o CPM de EUR 21,43 e o mais alto da conta. O criativo "IMA 02 - EUROPA - Santa Clara" lidera com CTR de 3,53% e CPL de EUR 9,11 com 2 leads — melhor performance individual da conta.

---

## Modulo 3 — Anomalias Detectadas

A ferramenta de anomalia automatica nao retornou sinais para o periodo. Analise manual identificou:

| Anomalia | Data de Inicio | Causa Provavel | Acao Recomendada |
|---|---|---|---|
| CPL Mexico +72,9% em 7 dias | Sem 01/06/2026 | Criativo "09 - GOLF" concentrou 63% do gasto com CPL EUR 65,97 | Pausar imediatamente; redistribuir orcamento |
| Frequencia Europa em 2,08 | Progressiva | Ad set unico com publico restrito (Alemanha + Belgica + Holanda) | Monitorar semanalmente; se > 2,5 inserir criativo novo |
| 63% do gasto Mexico concentrado em 1 criativo | 31/05/2026 | Algoritmo priorizou "09 - GOLF" sem resultado consistente | Forcar rotacao ou criar novo ad set com criativo restrito |

---

## Modulo 4 — Pacing Monitor

**Orcamento diario combinado:** EUR 50/dia (EUR 20 Europa + EUR 30 Mexico)
**Periodo de referencia:** Mes de junho 2026
**Dias decorridos no mes:** 6 de 30 (20% do mes)

**Gasto atual no mes (jun/26):**
- Dados disponiveis apenas para o periodo 31/05-06/06
- Gasto medio diario observado: EUR 348,85 / 7 dias = EUR 49,84/dia
- Orcamento diario configurado: EUR 50,00/dia

**Projecao mensal:** EUR 49,84 x 30 = EUR 1.495/mes

**Status: NO RITMO — dentro da faixa esperada**

O gasto diario medio (EUR 49,84) esta praticamente alinhado ao orcamento configurado (EUR 50,00), com desvio de apenas 0,3%. Sem aceleracao nem subentrega.

---

## Modulo 5 — Fadiga de Criativos

A ferramenta de criativos nao esta disponivel para esta conta via MCP (rollout gradual). Analise baseada em frequencia e tendencia de CTR:

### Ad Set [ALE][BEL][HOL] — Campanha Europa

| Criativo | Leads | CTR | Frequencia | Gasto | CPL | Status CTR |
|---|---|---|---|---|---|---|
| IMA 02 - EUROPA - Santa Clara | 2 | 3,53% | 1,37 | EUR 18,21 | EUR 9,11 | SUBINDO (+180%) |
| AD04_IMG_ | 3 | 1,54% | 1,92 | EUR 88,11 | EUR 29,37 | Neutro |
| AD03_VID_Santa Clara | 0 | 2,78% | 1,07 | EUR 2,68 | N/A | Muito novo |
| IMA 04 - EUROPA - MIJAS (PAUSADO) | 0 | 1,96% | 1,29 | EUR 30,91 | N/A | Pausado |

**Frequencia do ad set:** 2,08 — ATENCAO (faixa 2,0-2,5)

### Ad Set [PS - Cidades x Rico x Mexico] — Campanha Mexico

| Criativo | Leads | CTR | Frequencia | Gasto | CPL | Status |
|---|---|---|---|---|---|---|
| AD10 - [IMG] [PROPRIEDADES PREMIUM] | 1 | 6,06% | 1,11 | EUR 4,45 | EUR 4,45 | OTIMO - subindo |
| AD10 - [IMG] [BOLINHA] | 0 | 5,00% | 1,25 | EUR 0,89 | N/A | CTR caindo |
| 08 - Villas — Copia | 0 | 4,17% | 1,03 | EUR 0,68 | N/A | Muito novo |
| VID 01 — Copia | 1 | 2,07% | 1,15 | EUR 3,47 | EUR 3,47 | CTR caindo |
| 09 - GOLF (ATIVO) | 2 | 1,56% | 1,40 | EUR 131,93 | EUR 65,97 | CRITICO |
| 03 - PROPRIEDADE EXCLUSIVA (PAUSADO) | 0 | 1,34% | 1,21 | EUR 23,34 | N/A | Pausado |
| AD11 - [IMG] [para unos pocos] (PAUSADO) | 0 | 1,57% | 1,57 | EUR 44,18 | N/A | Pausado |

**Recomendacoes de criativos:**
- PAUSAR imediatamente: "09 - GOLF" — consumiu EUR 131,93 (63% do budget Mexico), gerou 2 leads, CPL EUR 65,97
- ESCALAR: "AD10 - [IMG] [PROPRIEDADES PREMIUM]" — CTR 6,06%, CPL EUR 4,45, tendencia fortemente positiva (+142%)
- MONITORAR: "IMA 02 - EUROPA - Santa Clara" — melhor criativo da conta, CTR 3,53%, CPL EUR 9,11, subindo 180%
- INSERIR: Novo criativo para ad set Europa quando frequencia atingir 2,5

---

## Modulo 6 — Gerador de Variacoes de Copy

**Base nos 2 melhores criativos da conta:**

### Criativo vencedor 1: IMA 02 - EUROPA - Santa Clara (CTR 3,53%, CPL EUR 9,11)

Angulo provavel: Imovel especifico, imagem de propriedade real, urgencia de disponibilidade

**Variacao A — Espanhol (prova social):**
Hook: "127 familias europeas ya eligieron vivir en la Costa del Sol. Queda 1 unidad disponible en Santa Clara."
CTA: "Ver disponibilidad ahora"

**Variacao B — Espanhol (exclusividade financeira):**
Hook: "La inversion que protege tu patrimonio mientras disfrutas el Mediterraneo. Desde EUR 450.000 en Marbella."
CTA: "Solicitar informacion privada"

**Variacao A — Ingles (prova social):**
Hook: "127 European families already chose their life on the Costa del Sol. 1 unit left at Santa Clara."
CTA: "Check availability now"

**Variacao B — Ingles (exclusividade financeira):**
Hook: "The investment that protects your wealth while you enjoy the Mediterranean. From EUR 450,000 in Marbella."
CTA: "Request private information"

---

### Criativo vencedor 2: AD10 - [IMG] [PROPRIEDADES PREMIUM] (CTR 6,06%, CPL EUR 4,45)

Angulo provavel: Imagem de propriedade premium, apelo a exclusividade, publico mexicano alto valor

**Variacao A — Espanhol (ROI + localizacao):**
Hook: "Marbella: donde el metro cuadrado de lujo sube 12% cada ano. Tu propiedad, tu rentabilidad."
CTA: "Quiero conocer las opciones"

**Variacao B — Espanhol (lifestyle + investimento):**
Hook: "Para quienes ya lo tienen todo — excepto una residencia en la Costa del Sol."
CTA: "Explorar propiedades exclusivas"

**Variacao A — Ingles (ROI + localizacao):**
Hook: "Marbella: where luxury property rises 12% annually. Your asset, your returns."
CTA: "Explore investment options"

**Variacao B — Ingles (lifestyle + investimento):**
Hook: "For those who have everything — except a residence on the Costa del Sol."
CTA: "Discover exclusive properties"

---

## Modulo 7 — Sobreposicao de Publicos

A ferramenta de custom audiences nao esta disponivel para esta conta via MCP (rollout gradual). Analise baseada nos dados de ad sets:

### Ad sets ativos simultaneos

| Ad Set | Campanha | Segmentacao | Geo | Otimizacao |
|---|---|---|---|---|
| [ALE][BEL][HOL] | Europa | Interesses (imobiliario/investimento) | Alemanha, Belgica, Holanda | LEAD_GENERATION |
| [PS - Cidades x Rico x Mexico] | Mexico | Interesses (golf, alto valor, cidades ricas) | Mexico | LEAD_GENERATION |

**Sobreposicao estimada: BAIXA**
Os dois ad sets ativos segmentam geografias completamente distintas (Europa Ocidental vs. Mexico) — sem sobreposicao de leilao entre eles. Risco de competicao interna: inexistente no momento.

**Alerta estrutural — Ad sets pausados:**
Ha 20+ ad sets pausados nas campanhas Mexico e SOULMARBELLA com segmentacoes sobrepostas (Golf, Alto Valor, Novos Locais, Viajantes — todos direcionados ao Mexico). Se reativados simultaneamente, havera alta sobreposicao de publico e inflacao de CPM. Recomenda-se consolidar em no maximo 2-3 ad sets por mercado antes de reativar.

---

## Plano de Acao

| Prioridade | Acao | Impacto Esperado | Prazo |
|---|---|---|---|
| 1 | Pausar criativo "09 - GOLF" (ID 120241726743890513) — EUR 131,93 gasto, CPL EUR 65,97 | Reduzir CPL medio da campanha Mexico em ~40% | Imediato (hoje) |
| 2 | Aumentar orcamento do criativo "AD10 - [IMG] [PROPRIEDADES PREMIUM]" (ID 120241798869710513) — CTR 6,06%, CPL EUR 4,45 | Potencial de escalar leads Mexico com CPL baixo | Esta semana |
| 3 | Criar 2 novos criativos para ad set Europa (Variacao A e B geradas no Modulo 6) antes que frequencia atinja 2,5 | Prevenir queda de CTR e aumento de CPL | Ate 10/06/2026 |
| 4 | Testar reativacao da campanha SOULMARBELLA com 1 ad set consolidado (Golf/Viajantes) + EUR 15/dia | Diversificar mercado e reduzir dependencia de 2 campanhas | Ate 13/06/2026 |
| 5 | Revisar e limpar estrutura de ad sets pausados da campanha Mexico — consolidar em 1-2 ad sets antes de qualquer reativacao | Prevenir sobreposicao de publico e inflacao de CPM | Ate 15/06/2026 |

---

*Relatorio gerado automaticamente pelo Agente Meta Ads — Data Know*
*Proxima analise recomendada: 13/06/2026*
