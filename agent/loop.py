"""
loop.py

Core Agent Loop for TokenLean Agent.

Responsibilities:
- Receive a user task
- Store task in ContextStore
- Decide which tool to use
- Execute the selected tool
- Store tool output
- Return result

This is the first version of the agent loop.
Currently it uses simple rule-based tool selection.

Later versions will integrate:
- Paritok
- LLM reasoning
- Multi-step planning
"""

from agent.context_store import ContextStore
from agent.tools.read_file import read_file
from agent.tools.grep import grep
from agent.tools.run_shell import run_shell


class AgentLoop:
    """
    Main controller for the TokenLean Agent.
    """

    def __init__(self):
        """
        Initialize the agent.
        """
        self.memory = ContextStore()

    def run(self, task: str):
        """
        Execute a user task.

        Parameters
        ----------
        task : str

        Returns
        -------
        Result from the selected tool.
        """

        # Store user request
        self.memory.add_message("user", task)

        task_lower = task.lower()

        # --------------------------
        # READ FILE
        # --------------------------
        if task_lower.startswith("read "):

            filename = task[5:].strip()

            result = read_file(filename)

            self.memory.add_message(
                "tool",
                f"Read file: {filename}"
            )

            return result

        # --------------------------
        # GREP
        # --------------------------
        elif task_lower.startswith("find "):

            pattern = task[5:].strip()

            result = grep(".", pattern)

            self.memory.add_message(
                "tool",
                f"Searched for: {pattern}"
            )

            return result

        # --------------------------
        # RUN SHELL
        # --------------------------
        elif task_lower.startswith("run "):

            command = task[4:].strip()

            result = run_shell(command)

            self.memory.add_message(
                "tool",
                f"Executed: {command}"
            )

            return result

        # --------------------------
        # UNKNOWN TASK
        # --------------------------
        else:

            message = (
                "Unknown task.\n"
                "Supported commands:\n"
                "Read <file>\n"
                "Find <pattern>\n"
                "Run <command>"
            )

            self.memory.add_message(
                "assistant",
                message
            )

            return message