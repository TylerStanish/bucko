import psycopg2
import pathlib
import os
import sys
from typing import List

from utils.db import get_db_info
from utils.fs import get_file_contents, get_absolute_path


def get_all_tables(sql):
    for line in sql.splitlines():
        if 'create table' in line:
            yield line.split('create table ')[1].split(' ')[0]


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

def get_latest_migration_version() -> int:
    migrations = os.listdir(os.getcwd() + '/db/migrations')
    max_so_far = 0
    for mig in migrations:
        max_so_far = max(max_so_far, int(mig[1:]))
    return max_so_far

def migrate_str(up_or_down: str, v_start: int, v_end: int) -> str:
    """
    :param v_start: The starting version
    :param v_end: The ending version (inclusive)
    """
    sql = []
    if up_or_down == 'down':
        for version in range(v_end, v_start + 1):
            sql.append(replace_sql_imports(get_file_contents(f'db/migrations/v{version}/{up_or_down}.sql')))
    elif up_or_down == 'up':
        for version in range(v_start, v_end + 1):
            sql.append(replace_sql_imports(get_file_contents(f'db/migrations/v{version}/{up_or_down}.sql')))
    else:
        raise ValueError("up_or_down must be either 'up' or 'down'")
    return '\n'.join(sql)


if __name__ == '__main__':
    up_down, v_start, v_end = sys.argv[1:]
    print(migrate_str(up_down, int(v_start), int(v_end)))

