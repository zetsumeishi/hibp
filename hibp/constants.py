import logging
import os

try:
    HIBP_API_KEY = os.environ.get('HIBP_API_KEY')
except Exception:
    logging.warning(
        'To use this package, please add your API key to your environment:\n'
        'export HIBP_API_KEY="YOUR_API_KEY"',
    )
    HIBP_API_KEY = 'MISSING_API_KEY'

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
