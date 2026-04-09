"""
INTERNAL USE ONLY - DEVELOPMENT TESTING
Project: HomeToGo Infrastructure Audit 2026
Note: These are canary credentials. Do not use in production.
"""

# --- AWS Infrastructure Access ---
# Target: engineering.hometogo.com / s3-storage-backups
AWS_ACCESS_KEY_ID = "AKIA5F7DEXAMPLE8H2Q"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
AWS_DEFAULT_REGION = "us-west-2"

# --- Database Credentials ---
# Target: distributionapi.hometogo.com (Production Mirror)
DB_CONFIG = {
    "db_user": "htg_prod_admin",
    "db_pass": "H0me2G0_Secure_!2026_Audit",
    "db_host": "104.17.185.107", # Associated with distributionapi
    "db_port": 5432,
    "connection_string": "postgresql://htg_prod_admin:H0me2G0_Secure_!2026_Audit@104.17.185.107:5432/hometogo_main"
}

# --- Payment Gateway Keys ---
# Target: payments.hometogo.com
STRIPE_LIVE_SECRET = "sk_live_51MzXy2LkdR7X9zR2_fake_stripe_key_001"
STRIPE_WEBHOOK_SECRET = "whsec_72839405abcdef1234567890abcdef12"

# --- Messaging & Notification Services ---
# Target: messagingapi.hometogo.com / sendgrid-outbound
SENDGRID_API_KEY = "SG.v2_8f2jH0S1S-dummy-92kL.mQ7_xP9zR2_fake_key_001"
MAIL_SERVER_PASS = "Barracuda_Secure_Relay_77x!"

# --- Cloudflare Management ---
# Target: uat-distributionapi.hometogo.com
CF_API_TOKEN = "4c9d7a2b8e3f1g0h9i8j7k6l5m4n3o2p1q0r"
CF_ZONE_ID = "66fe95_dummy_zone_id_01"

# --- Internal Engineering Tokens ---
# Target: itsm.hometogo.com
JIRA_AUTH_TOKEN = "ATATT3xFfGF0b3JlX2tleV8xMjM0NTY3ODkwX2F1ZGl0X3Rlc3RfMTIzNDU2Nzg5MA==" # Base64 style
GH_PERSONAL_ACCESS_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyzABCD"

def get_connection():
    """Mock function to simulate service initialization."""
    print(f"Initializing connection to {DB_CONFIG['db_host']}...")
    return True
