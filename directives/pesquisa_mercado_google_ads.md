# Directive: Pesquisa de Mercado + Estratégia Search Google Ads

## Objetivo
Realizar uma inteligência de mercado completa para um cliente novo ou existente, combinando análise do site, pesquisa de concorrentes, Keyword Planner, auditoria da conta ativa e entrega de uma estratégia de Search pronta para implementar — em 20 minutos o que levaria 4 horas manualmente.

## Inputs necessários
- `url_cliente`: URL do site do cliente
- `conta_google_ads`: ID da conta Google Ads (opcional — se tiver campanha ativa)
- `tipo_publico`: B2B, B2C ou ambos (se não informado, detectar automaticamente pelo site)
- `contexto_extra`: Qualquer informação adicional que o usuário fornecer (ex: "quer apenas empresas com +50 funcionários")

## Etapas de execução

### Etapa 1 — Leitura e análise do site do cliente
Use a ferramenta WebFetch para ler o site do cliente.

Extraia:
- Qual é o serviço/produto principal
- Quem é o público-alvo explícito (o que o site diz)
- Qual é o diferencial declarado
- Tom de voz (formal, técnico, popular)
- Palavras e termos que o próprio cliente usa para descrever o negócio
- O que está faltando ou mal comunicado no site

### Etapa 2 — Classificação do mercado
Com base no site e no contexto fornecido, classifique:

**Se B2B:**
- Como o comprador empresarial pensa? (gestor, facilities, compras, CEO)
- Qual é a dor do comprador empresarial? (custo, risco, conformidade, produtividade)
- Em que momento ele pesquisa? (urgência vs. planejamento)
- Que termos técnicos ele usaria?

**Se B2C:**
- Como o consumidor final pensa?
- Qual é a dor imediata? (preço, urgência, praticidade, qualidade)
- Que termos emocionais/práticos ele usaria?

**Se ambos:**
- Separe completamente as duas personas
- Defina keywords, ângulos e negativas distintos para cada uma
- Identifique como evitar que o B2C contamine as campanhas B2B e vice-versa

### Etapa 3 — Pesquisa de concorrentes no Google
Use WebFetch e WebSearch para:

1. Buscar no Google os principais termos do nicho (ex: "empresa de ar condicionado São Paulo", "manutenção HVAC industrial")
2. Identificar quem está anunciando (resultados patrocinados)
3. Para cada concorrente encontrado:
   - Capturar headline e descrição do anúncio
   - Identificar a oferta principal (preço, garantia, prazo, diferencial)
   - Identificar o ângulo (urgência, autoridade, preço, resultado)
   - Ver a landing page de destino se possível
4. Montar uma tabela comparativa: Concorrente | Anúncio | Oferta | Ângulo | Ponto fraco

### Etapa 3.5 — Auditoria da conta ativa (se fornecida)
Se o usuário informou um ID de conta Google Ads, execute:

```bash
python3 execution/google_ads_search_terms.py --customer-id CUSTOMER_ID --days 60 --min-cost 5
python3 execution/google_ads_keyword_analyzer.py --customer-id CUSTOMER_ID --days 60
```

Analise os resultados e identifique:
- **Termos que convertem** → candidatos a virar keywords de exata match
- **Termos com gasto e zero conversão** → lista de negativas imediatas
- **Termos B2C infiltrados em campanha B2B** (ou vice-versa) → negativas estratégicas
- **Alinhamento**: os termos reais que aparecem condizem com as keywords ativas?
- **Gaps**: o que o público está buscando que não está sendo capturado?

### Etapa 4 — Keyword Planner
Use a ferramenta `get_keyword_ideas` do MCP Google Ads com as seeds identificadas.

Para cada keyword retornada, avalie:
- Volume mensal
- CPC estimado
- Competição (baixa/média/alta)
- Intenção (topo = informacional, meio = comparação, fundo = compra)
- Público (B2B ou B2C)

Organize em grupos:
- **Grupo A — Fundo de funil B2B**: alta intenção de compra empresarial
- **Grupo B — Fundo de funil B2C**: alta intenção de compra residencial/pessoal
- **Grupo C — Meio de funil**: comparação e pesquisa
- **Grupo D — Branded/Concorrentes**: termos de marca própria e concorrentes

### Etapa 5 — Biblioteca de anúncios Meta
Use WebFetch para pesquisar na Meta Ads Library os concorrentes identificados.

URL padrão: `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=BR&q=TERMO`

Identifique:
- Que ângulos criativos estão sendo testados
- Que formatos (vídeo, carrossel, estático)
- Que ofertas estão sendo feitas
- Oportunidades não exploradas pelos concorrentes

### Etapa 6 — Entrega da estratégia

#### 6.1 Estrutura de campanha recomendada
```
Campanha 1: [B2B] Nome do cliente — Fundo de funil
  Ad Group 1: [Serviço principal] — Exact match
  Ad Group 2: [Termos técnicos] — Phrase match
  Ad Group 3: [Concorrentes] — Exact match

Campanha 2: [B2C] Nome do cliente — Fundo de funil (se aplicável)
  Ad Group 1: [Termos de urgência] — Exact match
  Ad Group 2: [Termos de preço] — Phrase match
```

#### 6.2 Keywords por grupo (com volume e CPC)
Liste as keywords recomendadas organizadas por ad group, com tipo de correspondência sugerido.

#### 6.3 Lista de negativas sugeridas
Separe em:
- **Negativas de campanha**: excluem públicos completamente errados
- **Negativas de ad group**: refinam a segmentação entre grupos

#### 6.4 Ângulos de copy recomendados
Para cada público (B2B e B2C), sugira 3 ângulos de headline diferentes com base no que os concorrentes NÃO estão fazendo.

#### 6.5 Oportunidades identificadas
O que está sendo ignorado pelos concorrentes que o cliente pode explorar.

#### 6.6 Alertas e riscos
O que pode dar errado se não for tratado (ex: broad match sem negativas vai misturar B2B e B2C).

## Output
1. **Análise completa no chat** — formatada em seções claras
2. **Google Docs** — versão limpa e profissional para apresentar ao cliente, criado na pasta padrão do Google Drive (`GOOGLE_DRIVE_FOLDER_ID`)

## Edge Cases
- Se o site do cliente estiver fora do ar: pedir URL alternativa ou LinkedIn da empresa
- Se não houver conta ativa: pular Etapa 3.5 e indicar isso no output
- Se o nicho for muito específico (ex: B2B industrial): focar em termos técnicos e CNAE, não em termos populares
- Se o Keyword Planner retornar volume baixo para termos B2B: isso é normal — volume baixo + alta intenção = oportunidade boa
- Se encontrar menos de 3 concorrentes anunciando: ampliar busca para cidades vizinhas ou termos relacionados

## Notas estratégicas
- Volume baixo não significa oportunidade ruim — em B2B, 50 pesquisas/mês com alta intenção valem mais que 5.000 de B2C
- Sempre que o cliente quiser B2B puro: a lista de negativas é tão importante quanto as keywords ativas
- Termos como "residencial", "pequeno", "apartamento", "casa" são negativas automáticas para B2B industrial
- O comprador empresarial pesquisa diferente: ele usa termos como "fornecedor", "contrato", "manutenção preventiva", "laudo técnico", "empresa especializada"
