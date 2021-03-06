import json
from unittest import TestCase
import os
os.environ['FLASK_ENV'] = 'testing'
import psycopg2

from main import create_app
from migrate import migrate_str, get_latest_migration_version
from utils.db import get_db_info
from utils.fs import get_file_contents


class FlaskIntegrationTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()


class DbTest(FlaskIntegrationTest):
    PRIMARY_EMAIL = 'tystanish@gmail.com'

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.conn = psycopg2.connect(**get_db_info())
        # run migrations, detect current migration by default
        sql = migrate_str('up', 1, get_latest_migration_version())
        cur = cls.conn.cursor()
        cur.execute(sql)
        cls.conn.commit()
        cur.close()

    @classmethod
    def tearDownClass(cls):
        sql = migrate_str('down', get_latest_migration_version(), 1)
        cur = cls.conn.cursor()
        cur.execute(sql)
        cls.conn.commit()
        cur.close()
        cls.conn.close()

    def setUp(self):
        # TODO please allow having some sort of sql initial data that each test can specify?
        cur = self.__class__.conn.cursor()
        cur.execute(get_file_contents('tests/data/create.sql'))
        self.__class__.conn.commit()

    def tearDown(self):
        # TODO please clear database! Don't migrate down, just delete all records
        cur = self.__class__.conn.cursor()
        cur.execute(get_file_contents('tests/data/drop.sql'))
        self.__class__.conn.commit()

    def signup(self, email, password):
        return self.client.post(
            '/api/auth/signup',
            content_type='application/json',
            data=json.dumps({'email': email, 'password': password})
        )

    def login(self, email, password):
        return self.client.post(
            '/api/auth/login',
            content_type='application/json',
            data=json.dumps({'email': email, 'password': password})
        )


