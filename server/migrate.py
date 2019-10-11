import psycopg2
import pathlib
import sys

from utils import get_db_info
from utils.fs import get_file_contents, get_absolute_path


def replace_sql_imports(sql: str) -> str:
    """
    Replaces instances of \i with the text from that file.
    Doing this to avoid having a separate migration for each
    of the functions
    """
    for line in sql.splitlines():
        if '\i' in line:
            filename = line.split('\i')[1]
            line.replace('\i', get_file_contents(filename))

def migrate(up_or_down, v_start, v_end):
    """
    :param v_start: The starting version
    :param v_end: The ending version (exclusive)
    """
    conn = psycopg2(**get_db_info())
    cur = conn.cursor()
    sql = ''
    get_file_contents('db/migrations/')


if __name__ == '__main__':
    mirgrate(*sys.argv)

