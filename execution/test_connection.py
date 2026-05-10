"""Test Google Ads API connection and list accounts under MCC."""
import os
from dotenv import load_dotenv
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException

load_dotenv("/etc/secrets/.env", override=True)
load_dotenv(override=True)

config = {
    "developer_token": os.getenv("GOOGLE_ADS_DEVELOPER_TOKEN", "").strip(),
    "client_id": os.getenv("GOOGLE_ADS_CLIENT_ID", "").strip(),
    "client_secret": os.getenv("GOOGLE_ADS_CLIENT_SECRET", "").strip(),
    "refresh_token": os.getenv("GOOGLE_ADS_REFRESH_TOKEN", "").strip(),
    "login_customer_id": os.getenv("GOOGLE_ADS_LOGIN_CUSTOMER_ID", "").strip(),
    "use_proto_plus": True,
}

print(f"DEBUG client_id='{config['client_id'][:12]}...' secret='{config['client_secret'][:6]}...' login_id='{config['login_customer_id']}' token='{config['developer_token'][:6]}...'")
client = GoogleAdsClient.load_from_dict(config)

query = """
    SELECT
        customer_client.client_customer,
        customer_client.descriptive_name,
        customer_client.currency_code,
        customer_client.time_zone,
        customer_client.status
    FROM customer_client
    WHERE customer_client.level = 1
"""

service = client.get_service("GoogleAdsService")
login_id = os.getenv("GOOGLE_ADS_LOGIN_CUSTOMER_ID")

try:
    response = service.search(customer_id=login_id, query=query)
    print(f"\n✓ Conexão OK — Contas sob o MCC {login_id}:\n")
    for row in response:
        c = row.customer_client
        name = c.descriptive_name or "(sem nome)"
        cid = c.client_customer.split("/")[-1]
        print(f"  [{c.status.name}] {name} — ID: {cid} | {c.currency_code} | {c.time_zone}")
except GoogleAdsException as ex:
    for error in ex.failure.errors:
        print(f"Erro: {error.message}")
