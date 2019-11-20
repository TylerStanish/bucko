import os


def get_absolute_path(curr_file: str=__file__) -> str:
    """
    """
    return os.path.dirname(os.path.realpath(curr_file))


def get_file_contents(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()

