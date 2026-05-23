import os, json, urllib.request, base64, re
from datetime import datetime

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
NOTION_HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}
GH_TOKEN = os.environ.get("GH_TOKEN", "")
GH_HEADERS = {"Authorization": f"token {GH_TOKEN}", "Accept": "application/vnd.github+json"}

REPO_URL = "https://github.com/plusdigitalagencia-web/google-ads-agent-azel"
REPO     = "plusdigitalagencia-web/google-ads-agent-azel"

# link_clients  → recebem link do relatório
# camp_routing  → dicionário {keyword_no_nome: [page_ids]} para campanhas
#                 se vazio, usa link_clients para campanhas também
CLIENT_MAP = {
    "shineray": {
        "link_clients": [{"notion_id": "3690e07d-daa5-819a-9c43-d4f8542270f7", "nome": "Shineray Maranhão"}],
        "camp_routing": {},
    },
    "dra-cejana-dr-bruno": {
        "link_clients": [
            {"notion_id": "3690e07d-daa5-81a1-a2bf-e6257bc4847d", "nome": "Dra. Cejana"},
            {"notion_id": "3690e07d-daa5-8156-8ced-d09c352160b2", "nome": "Dr. Bruno"},
        ],
        "camp_routing": {
            "cejana": [{"notion_id": "3690e07d-daa5-81a1-a2bf-e6257bc4847d", "nome": "Dra. Cejana"}],
            "bruno":  [{"notion_id": "3690e07d-daa5-8156-8ced-d09c352160b2", "nome": "Dr. Bruno"}],
        },
    },
    "chez-france": {
        "link_clients": [{"notion_id": "3690e07d-daa5-81d1-afeb-eef8b4193324", "nome": "Chez France"}],
        "camp_routing": {},
    },
    "speed": {
        "link_clients": [{"notion_id": "3690e07d-daa5-81de-8601-dbb6a9457d69", "nome": "SpeedMais Gráfica"}],
        "camp_routing": {},
    },
    "hoteligy": {"link_clients": [], "camp_routing": {}},
    "nordika":  {"link_clients": [], "camp_routing": {}},
}

# ── Notion helpers ─────────────────────────────────────────────────────────────

def notion_get(url):
    req = urllib.request.Request(url, headers=NOTION_HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def notion_patch(url, body):
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, headers=NOTION_HEADERS, method="PATCH")
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def notion_delete(block_id):
    req = urllib.request.Request(
        f"https://api.notion.com/v1/blocks/{block_id}",
        headers=NOTION_HEADERS, method="DELETE")
    try:
        with urllib.request.urlopen(req): pass
    except: pass

def get_page_blocks(page_id):
    return notion_get(
        f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100"
    ).get("results", [])

def find_section(blocks, keyword):
    in_section = False
    inner_ids, last_id, heading_id = [], None, None
    for b in blocks:
        btype = b["type"]
        if btype == "heading_2":
            text = b.get("heading_2", {}).get("rich_text", [])
            title = text[0].get("plain_text", "") if text else ""
            if keyword in title:
                in_section, heading_id = True, b["id"]
                continue
            elif in_section:
                break
        if btype == "divider" and in_section:
            break
        if in_section:
            inner_ids.append(b["id"])
            last_id = b["id"]
    return heading_id, last_id, inner_ids

# ── Report link ────────────────────────────────────────────────────────────────

def add_report_link(page_id, file_name, file_path):
    blocks = get_page_blocks(page_id)
    _, last_id, _ = find_section(blocks, "Relat")
    if not last_id:
        print(f"    Seção Relatórios não encontrada"); return False
    today = datetime.now().strftime("%d/%m/%Y")
    github_url = f"{REPO_URL}/blob/main/{file_path}"
    body = {
        "after": last_id,
        "children": [{"object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {"rich_text": [
                {"type": "text", "text": {"content": f"📄 {file_name}  —  {today}  → "}},
                {"type": "text", "text": {"content": "Ver no GitHub", "link": {"url": github_url}},
                 "annotations": {"bold": True, "color": "blue"}},
            ]}}]
    }
    result = notion_patch(f"https://api.notion.com/v1/blocks/{page_id}/children", body)
    return bool(result.get("results"))

# ── Campaign extraction ────────────────────────────────────────────────────────

def detect_platform(filename):
    fn = filename.lower()
    if "meta" in fn or "whatsapp" in fn: return "Meta Ads"
    if "google" in fn:                   return "Google Ads"
    return "Google Ads + Meta Ads"

def extract_campaigns(content, platform):
    campaigns, seen = [], set()
    for line in content.split("\n"):
        if "|" not in line: continue
        if re.search(r"-{3,}", line): continue
        cells = [c.strip() for c in line.split("|") if c.strip()]
        if not cells: continue
        row = " ".join(cells)
        if not ("🟢" in row or "ATIVA" in row.upper() or "ACTIVE" in row.upper()):
            continue
        name = re.sub(r"\(\d{10,}\)", "", cells[0]).strip()
        if any(kw in name.lower() for kw in ["campanha", "camp.", "nome", "status"]): continue
        if name in seen or len(name) < 3: continue
        seen.add(name)
        campaigns.append({"nome": name[:70], "plataforma": platform})
    return campaigns

def fetch_file_content(file_path):
    url = f"https://api.github.com/repos/{REPO}/contents/{file_path}"
    req = urllib.request.Request(url, headers=GH_HEADERS)
    try:
        with urllib.request.urlopen(req) as r:
            return base64.b64decode(json.loads(r.read())["content"]).decode("utf-8")
    except Exception as e:
        print(f"    Erro ao ler arquivo: {e}"); return ""

# ── Update Campanhas section ───────────────────────────────────────────────────

def update_campaigns(page_id, campaigns):
    blocks = get_page_blocks(page_id)
    _, last_id, inner_ids = find_section(blocks, "Campanhas")
    if not last_id:
        print(f"    Seção Campanhas não encontrada"); return False

    for bid in inner_ids:
        block = next((b for b in blocks if b["id"] == bid), None)
        if block and block["type"] == "bulleted_list_item":
            notion_delete(bid)

    blocks = get_page_blocks(page_id)
    _, last_id, _ = find_section(blocks, "Campanhas")
    if not last_id: return False

    today = datetime.now().strftime("%d/%m/%Y")
    month = datetime.now().strftime("%m/%Y")
    new_blocks = [
        {"object": "block", "type": "bulleted_list_item",
         "bulleted_list_item": {"rich_text": [
             {"type": "text", "text": {"content": f"🔄 Atualizado em {today} — campanhas ativas em {month}"},
              "annotations": {"italic": True, "color": "gray"}}]}}
    ]
    for c in campaigns:
        new_blocks.append({"object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {"rich_text": [
                {"type": "text", "text": {"content": f"🟢 {c['plataforma']}  |  {c['nome']}  |  Ativa"}}
            ]}})

    result = notion_patch(
        f"https://api.notion.com/v1/blocks/{page_id}/children",
        {"after": last_id, "children": new_blocks}
    )
    return bool(result.get("results"))

# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    try:
        changed = [f.strip() for f in open("changed_files.txt").read().splitlines() if f.strip()]
    except FileNotFoundError:
        print("Nenhum arquivo de diff encontrado"); return
    if not changed:
        print("Nenhum relatório detectado"); return

    print(f"Arquivos detectados: {changed}")

    for file_path in changed:
        parts = file_path.split("/")
        if len(parts) < 3: continue
        folder, file_name = parts[1], parts[-1]
        if "." not in file_name: continue

        config = CLIENT_MAP.get(folder)
        if not config:
            print(f"  Pasta '{folder}' sem mapeamento"); continue

        platform  = detect_platform(file_name)
        content   = fetch_file_content(file_path)
        campaigns = extract_campaigns(content, platform) if content else []

        print(f"  [{folder}] {file_name} | {platform} | {len(campaigns)} campanhas ativas")

        # 1. Link do relatório → todos os clientes da pasta
        for client in config["link_clients"]:
            ok = add_report_link(client["notion_id"], file_name, file_path)
            print(f"  {'✅' if ok else '❌'} Link → {client['nome']}")

        # 2. Campanhas → roteamento por nome do arquivo
        if campaigns:
            fn_lower = file_name.lower()
            camp_routing = config.get("camp_routing", {})

            if camp_routing:
                # Pasta compartilhada: rotear pelo keyword no nome do arquivo
                matched = False
                for keyword, clients in camp_routing.items():
                    if keyword in fn_lower:
                        for client in clients:
                            ok = update_campaigns(client["notion_id"], campaigns)
                            print(f"  {'✅' if ok else '❌'} Campanhas → {client['nome']} ({len(campaigns)} ativas)")
                        matched = True
                        break
                if not matched:
                    # Sem match de keyword: atualiza todos
                    for client in config["link_clients"]:
                        ok = update_campaigns(client["notion_id"], campaigns)
                        print(f"  {'✅' if ok else '❌'} Campanhas → {client['nome']} ({len(campaigns)} ativas)")
            else:
                # Pasta exclusiva: atualiza todos os clientes
                for client in config["link_clients"]:
                    ok = update_campaigns(client["notion_id"], campaigns)
                    print(f"  {'✅' if ok else '❌'} Campanhas → {client['nome']} ({len(campaigns)} ativas)")
        else:
            print(f"  ⚠️  Nenhuma campanha ativa extraída — seção Campanhas mantida")

if __name__ == "__main__":
    main()
