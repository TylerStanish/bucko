import unittest
from unittest import TestCase
from unittest.mock import patch, PropertyMock, Mock

from auth.decorators import require_authentication
from auth.exceptions import ApiException
from auth.models import Profile


class TestAuthentication(TestCase):
    @patch('auth.decorators.request')
    @patch('auth.decorators.get_profile_by_token')
    def test_require_authentication(self, get_profile_mock, req_mock):
        # test we get 'Token not provided' for absent header
        # according to here: https://stackoverflow.com/questions/16867509/mock-attributes-in-python-mock
        # we're *supposed* to do it this way?
        headers = {}
        req_mock.headers = headers
        @require_authentication
        def test_route(profile):
            pass
        with self.assertRaises(ApiException) as ctx:
            test_route()
        self.assertEqual('Token not provided', str(ctx.exception))

        # test we get 'Token not provided' for empty header
        headers = {'Authorization': ''}
        req_mock.headers = headers
        @require_authentication
        def test_route(profile):
            pass
        with self.assertRaises(ApiException) as ctx:
            test_route(None)
        self.assertEqual('Token not provided', str(ctx.exception))

        # test we get 'Token does not exist' with malformed header
        get_profile_mock.return_value = None
        headers = {'Authorization': 'Bearer '}
        req_mock.headers = headers
        @require_authentication
        def test_route(profile):
            pass
        with self.assertRaises(ApiException) as ctx:
            test_route()
        self.assertEqual('Token does not exist', str(ctx.exception))

        # test we get 'Token does not exist' when we give a bad token (note mock)
        headers = {'Authorization': 'Bearer bad_token'}
        req_mock.headers = headers
        @require_authentication
        def test_route(profile):
            pass
        with self.assertRaises(ApiException) as ctx:
            test_route()
        self.assertEqual('Token does not exist', str(ctx.exception))

        # *now* we want a valid function
        get_profile_mock.return_value = Profile(
            id=1,
            email='bla@example.com',
            password='hashed password'
        )
        headers = {'Authorization': 'Bearer valid_token'}
        req_mock.headers = headers
        @require_authentication
        def test_route(profile):
            self.assertEqual(
                Profile(
                    id=1,
                    email='bla@example.com',
                    password='hashed password'
                ),
                profile
            )
        try:
            test_route()
        except Exception:
            self.fail('Threw exception when we wanted it not to')


if __name__ == '__main__':
    unittest.main()

