from tests.utils import DbTest


class AuthTest(DbTest):
    def test_sanity(self):
        res = self.client.post('/auth/login')
        self.assertEqual(res._status_code, 200)

