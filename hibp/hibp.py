from time import sleep

import requests

from .constants import (
    URL,
    HEADERS,
    BREACHED_ACCOUNT,
    BREACHES,
    BREACH,
    DATA_CLASSES,
    PASTE_ACCOUNT,
    HTTP_CODES,
)


class HIBP:
    def __init__(self):
        super(HIBP, self).__init__()

    def get(self, service, params=None, search_term=None):
        query = f"{URL}/{service}"
        if search_term:
            query += f"/{search_term}"
        if params:
            query += f"?{params}"

        response = requests.get(query, headers=HEADERS)
        sleep(1)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("No results found")
        else:
            print(
                f"Something happened: {HTTP_CODES[str(response.status_code)]}"
            )

    def breached_account(
        self, email, truncate=True, domain=None, unverified=False
    ):
        params = f"truncateResponse={truncate}&includeUnverified={unverified}"
        if domain:
            params += f"&domain={domain}"
        return self.get(BREACHED_ACCOUNT, params=params, search_term=email)

    def breaches(self, domain=None):
        params = ""
        if domain:
            params = f"domain={domain}"
        return self.get(BREACHES, params=params)

    def breach(self, breach_name):
        return self.get(BREACH, search_term=breach_name)

    def data_classes(self):
        return self.get(DATA_CLASSES)

    def paste_account(self, email):
        return self.get(PASTE_ACCOUNT, search_term=email)
