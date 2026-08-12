#!/usr/bin/env python3
"""Dispatcher - Relatorios Quinta-feira
Aciona todos os relatorios Meta Ads semanais via workflow_dispatch.
Chamado pelo dispatcher-segunda.yml toda quinta as 06:50 BRT.
"""
import os
import json
import time
import urllib.request
import urllib.error

GH_TOKEN = os.environ["GH_PAT"]
REPO = "plusdigitalagencia-web/google-ads-agent-azel"
HEADERS = {
    "Authorization": f"token {GH_TOKEN}",
    "Accept": "application/vnd.github+json",
    "Content-Type": "application/json",
}

# Todos os relatorios que rodam toda quinta-feira
WORKFLOWS = [
    # Data Know - Meta Ads
    ("Leblon Real Estate",  "leblon-meta-report.yml"),
    ("Luxe Icon",           "luxe-icon-meta-report.yml"),
    ("KG Clinica",          "kg-clinica-meta-report.yml"),
    ("Hoteligy",            "hoteligy-meta-report.yml"),
    ("Alcala Homes",        "alcala-homes-meta-report.yml"),
    ("LRS Safety",          "lrs-safety-meta-report.yml"),
    # Duosfera - Meta Ads
    ("Dra. Fernanda",       "dra-fernanda-meta-report.yml"),
    ("Dra. Isabela",        "dra-isabela-meta-report.yml"),
    ("Duosfera Digital",    "duosfera-digital-meta-report.yml"),
]


def dispatch(workflow_file):
    url = f"https://api.github.com/repos/{REPO}/actions/workflows/{workflow_file}/dispatches"
    data = json.dumps({"ref": "main"}).encode()
    req = urllib.request.Request(url, data=data, method="POST")
    for k, v in HEADERS.items():
        req.add_header(k, v)
    try:
        with urllib.request.urlopen(req) as r:
            return r.status == 204
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print(f"  HTTP {e.code}: {body}")
        return False


print("=== Dispatcher Quinta-feira ===")
erros = []

for nome, workflow in WORKFLOWS:
    ok = dispatch(workflow)
    icone = "OK" if ok else "ERRO"
    print(f"{icone} {nome} ({workflow})")
    if not ok:
        erros.append(nome)
    time.sleep(2)

print(f"\nTotal: {len(WORKFLOWS)} workflows | Erros: {len(erros)}")
if erros:
    print(f"Falhas: {chr(44).join(erros)}")
    raise SystemExit(1)
