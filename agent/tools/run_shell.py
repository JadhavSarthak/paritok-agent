"""
run_shell.py

Purpose:
    Safely execute allowed shell commands and capture their output.

Author:
    Sarthak Jadhav

Project:
    TokenLean Agent
"""

import subprocess
import shlex


# Commands that the agent is allowed to execute.
ALLOWED_COMMANDS = {
    "pwd",
    "ls",
    "git",
    "python",
    "pytest",
}


def run_shell(command: str) -> dict:
    """
    Execute a shell command safely.

    Args:
        command: Command to execute.

    Returns:
        Dictionary containing:
            success
            stdout
            stderr
            returncode
    """

    try:
        parts = shlex.split(command)

        if not parts:
            return {
                "success": False,
                "stdout": "",
                "stderr": "Empty command.",
                "returncode": -1,
            }

        if parts[0] not in ALLOWED_COMMANDS:
            return {
                "success": False,
                "stdout": "",
                "stderr": f"Command '{parts[0]}' is not allowed.",
                "returncode": -1,
            }

        result = subprocess.run(
            parts,
            capture_output=True,
            text=True,
            timeout=10,
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
            "returncode": result.returncode,
        }

    except subprocess.TimeoutExpired:

        return {
            "success": False,
            "stdout": "",
            "stderr": "Command timed out.",
            "returncode": -1,
        }

    except Exception as e:

        return {
            "success": False,
            "stdout": "",
            "stderr": str(e),
            "returncode": -1,
        }