from datetime import datetime, timedelta
from http import HTTPStatus as status
import json

from tests.utils import DbTest


class EventsTest(DbTest):
    def test_get_events(self):
        res = self.signup(self.PRIMARY_EMAIL, 'password')
        tok = res.json.get('token')
        res = self.client.get(
            '/event',
            headers={'Authorization': f'Bearer {tok}'}
        )
        self.assertEqual(res._status_code, status.OK)
        self.assertEqual(len(res.json), 0)

        res = self.client.post(
            '/event',
            content_type='application/json',
            data=json.dumps({
                'title': 'the title',
                'eventStart': datetime.utcnow().isoformat(),
                'eventEnd': (datetime.utcnow() + timedelta(hours=1)).isoformat()
            }),
            headers={'Authorization': f'Bearer {tok}'}
        )
        self.assertEqual(res._status_code, status.OK)
        self.assertDictContainsSubset({'title': 'the title'}, res.json)

        res = self.client.get(
            '/event',
            headers={'Authorization': f'Bearer {tok}'}
        )
        self.assertEqual(res._status_code, status.OK)
        self.assertEqual(len(res.json), 1)

import unittest
if __name__ == '__main__':
    unittest.main()

