"""
Step 1: Run this to get the auth URL, open it in browser, paste the code back.
Step 2: Run with the code as argument: python3 generate_refresh_token.py CODE_HERE
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
        if rt:
            print(f"\n✓ REFRESH TOKEN:\n{rt}\n")
            print("Cole em GOOGLE_ADS_REFRESH_TOKEN no .env")
        else:
            print(f"Erro: {tokens}")
