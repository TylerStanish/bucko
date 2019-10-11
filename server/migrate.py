import psycopg2
import pathlib
import os
import sys

from utils.db import get_db_info
from utils.fs import get_file_contents, get_absolute_path


def replace_sql_imports(sql: str) -> str:
    """
    Replaces instances of \i with the text from that file.
    Doing this to avoid having a separate migration for each
    of the functions.

    Most postgresql drivers don't support
    metacommands such as \i so we have to implement this functionality
    ourselves
    """
    lines = []
    for line in sql.splitlines():
        if '\i' in line:
            filename = line.split('\i ')[1]
            filepath = os.getcwd() + '/db/' + filename
            line = get_file_contents(filepath)
        lines.append(line)
    return '\n'.join(lines)

def migrate_str(up_or_down: str, v_start: int, v_end: int) -> str:
    """
    :param v_start: The starting version
    :param v_end: The ending version (exclusive)
    """
    sql = []
    for version in range(v_start, v_end):
        sql.append(replace_sql_imports(get_file_contents(f'db/migrations/v{version}/{up_or_down}.sql')))
    return '\n'.join(sql)


if __name__ == '__main__':
    up_down, v_start, v_end = sys.argv[1:]
    print(migrate_str(up_down, int(v_start), int(v_end)))

