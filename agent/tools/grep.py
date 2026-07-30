"""
grep.py

Purpose:
    Search recursively through a project directory and return all
    occurrences of a given search pattern.

Author:
    Sarthak Jadhav

Project:
    TokenLean Agent
"""

from pathlib import Path
from typing import List


def grep(directory: str, pattern: str) -> List[dict]:
    """
    Search recursively for a pattern inside all text files.

    Args:
        directory: Directory to search.
        pattern: Text pattern to find.

    Returns:
        List of matching dictionaries with file, line number, and text.
    """

    root = Path(directory)

    if not root.exists() or not root.is_dir():
        return []

    results = []

    for file in root.rglob("*"):

        if not file.is_file():
            continue

        try:
            with file.open("r", encoding="utf-8") as f:

                for line_number, line in enumerate(f, start=1):

                    if pattern in line:

                        results.append(
                            {
                                "file": str(file.relative_to(root)),
                                "line": line_number,
                                "text": line.strip(),
                            }
                        )

        except (UnicodeDecodeError, PermissionError, OSError):
            continue

    return results