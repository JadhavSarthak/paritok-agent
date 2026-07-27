"""
context_store.py

Stores the complete history of an agent session.

This is the agent's memory. Every interaction
(user messages, tool outputs, observations, etc.)
is appended here.

Later, pruner.py will use this history and ask
Paritok to keep only the relevant parts before
each LLM call.
"""


class ContextStore:
    """
    Stores all messages generated during an agent session.
    """

    def __init__(self):
        """
        Create an empty conversation history.
        """
        self.history = []

    def add_message(self, role: str, content: str):
        """
        Add a message to the history.

        Parameters
        ----------
        role : str
            user, assistant, tool, system

        content : str
            Actual message text
        """

        message = {
            "role": role,
            "content": content
        }

        self.history.append(message)

    def get_history(self):
        """
        Return the complete conversation history.
        """

        return self.history

    def clear(self):
        """
        Remove all stored messages.
        """

        self.history.clear()

    def __len__(self):
        """
        Allows len(context_store)
        """

        return len(self.history)