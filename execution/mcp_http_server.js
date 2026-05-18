#!/usr/bin/env node
/**
 * MCP HTTP Server para Google Ads — versão para deploy na nuvem (Render).
 * Usa StreamableHTTP transport (protocolo atual do claude.ai).
 */
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { CallToolRequestSchema, ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";
import { execFileSync } from "child_process";
import express from "express";
import path from "path";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const PROJECT_ROOT = path.dirname(__dirname);
const PYTHON = process.env.PYTHON_PATH || "python3";
const EXEC_DIR = path.join(PROJECT_ROOT, "execution");

const ACCOUNTS = {
  "dra cejana":      { id: "2470198472", mcc: "2694906582" },
  "costa e rassi":   { id: "2080767729", mcc: "2694906582" },
  "cursos makeup":   { id: "4571513045", mcc: "2694906582" },
  "dr bruno":        { id: "8521374023", mcc: "2694906582" },
  "ferravima":       { id: "1629787957", mcc: "2694906582" },
  "grupo ferravima": { id: "1537394693", mcc: "2694906582" },
  "hi nutrition":    { id: "4174012683", mcc: "2694906582" },
  "inades":          { id: "2914601254", mcc: "2694906582" },
  "levant digital":  { id: "7287032519", mcc: "2694906582" },
  "plus afiliado":   { id: "4950512913", mcc: "2694906582" },
  "quick power":     { id: "4520811474", mcc: "2694906582" },
  "shineray":        { id: "3604927656", mcc: "2694906582" },
  "chez france":     { id: "8882189559", mcc: "2564865113" },
  "speedmais":       { id: "6081418993", mcc: "2564865113" },
  "aquino lopes":    { id: "9480555388", mcc: "7118682168" },
  "dna renata":      { id: "3511852091", mcc: "7118682168" },
  "dr lincoln":      { id: "5490318966", mcc: "7118682168" },
  "dra isabela":     { id: "5234591068", mcc: "7118682168" },
  "duosfera":        { id: "4938246000", mcc: "7118682168" },
  "laboratorio genesi": { id: "2851947028", mcc: "7118682168" },
  "pro vida":        { id: "5981473421", mcc: "7118682168" },
  "wm maquinas":     { id: "7447095468", mcc: "7118682168" },
  "fr arquitectura": { id: "7481567331", mcc: "2319759276" },
  "allmark":         { id: "7403302344", mcc: "2319759276" },
  "cs assistencia":  { id: "4705719784", mcc: "2319759276" },
  "enova":           { id: "7551003277", mcc: "2319759276" },
  "harium":          { id: "6733003839", mcc: "2319759276" },
  "parma":           { id: "3355440327", mcc: "2319759276" },
  "sciente":         { id: "3679830725", mcc: "2319759276" },
  "spartan":         { id: "9559342501", mcc: "2319759276" },
  "nordika":         { id: "6182489345", mcc: "2319759276" },
};

function resolveAccount(name) {
  const lower = name.toLowerCase().trim();
  for (const [key, val] of Object.entries(ACCOUNTS)) {
    if (key.includes(lower) || lower.includes(key)) return val;
  }
  return null;
}

function runScript(script, args, mccOverride = null) {
  const env = { ...process.env, PYTHONWARNINGS: "ignore" };
  if (mccOverride) env.GOOGLE_ADS_LOGIN_CUSTOMER_ID = mccOverride;

  try {
    const output = execFileSync(PYTHON, [path.join(EXEC_DIR, script), ...args], {
      env,
      cwd: PROJECT_ROOT,
      timeout: 90000,
      encoding: "utf8",
    });
    return cleanOutput(output);
  } catch (err) {
    return cleanOutput(err.stdout || err.message || "Erro ao executar script.");
  }
}

function cleanOutput(text) {
  return (text || "")
    .split("\n")
    .filter(l => !["FutureWarning","warnings.warn","NotOpenSSLWarning","end of life",
                    "python3 -m pip","upgrade","LibreSSL","Request made:"].some(w => l.includes(w)))
    .join("\n")
    .trim();
}

function createServer() {
  const server = new Server(
    { name: "google-ads", version: "1.0.0" },
    { capabilities: { tools: {} } }
  );

  server.setRequestHandler(ListToolsRequestSchema, async () => ({
    tools: [
      {
        name: "list_accounts",
        description: "Lista todas as contas Google Ads disponíveis.",
        inputSchema: { type: "object", properties: {} },
      },
      {
        name: "get_campaign_metrics",
        description: "Puxa métricas de campanhas: gasto, cliques, CTR, CPA, ROAS, conversões.",
        inputSchema: {
          type: "object",
          properties: {
            account_name: { type: "string", description: "Nome da conta (ex: 'Chez France')" },
            days: { type: "number", description: "Período em dias (padrão: 30)" },
          },
          required: ["account_name"],
        },
      },
      {
        name: "analyze_keywords",
        description: "Analisa keywords ativas: Quality Score, gasto, conversões, keywords problemáticas.",
        inputSchema: {
          type: "object",
          properties: {
            account_name: { type: "string" },
            days: { type: "number" },
          },
          required: ["account_name"],
        },
      },
      {
        name: "analyze_search_terms",
        description: "Analisa termos de busca e identifica negativas que estão desperdiçando dinheiro.",
        inputSchema: {
          type: "object",
          properties: {
            account_name: { type: "string" },
            days: { type: "number" },
            min_cost: { type: "number" },
          },
          required: ["account_name"],
        },
      },
      {
        name: "audit_ads",
        description: "Audita anúncios, títulos, descrições e extensões de campanhas Search e PMax.",
        inputSchema: {
          type: "object",
          properties: {
            account_name: { type: "string" },
            type: { type: "string", enum: ["search", "pmax", "extensions", "all"] },
          },
          required: ["account_name"],
        },
      },
      {
        name: "get_keyword_ideas",
        description: "Usa o Keyword Planner do Google para encontrar novas oportunidades de keywords.",
        inputSchema: {
          type: "object",
          properties: {
            account_name: { type: "string" },
            keywords: { type: "array", items: { type: "string" } },
          },
          required: ["account_name", "keywords"],
        },
      },
    ],
  }));

  server.setRequestHandler(CallToolRequestSchema, async (request) => {
    const { name, arguments: args } = request.params;

    if (name === "list_accounts") {
      return { content: [{ type: "text", text: runScript("test_connection.py", []) }] };
    }

    const account = resolveAccount(args.account_name || "");
    if (!account) {
      const names = Object.keys(ACCOUNTS).join(", ");
      return { content: [{ type: "text", text: `Conta '${args.account_name}' não encontrada. Disponíveis: ${names}` }] };
    }

    const { id: customerId, mcc } = account;
    let output = "";

    if (name === "get_campaign_metrics") {
      output = runScript("google_ads_metrics_reader.py",
        ["--customer-id", customerId, "--days", String(args.days ?? 30)], mcc);
    } else if (name === "analyze_keywords") {
      output = runScript("google_ads_keyword_analyzer.py",
        ["--customer-id", customerId, "--days", String(args.days || 30)], mcc);
    } else if (name === "analyze_search_terms") {
      output = runScript("google_ads_search_terms.py",
        ["--customer-id", customerId, "--days", String(args.days || 30),
         "--min-cost", String(args.min_cost || 10)], mcc);
    } else if (name === "audit_ads") {
      output = runScript("google_ads_ad_auditor.py",
        ["--customer-id", customerId, "--type", args.type || "all"], mcc);
    } else if (name === "get_keyword_ideas") {
      output = runScript("google_ads_keyword_analyzer.py",
        ["--customer-id", customerId, "--new-ideas", ...(args.keywords || [])], mcc);
    }

    return { content: [{ type: "text", text: output || "Sem dados retornados." }] };
  });

  return server;
}

const app = express();
app.use(express.json());

// StreamableHTTP — protocolo atual do claude.ai
app.all("/mcp", async (req, res) => {
  const transport = new StreamableHTTPServerTransport({
    sessionIdGenerator: undefined, // stateless — mais simples e compatível
  });

  const server = createServer();
  await server.connect(transport);
  await transport.handleRequest(req, res, req.body);
  await server.close();
});

app.get("/health", (_, res) => res.json({ status: "ok", service: "google-ads-mcp" }));

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Google Ads MCP Server rodando na porta ${PORT}`);
  console.log(`MCP endpoint: https://google-ads-mcp-i085.onrender.com/mcp`);
});
