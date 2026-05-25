"""
Step 1: Run this to get the auth URL, open it in browser, paste the code back.
Step 2: Run with the code as argument: python3 generate_refresh_token.py CODE_HERE

Após gerar o token, atualiza automaticamente os 4 servidores Render.
"""
import os
import sys
import json
import urllib.request
import urllib.parse
from dotenv import load_dotenv

load_dotenv("/etc/secrets/.env", override=True)
load_dotenv(override=True)

CLIENT_ID = os.getenv("GOOGLE_ADS_CLIENT_ID")
CLIENT_SECRET = os.getenv("GOOGLE_ADS_CLIENT_SECRET")
REDIRECT_URI = "http://localhost"
SCOPE = "https://www.googleapis.com/auth/adwords"

RENDER_API_KEY = "rnd_GBGzuFpV1qcE1Yj2GwuSu2SKhaph"
RENDER_SERVICES = [
    {"id": "srv-d809turrjlhs73a4tiv0", "name": "google-ads-mcp (Principal)"},
    {"id": "srv-d85oes8js32c73al9lp0", "name": "google-ads-mcp-assucar"},
    {"id": "srv-d85oevndl75s7393mmu0", "name": "google-ads-mcp-duosfera"},
    {"id": "srv-d85of2dckfvc73e3cai0", "name": "google-ads-mcp-dataknow"},
]

def get_auth_url():
    params = {
        "client_id": CLIENT_ID,
        "redirect_uri": REDIRECT_URI,
        "scope": SCOPE,
        "response_type": "code",
        "access_type": "offline",
        "prompt": "consent",
    }
    return f"https://accounts.google.com/o/oauth2/auth?{urllib.parse.urlencode(params)}"

def exchange_code(code):
    data = urllib.parse.urlencode({
        "code": code,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code",
    }).encode()
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data, method="POST")
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

def get_render_env_vars(service_id):
    req = urllib.request.Request(
        f"https://api.render.com/v1/services/{service_id}/env-vars",
        headers={"Accept": "application/json", "Authorization": f"Bearer {RENDER_API_KEY}"},
    )
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read())

def update_render_token(service_id, new_token):
    env_vars = get_render_env_vars(service_id)
    updated = []
    for item in env_vars:
        ev = item.get("envVar", item)
        if ev["key"] == "GOOGLE_ADS_REFRESH_TOKEN":
            updated.append({"key": ev["key"], "value": new_token})
        else:
            updated.append({"key": ev["key"], "value": ev.get("value", "")})

    data = json.dumps(updated).encode()
    req = urllib.request.Request(
        f"https://api.render.com/v1/services/{service_id}/env-vars",
        data=data,
        method="PUT",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {RENDER_API_KEY}",
        },
    )
    with urllib.request.urlopen(req) as resp:
        return resp.status

def update_local_env(new_token):
    env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
    if not os.path.exists(env_path):
        return
    with open(env_path, "r") as f:
        lines = f.readlines()
    with open(env_path, "w") as f:
        for line in lines:
            if line.startswith("GOOGLE_ADS_REFRESH_TOKEN="):
                f.write(f"GOOGLE_ADS_REFRESH_TOKEN={new_token}\n")
            else:
                f.write(line)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\n=== PASSO 1: Abra este link no navegador ===\n")
        print(get_auth_url())
        print("\nDepois que autorizar, o navegador vai abrir uma página que não carrega.")
        print("Copie o valor de 'code=' da URL e rode:")
        print("python3 execution/generate_refresh_token.py SEU_CODE_AQUI\n")
    else:
        code = sys.argv[1]
        print("Trocando código por tokens...")
        tokens = exchange_code(code)
        rt = tokens.get("refresh_token")
        if not rt:
            print(f"Erro: {tokens}")
            sys.exit(1)

        print(f"\n✓ REFRESH TOKEN:\n{rt}\n")

        print("Atualizando .env local...")
        update_local_env(rt)
        print("✓ .env local atualizado")

        print("\nAtualizando servidores Render...")
        for svc in RENDER_SERVICES:
            try:
                status = update_render_token(svc["id"], rt)
                print(f"  ✓ {svc['name']}")
            except Exception as e:
                print(f"  ✗ {svc['name']} — erro: {e}")

        print("\n✅ Pronto! Todos os servidores atualizados automaticamente.")
