# Directive: Google Ads Account Overview

## Goal
Get a fast performance snapshot of all accounts under the MCC and identify which ones need immediate attention.

## Inputs
- None required (reads all accounts from MCC automatically)

## Steps

### 1. List all accounts
```bash
python3 execution/test_connection.py
```
Shows all ENABLED and CANCELED accounts with IDs.

### 2. Pull metrics for each active account
For each ENABLED account, run:
```bash
python3 execution/google_ads_metrics_reader.py --customer-id CUSTOMER_ID --days 30
```

Or loop through all accounts for a full MCC overview.

### 3. Prioritize accounts
Flag accounts that need attention:
- **Red**: ROAS < 1x (spending more than making)
- **Yellow**: ROAS 1x–2x or CPA above target
- **Green**: ROAS > 3x, stable or growing

## Active Accounts (as of May 2026)
| Account | ID | Status |
|---------|-----|--------|
| Conta Dra Cejana | 2470198472 | ENABLED |
| Costa e Rassi | 2080767729 | ENABLED |
| Cursos Makeup | 4571513045 | ENABLED |
| Dr. Bruno Ortopedista | 8521374023 | ENABLED |
| Ferravima | 1629787957 | ENABLED |
| Grupo Ferravima | 1537394693 | ENABLED |
| Hi Nutrition | 4174012683 | ENABLED |
| Inades Ads 1 | 2914601254 | ENABLED |
| Levant Digital | 7287032519 | ENABLED |
| PLUS AFILIADO | 4950512913 | ENABLED |
| Quick Power | 4520811474 | ENABLED |
| Shineray Maranhão | 3604927656 | ENABLED |

## Notes
- Always specify `--customer-id` without dashes
- MCC ID: 2694906582 (used as login_customer_id in all API calls)
- All accounts are BRL / America/Sao_Paulo
