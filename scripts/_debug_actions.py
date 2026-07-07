#!/usr/bin/env python3
import os, urllib.request, urllib.parse, json

TOKEN = os.environ["DUOSFERA_META_TOKEN"]
BASE = "https://graph.facebook.com/v25.0"
ACCOUNTS = {
    "fernanda": "act_1062379715841653",
    "isabela": "act_1181839902697616",
}

def fetch(account, since, until):
    fields = "campaign_name,ad_name,actions,spend"
    params = urllib.parse.urlencode({
        "fields": fields, "level": "ad",
        "time_range": json.dumps({"since": since, "until": until}),
        "action_breakdowns": "action_type",
        "access_token": TOKEN, "limit": 100
    })
    resp = urllib.request.urlopen(f"{BASE}/{account}/insights?{params}")
    return json.loads(resp.read()).get("data", [])

for name, acc in ACCOUNTS.items():
    print(f"=== {name} ({acc}) ===")
    data = fetch(acc, "2026-06-01", "2026-06-30")
    action_types = set()
    for r in data:
        for a in r.get("actions", []):
            action_types.add((a.get("action_type"), a.get("value")))
    print("action_types encontrados:", action_types)
