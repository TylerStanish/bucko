from http import HTTPStatus as status
import json

from tests.utils import DbTest


class AuthTest(DbTest):
    def test_signup_with_no_data(self):
        res = self.client.post('/auth/signup')
        self.assertEqual(res._status_code, status.BAD_REQUEST)

    def test_signup(self):
        res = self.client.post(
            '/auth/signup',
            content_type='application/json',
            data=json.dumps({'email': 'jkl', 'password': 'hi'})
        )
        self.assertEqual(res._status_code, status.OK)

    def test_login(self):
        raise NotImplementedError

    def test_signup_with_no_data(self):
        res = self.client.post('/auth/login')
        self.assertEqual(res._status_code, status.BAD_REQUEST)

import unittest
if __name__ == '__main__':
    unittest.main()

