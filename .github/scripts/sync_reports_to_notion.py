import os, json, urllib.request
from datetime import datetime

NOTION_TOKEN = os.environ["NOTION_TOKEN"]

# Mapeamento: pasta GitHub → IDs de página no Notion
CLIENT_MAP = {
    "shineray":              ["3690e07d-daa5-819a-9c43-d4f8542270f7"],
    "dra-cejana-dr-bruno":   ["3690e07d-daa5-81a1-a2bf-e6257bc4847d",
                              "3690e07d-daa5-8156-8ced-d09c352160b2"],
    "chez-france":           ["3690e07d-daa5-81d1-afeb-eef8b4193324"],
    "speed":                 ["3690e07d-daa5-81de-8601-dbb6a9457d69"],
    "hoteligy":              [],
    "nordika":               [],
}

REPO_URL = "https://github.com/plusdigitalagencia-web/google-ads-agent-azel"
HEADERS  = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

def notion_get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def notion_patch(url, body):
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, headers=HEADERS, method="PATCH")
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def find_relatorio_block(page_id):
    blocks = notion_get(f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100")
    for b in blocks.get("results", []):
        if b.get("type") == "heading_2":
            texts = b.get("heading_2", {}).get("rich_text", [])
            if texts and "Relat" in texts[0].get("plain_text", ""):
                return b["id"]
    return None

def add_entry(page_id, file_name, file_path):
    block_id = find_relatorio_block(page_id)
    if not block_id:
        print(f"  Seção Relatórios não encontrada na página {page_id[:8]}")
        return False
    today = datetime.now().strftime("%d/%m/%Y")
    github_url = f"{REPO_URL}/blob/main/{file_path}"
    body = {"children": [{"object": "block", "type": "bulleted_list_item",
        "bulleted_list_item": {"rich_text": [
            {"type": "text", "text": {"content": f"📄 {file_name}  —  {today}  → "}},
            {"type": "text", "text": {"content": "Ver no GitHub", "link": {"url": github_url}},
             "annotations": {"bold": True, "color": "blue"}},
        ]}}]}
    notion_patch(f"https://api.notion.com/v1/blocks/{block_id}/children", body)
    return True

def main():
    try:
        changed = open("changed_files.txt").read().splitlines()
    except FileNotFoundError:
        print("Nenhum arquivo alterado"); return
    if not changed:
        print("Nenhum relatório novo"); return

    for path in changed:
        parts = path.split("/")
        if len(parts) < 3:
            continue
        folder, file_name = parts[1], parts[-1]
        if "." not in file_name:
            continue
        page_ids = CLIENT_MAP.get(folder, [])
        if not page_ids:
            print(f"  Pasta '{folder}' sem mapeamento Notion"); continue
        for pid in page_ids:
            ok = add_entry(pid, file_name, path)
            icon = "✅" if ok else "❌"
            print(f"  {icon} {file_name} → {pid[:8]}...")

if __name__ == "__main__":
    main()
