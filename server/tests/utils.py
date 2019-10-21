from unittest import TestCase
import os

import psycopg2

from migrate import migrate_str, get_latest_migration_version
from utils.db import get_db_info


class DbTest(TestCase):
    @classmethod
    def setUpClass(self):
        os.environ['FLASK_ENV'] = 'testing'
        self.conn = psycopg2.connect(**get_db_info())
        # run migrations, detect current migration by default
        sql = migrate_str('up', 1, get_latest_migration_version())
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()

    @classmethod
    def tearDownClass(self):
        sql = migrate_str('down', get_latest_migration_version(), 1)
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()
        self.conn.close()

