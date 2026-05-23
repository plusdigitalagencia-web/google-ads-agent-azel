import os, json, urllib.request
from datetime import datetime

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json",
}

CLIENT_MAP = {
    "shineray":            ["3690e07d-daa5-819a-9c43-d4f8542270f7"],
    "dra-cejana-dr-bruno": ["3690e07d-daa5-81a1-a2bf-e6257bc4847d",
                            "3690e07d-daa5-8156-8ced-d09c352160b2"],
    "chez-france":         ["3690e07d-daa5-81d1-afeb-eef8b4193324"],
    "speed":               ["3690e07d-daa5-81de-8601-dbb6a9457d69"],
    "hoteligy":            [],
    "nordika":             [],
}

REPO_URL = "https://github.com/plusdigitalagencia-web/google-ads-agent-azel"

def notion_get(url):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def notion_patch(url, body):
    data = json.dumps(body).encode()
    req = urllib.request.Request(url, data=data, headers=HEADERS, method="PATCH")
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())

def find_last_block_in_section(page_id, keyword):
    blocks = notion_get(f"https://api.notion.com/v1/blocks/{page_id}/children?page_size=100")
    in_section = False
    last_id = None
    for b in blocks.get("results", []):
        btype = b.get("type")
        if btype == "heading_2":
            text = b.get("heading_2", {}).get("rich_text", [])
            title = text[0].get("plain_text", "") if text else ""
            if keyword in title:
                in_section = True
                continue
            elif in_section:
                break
        if btype == "divider" and in_section:
            break
        if in_section:
            last_id = b["id"]
    return last_id

def add_entry(page_id, file_name, file_path):
    after_id = find_last_block_in_section(page_id, "Relat")
    if not after_id:
        print(f"  Seção Relatórios não encontrada em {page_id[:8]}")
        return False
    today = datetime.now().strftime("%d/%m/%Y")
    github_url = f"{REPO_URL}/blob/main/{file_path}"
    body = {
        "after": after_id,
        "children": [{"object": "block", "type": "bulleted_list_item",
            "bulleted_list_item": {"rich_text": [
                {"type": "text", "text": {"content": f"📄 {file_name}  —  {today}  → "}},
                {"type": "text", "text": {"content": "Ver no GitHub", "link": {"url": github_url}},
                 "annotations": {"bold": True, "color": "blue"}},
            ]}}]
    }
    result = notion_patch(f"https://api.notion.com/v1/blocks/{page_id}/children", body)
    return bool(result.get("results"))

def main():
    try:
        changed = open("changed_files.txt").read().splitlines()
    except FileNotFoundError:
        print("Nenhum arquivo de diff encontrado"); return
    changed = [f for f in changed if f.strip()]
    if not changed:
        print("Nenhum relatório detectado"); return
    print(f"Arquivos detectados: {changed}")
    for path in changed:
        parts = path.split("/")
        if len(parts) < 3:
            continue
        folder, file_name = parts[1], parts[-1]
        if "." not in file_name:
            continue
        page_ids = CLIENT_MAP.get(folder, [])
        if not page_ids:
            print(f"  Pasta '{folder}' sem mapeamento Notion")
            continue
        for pid in page_ids:
            ok = add_entry(pid, file_name, path)
            print(f"  {'✅' if ok else '❌'} {file_name} → Notion {pid[:8]}...")

if __name__ == "__main__":
    main()
