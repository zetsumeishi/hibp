from config import KEY

HEADERS = {"User-Agent": "hibpy", "hibp-api-key": KEY}
VERSION = "v3"
URL = f"https://haveibeenpwned.com/api/{VERSION}"

# Services
# All breaches for an account
BREACHED_ACCOUNT = "breachedaccount"
# All breached sites on HIPB
BREACHES = "breaches"
# Single breached site
BREACH = "breach"
# All data classes (eg: Email addresses, passwords, etc...)
DATA_CLASSES = "dataclasses"
# All pastes for an account
PASTE_ACCOUNT = "pasteaccount"
