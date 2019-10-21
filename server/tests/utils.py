from unittest import TestCase
import os
os.environ['FLASK_ENV'] = 'testing'
import psycopg2

from main import create_app
from migrate import migrate_str, get_latest_migration_version
from utils.db import get_db_info


class FlaskIntegrationTest(TestCase):
    @classmethod
    def setUpClass(cls):
        print('hi from FlaskIntegrationTest!')
        cls.app = create_app()


class DbTest(FlaskIntegrationTest):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        print('hi from DbTest!')
        cls.conn = psycopg2.connect(**get_db_info())
        # run migrations, detect current migration by default
        sql = migrate_str('up', 1, get_latest_migration_version())
        cur = cls.conn.cursor()
        cur.execute(sql)
        cls.conn.commit()
        cur.close()

    @classmethod
    def tearDownClass(cls):
        print('bye from DbTest!')
        sql = migrate_str('down', get_latest_migration_version(), 1)
        cur = cls.conn.cursor()
        cur.execute(sql)
        cls.conn.commit()
        cur.close()
        cls.conn.close()

