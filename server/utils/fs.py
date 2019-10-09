import os


def get_absolute_path() -> str:
    """
    """
    return os.path.dirname(os.path.realpath(__file__))


def get_file_contents(filename: str) -> str:
    with open(filename, 'r') as f:
        return f.read()

