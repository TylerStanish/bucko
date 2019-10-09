import psycopg2
import pathlib
import sys

from utils import get_db_info


def migrate(up_or_down, v1, v2):
    conn = psycopg2(**get_db_info())


if __name__ == '__main__':
    mirgrate(*sys.argv)

