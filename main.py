from agent.context_store import ContextStore
from agent.tools.read_file import read_file
store = ContextStore()

store.add_message("user", "Fix the login bug.")
store.add_message("tool", "Read auth.py")
store.add_message("assistant", "Bug found in auth.py line 42.")

print(store.get_history())

print(f"\nMessages stored: {len(store)}")

store.clear()

print("\nAfter clearing:")
print(store.get_history())

print("\nReading README.md...\n")

content = read_file("README.md")

print(content[:500])