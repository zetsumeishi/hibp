import unittest
from time import sleep

from hibp.hibp import breach
from hibp.hibp import breached_account
from hibp.hibp import breaches
from hibp.hibp import data_classes
from hibp.hibp import paste_account

BREACH_KEYS = [
    ('Name', str),
    ('Title', str),
    ('Domain', str),
    ('BreachDate', str),
    ('AddedDate', str),
    ('ModifiedDate', str),
    ('PwnCount', int),
    ('Description', str),
    ('LogoPath', str),
    ('DataClasses', list),
    ('IsVerified', bool),
    ('IsFabricated', bool),
    ('IsSensitive', bool),
    ('IsRetired', bool),
    ('IsSpamList', bool),
]


class HIBPTestCase(unittest.TestCase):
    def setUp(self):
        self.content_type = 'application/json; charset=utf-8'

    def test_breached_account(self):
        sleep(1.5)
        response = breached_account(
            'oliver@gmail.com',
            truncate=False,
            unverified=True,
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], self.content_type)
        response = response.json()
        for elem in BREACH_KEYS:
            self.assertIsInstance(response[0][elem[0]], elem[1])

        sleep(1.5)
        response = breached_account(
            'oliver@gmail.com',
            truncate=False,
            unverified=True,
            domain='adobe.com',
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], self.content_type)
        response = response.json()
        for elem in BREACH_KEYS:
            self.assertIsInstance(response[0][elem[0]], elem[1])

        sleep(1.5)
        response = breached_account(
            'john.doe@nothacked.com',
            truncate=False,
            unverified=True,
        )
        self.assertEqual(response.status_code, 404)

    def test_breaches(self):
        sleep(1.5)
        response = breaches()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], self.content_type)
        response = response.json()
        for elem in BREACH_KEYS:
            self.assertIsInstance(response[0][elem[0]], elem[1])

        sleep(1.5)
        response = breaches(domain='adobe.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], self.content_type)
        response = response.json()
        for elem in BREACH_KEYS:
            self.assertIsInstance(response[0][elem[0]], elem[1])

    def test_breach(self):
        sleep(1.5)
        response = breach('Canva')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], self.content_type)
        response = response.json()
        for elem in BREACH_KEYS:
            self.assertIsInstance(response[elem[0]], elem[1])

    def test_data_classes(self):
        sleep(1.5)
        response = data_classes()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], self.content_type)
        response = response.json()
        for cls in response:
            self.assertIsInstance(cls, str)

    def test_paste_account(self):
        sleep(1.5)
        response = paste_account('oliver@gmail.com')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], self.content_type)
        response = response.json()
        self.assertIsInstance(response[0]['Id'], str)
        self.assertIsInstance(response[0]['Source'], str)
        self.assertIsInstance(response[0]['EmailCount'], int)
        self.assertTrue(type(response[0]['Title']) in [str, type(None)])
        self.assertTrue(type(response[0]['Date']) in [str, type(None)])


if __name__ == '__main__':
    unittest.main()
