from http import HTTPStatus as status

from tests.utils import DbTest


class AuthTest(DbTest):
    def test_login(self):
        res = self.client.post('/auth/signup')
        breakpoint()
        self.assertEqual(res._status_code, status.BAD_REQUEST)

import unittest
if __name__ == '__main__':
    unittest.main()

