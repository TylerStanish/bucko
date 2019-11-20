from http import HTTPStatus as status
import json

from tests.utils import DbTest


class AuthTest(DbTest):
    def test_signup_with_no_data(self):
        res = self.client.post('/api/auth/signup')
        self.assertEqual(res._status_code, status.BAD_REQUEST)

    def test_signup_with_invalid_data(self):
        res = self.client.post(
            '/api/auth/signup',
            content_type='application/json',
            data=json.dumps({'emaillll': 'jkl', 'password': 'hi'})
        )
        self.assertEqual(res._status_code, status.BAD_REQUEST)

    def test_signup(self):
        res = self.signup(self.PRIMARY_EMAIL, 'password')
        self.assertEqual(res._status_code, status.OK)

    def test_login_fails_before_signing_up(self):
        res = self.login(self.PRIMARY_EMAIL, 'password')
        self.assertEqual(res._status_code, status.BAD_REQUEST)

    def test_login_fails_when_password_incorrect(self):
        res = self.signup(self.PRIMARY_EMAIL, 'password')
        res = self.client.post(
            '/api/auth/login',
            content_type='application/json',
            data=json.dumps({'email': self.PRIMARY_EMAIL, 'password': 'wrongpassword'})
        )
        self.assertEqual(res._status_code, status.BAD_REQUEST)

    def test_login(self):
        res = self.signup(self.PRIMARY_EMAIL, 'password')
        res = self.login(self.PRIMARY_EMAIL, 'password')
        self.assertEqual(res._status_code, status.OK)

    def test_login_with_no_data(self):
        res = self.client.post('/api/auth/login')
        self.assertEqual(res._status_code, status.BAD_REQUEST)


import unittest
if __name__ == '__main__':
    unittest.main()

