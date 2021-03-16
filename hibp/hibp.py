import requests

from .constants import API_URL
from .constants import BREACH
from .constants import BREACHED_ACCOUNT
from .constants import BREACHES
from .constants import DATA_CLASSES
from .constants import HEADERS
from .constants import PASTE_ACCOUNT


def get(service, params=None, search_term=None):
    query = f'{API_URL}/{service}'
    if search_term:
        query += f'/{search_term}'
    if params:
        query += f'?{params}'

    response = requests.get(query, headers=HEADERS)
    return response


def breached_account(email, truncate=True, domain=None, unverified=False):
    params = f'truncateResponse={truncate}&includeUnverified={unverified}'
    if domain:
        params += f'&domain={domain}'
    return get(BREACHED_ACCOUNT, params=params, search_term=email)


def breaches(domain=None):
    params = str()
    if domain:
        params = f'domain={domain}'
    return get(BREACHES, params=params)


def breach(breach_name):
    return get(BREACH, search_term=breach_name)


def data_classes():
    return get(DATA_CLASSES)


def paste_account(email):
    return get(PASTE_ACCOUNT, search_term=email)
