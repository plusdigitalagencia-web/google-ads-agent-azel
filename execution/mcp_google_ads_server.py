"""
MCP Server for Google Ads — exposes Google Ads scripts as tools for Claude.
Runs locally via stdio. Configure in .claude/settings.json.
"""
import asyncio
import subprocess
import sys
import os
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

PROJECT_ROOT = str(Path(__file__).parent.parent)
PYTHON = sys.executable

ACCOUNTS = {
    "dra cejana": ("2470198472", "2694906582"),
    "costa e rassi": ("2080767729", "2694906582"),
    "cursos makeup": ("4571513045", "2694906582"),
    "dr bruno": ("8521374023", "2694906582"),
    "ferravima": ("1629787957", "2694906582"),
    "grupo ferravima": ("1537394693", "2694906582"),
    "hi nutrition": ("4174012683", "2694906582"),
    "inades": ("2914601254", "2694906582"),
    "levant digital": ("7287032519", "2694906582"),
    "plus afiliado": ("4950512913", "2694906582"),
    "quick power": ("4520811474", "2694906582"),
    "shineray": ("3604927656", "2694906582"),
    "chez france": ("8882189559", "2564865113"),
    "speedmais": ("6081418993", "2564865113"),
    "speed": ("6081418993", "2564865113"),
    # Duosfera MCC (7118682168) — adicionar contas aqui quando necessário
    # DataKnow MCC (2319759276)
    "nordika": ("6182489345", "2319759276"),
}

# MCC IDs disponíveis:
# Plus Digital Agência: 2694906582
# ASSUCAR MCC:          2564865113
# Agência Duosfera MCC: 7118682168
# DataKnow:             2319759276

def run_script(script: str, args: list[str]) -> str:
    result = subprocess.run(
        [PYTHON, os.path.join(PROJECT_ROOT, "execution", script)] + args,
        capture_output=True,
        text=True,
        cwd=PROJECT_ROOT,
        env={**os.environ, "PYTHONWARNINGS": "ignore"},
    )
    output = result.stdout
    if result.returncode != 0 and not output:
        output = result.stderr
    lines = [l for l in output.splitlines() if not any(w in l for w in [
        "FutureWarning", "warnings.warn", "NotOpenSSLWarning",
        "end of life", "python3 -m pip", "upgrade", "LibreSSL"
    ])]
    return "\n".join(lines).strip()

def resolve_account(account_name: str) -> tuple[str, str] | None:
    name = account_name.lower().strip()
    for key, ids in ACCOUNTS.items():
        if key in name or name in key:
            return ids
    return None

app = Server("google-ads")

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="list_accounts",
            description="Lista todas as contas Google Ads no MCC. Use para descobrir quais contas estão disponíveis.",
            inputSchema={"type": "object", "properties": {}, "required": []},
        ),
        Tool(
            name="get_campaign_metrics",
            description="Puxa métricas de campanhas de uma conta: gasto, cliques, impressões, CTR, CPA, ROAS, conversões.",
            inputSchema={
                "type": "object",
                "properties": {
                    "account_name": {"type": "string", "description": "Nome da conta (ex: 'Hi Nutrition', 'Chez France')"},
                    "days": {"type": "integer", "description": "Período em dias (padrão: 30)", "default": 30},
                },
                "required": ["account_name"],
            },
        ),
        Tool(
            name="analyze_keywords",
            description="Analisa keywords ativas de uma conta: Quality Score, gasto, conversões, keywords desperdiçando dinheiro.",
            inputSchema={
                "type": "object",
                "properties": {
                    "account_name": {"type": "string", "description": "Nome da conta"},
                    "days": {"type": "integer", "description": "Período em dias (padrão: 30)", "default": 30},
                },
                "required": ["account_name"],
            },
        ),
        Tool(
            name="analyze_search_terms",
            description="Analisa termos de busca e identifica keywords negativas que estão desperdiçando dinheiro.",
            inputSchema={
                "type": "object",
                "properties": {
                    "account_name": {"type": "string", "description": "Nome da conta"},
                    "days": {"type": "integer", "description": "Período em dias (padrão: 30)", "default": 30},
                    "min_cost": {"type": "number", "description": "Custo mínimo para candidato a negativa em R$ (padrão: 10)", "default": 10},
                },
                "required": ["account_name"],
            },
        ),
        Tool(
            name="audit_ads",
            description="Audita anúncios, títulos, descrições e extensões de campanhas Search e PMax.",
            inputSchema={
                "type": "object",
                "properties": {
                    "account_name": {"type": "string", "description": "Nome da conta"},
                    "type": {"type": "string", "enum": ["search", "pmax", "extensions", "all"], "default": "all"},
                },
                "required": ["account_name"],
            },
        ),
        Tool(
            name="get_keyword_ideas",
            description="Usa o Keyword Planner do Google para encontrar novas oportunidades de keywords com volume e CPC estimado.",
            inputSchema={
                "type": "object",
                "properties": {
                    "account_name": {"type": "string", "description": "Nome da conta"},
                    "keywords": {"type": "array", "items": {"type": "string"}, "description": "Lista de keywords semente para buscar ideias"},
                },
                "required": ["account_name", "keywords"],
            },
        ),
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    if name == "list_accounts":
        output = run_script("test_connection.py", [])
        return [TextContent(type="text", text=output)]

    account_name = arguments.get("account_name", "")
    ids = resolve_account(account_name)

    if not ids:
        return [TextContent(type="text", text=f"Conta '{account_name}' não encontrada. Contas disponíveis: {', '.join(ACCOUNTS.keys())}")]

    customer_id, mcc_id = ids

    env_patch = os.environ.copy()
    env_patch["GOOGLE_ADS_LOGIN_CUSTOMER_ID"] = mcc_id
    env_patch["PYTHONWARNINGS"] = "ignore"

    if name == "get_campaign_metrics":
        days = arguments.get("days", 30)
        result = subprocess.run(
            [PYTHON, os.path.join(PROJECT_ROOT, "execution", "google_ads_metrics_reader.py"),
             "--customer-id", customer_id, "--days", str(days)],
            capture_output=True, text=True, cwd=PROJECT_ROOT, env=env_patch,
        )
        output = result.stdout or result.stderr

    elif name == "analyze_keywords":
        days = arguments.get("days", 30)
        result = subprocess.run(
            [PYTHON, os.path.join(PROJECT_ROOT, "execution", "google_ads_keyword_analyzer.py"),
             "--customer-id", customer_id, "--days", str(days)],
            capture_output=True, text=True, cwd=PROJECT_ROOT, env=env_patch,
        )
        output = result.stdout or result.stderr

    elif name == "analyze_search_terms":
        days = arguments.get("days", 30)
        min_cost = arguments.get("min_cost", 10)
        result = subprocess.run(
            [PYTHON, os.path.join(PROJECT_ROOT, "execution", "google_ads_search_terms.py"),
             "--customer-id", customer_id, "--days", str(days), "--min-cost", str(min_cost)],
            capture_output=True, text=True, cwd=PROJECT_ROOT, env=env_patch,
        )
        output = result.stdout or result.stderr

    elif name == "audit_ads":
        audit_type = arguments.get("type", "all")
        result = subprocess.run(
            [PYTHON, os.path.join(PROJECT_ROOT, "execution", "google_ads_ad_auditor.py"),
             "--customer-id", customer_id, "--type", audit_type],
            capture_output=True, text=True, cwd=PROJECT_ROOT, env=env_patch,
        )
        output = result.stdout or result.stderr

    elif name == "get_keyword_ideas":
        keywords = arguments.get("keywords", [])
        result = subprocess.run(
            [PYTHON, os.path.join(PROJECT_ROOT, "execution", "google_ads_keyword_analyzer.py"),
             "--customer-id", customer_id, "--new-ideas"] + keywords,
            capture_output=True, text=True, cwd=PROJECT_ROOT, env=env_patch,
        )
        output = result.stdout or result.stderr

    else:
        output = f"Ferramenta '{name}' não reconhecida."

    lines = [l for l in output.splitlines() if not any(w in l for w in [
        "FutureWarning", "warnings.warn", "NotOpenSSLWarning",
        "end of life", "python3 -m pip", "upgrade", "LibreSSL", "Request made:"
    ])]
    return [TextContent(type="text", text="\n".join(lines).strip())]

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await app.run(read_stream, write_stream, app.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
