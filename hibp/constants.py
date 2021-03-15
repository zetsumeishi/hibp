import os
import sys

try:
    HIBP_API_KEY = os.environ.get('HIBP_API_KEY')
except Exception:
    print(
        'To use this package, please export your API key:\n'
        'export HIBP_API_KEY=\'YOUR_API_KEY\''
    )
    sys.exit(0)

HEADERS = {'User-Agent': 'hibpy', 'hibp-api-key': HIBP_API_KEY}
VERSION = 'v3'
BASE_URL = 'https://haveibeenpwned.com/'
API_URL = f'https://haveibeenpwned.com/api/{VERSION}'

# Services
# All breaches for an account
BREACHED_ACCOUNT = 'breachedaccount'
# All breached sites on HIPB
BREACHES = 'breaches'
# Single breached site
BREACH = 'breach'
# All data classes (eg: Email addresses, passwords, etc...)
DATA_CLASSES = 'dataclasses'
# All pastes for an account
PASTE_ACCOUNT = 'pasteaccount'

HTTP_CODES = {
    '400': '400 - Bad Request',
    '401': '401 - Unauthorised',
    '403': '403 - Forbidden',
    '429': '429 - Too Many Requests',
    '503': '503 - Service Unavailable',
}
