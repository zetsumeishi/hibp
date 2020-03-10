import requests

from .constants import (
    API_URL,
    HEADERS,
    BREACHED_ACCOUNT,
    BREACHES,
    BREACH,
    DATA_CLASSES,
    PASTE_ACCOUNT,
    HTTP_CODES,
)


def get(service, params=None, search_term=None):
    query = f"{API_URL}/{service}"
    if search_term:
        query += f"/{search_term}"
    if params:
        query += f"?{params}"

    response = requests.get(query, headers=HEADERS)
    if response.status_code == 200:
        return response
    elif response.status_code == 404:
        print("No results found")
    else:
        print(f"Something happened: {HTTP_CODES[str(response.status_code)]}")


def breached_account(email, truncate=True, domain=None, unverified=False):
    params = f"truncateResponse={truncate}&includeUnverified={unverified}"
    if domain:
        params += f"&domain={domain}"
    return get(BREACHED_ACCOUNT, params=params, search_term=email)


def breaches(domain=None):
    params = ""
    if domain:
        params = f"domain={domain}"
    return get(BREACHES, params=params)


def breach(breach_name):
    return get(BREACH, search_term=breach_name)


def data_classes():
    return get(DATA_CLASSES)


def paste_account(email):
    return get(PASTE_ACCOUNT, search_term=email)
