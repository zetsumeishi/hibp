# hibp [![Build Status](https://travis-ci.org/zetsumeishi/hibp.svg?branch=master)](https://travis-ci.org/zetsumeishi/hibp) [![Coverage Status](https://coveralls.io/repos/github/zetsumeishi/hibp/badge.svg?branch=master)](https://coveralls.io/github/zetsumeishi/hibp?branch=master) [![PyPI version](https://badge.fury.io/py/hibp-zetsumeishi.svg)](https://badge.fury.io/py/hibp-zetsumeishi)

## Introduction

This package was developed on Ubuntu 20 using Python 3.9. It is tested against Python 3.6, 3.7, 3.8, and 3.9.

You need an API key from [HaveIBeenPwned](https://haveibeenpwned.com/API/Key).

## Installation

```
python3 -m pip install hibp-zetsumeishi
export HIBP_API_KEY='YOUR_API_KEY'
```

## Usage

```
from hibp.hibp import (
  breached_account,
  breaches,
  breach,
  data_classes,
  paste_account,
)

response = breached_account('example@example.com')
if response.status_code == 200:
  data = response.json()

print(data)
[
   {
      "Name":"000webhost"
   },
   {
      "Name":"500px"
   },
   ...
]
```

Each function returns a requests.Response object.

### Prototypes

- `breached_account(email, truncate=True, domain=None, unverified=False)`
  - `email` is the email you want to search for
  - `truncate` is a boolean. If `True`, it just returns the name of the breaches association with the email provided. By default, the API truncates responses. Otherwise, it returns the information regarding the breaches.
  - `domain` is a string to search against a specific domain.
  - `unverified`, when `True`, also returns unverified breaches.

- `breaches()`
  - Takes no argument and returns the list of all indexed breaches. But doesn't return unverified breaches.

- `breach(breach_name)`
  - Takes a `breach_name` as argument and returns non-truncated response.

- `data_classes()`
  - Takes no argument, returns a list of all types of data breaches (eg: Phone numbers, credit cards, etc...)

- `paste_account(email)`
  - Takes an email as argument and returns a list of all copy/paste services where the email appears.
