"""
read_file.py

Tool for reading the contents of a file.

This is the first tool used by the TokenLean Agent.
"""

from pathlib import Path


def read_file(file_path: str) -> str:
    """
    Read and return the contents of a text file.

    Parameters
    ----------
    file_path : str
        Path to the file.

    Returns
    -------
    str
        File contents or an error message.
    """

    path = Path(file_path)

    if not path.exists():
        return f"Error: File '{file_path}' does not exist."

    if not path.is_file():
        return f"Error: '{file_path}' is not a file."

    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()

    except PermissionError:
        return f"Error: Permission denied while reading '{file_path}'."

    except UnicodeDecodeError:
        return f"Error: '{file_path}' is not a UTF-8 text file."

    except Exception as e:
        return f"Unexpected Error: {e}"