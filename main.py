from agent.context_store import ContextStore
from agent.tools.read_file import read_file
from agent.tools.grep import grep
from agent.tools.run_shell import run_shell

def main():
    # -----------------------------
    # ContextStore Demo (Day 1)
    # -----------------------------
    store = ContextStore()

    store.add_message("user", "Fix the login bug.")
    store.add_message("tool", "Read auth.py")
    store.add_message("assistant", "Bug found in auth.py line 42.")

    print("=" * 50)
    print("ContextStore Demo")
    print("=" * 50)

    print(store.get_history())
    print(f"\nMessages stored: {len(store)}")

    store.clear()

    print("\nAfter clearing:")
    print(store.get_history())

    # -----------------------------
    # read_file Demo (Day 1)
    # -----------------------------
    print("\n" + "=" * 50)
    print("Read File Demo")
    print("=" * 50)

    content = read_file("README.md")
    print(content[:500])

    # -----------------------------
    # grep Demo (Day 2)
    # -----------------------------
    print("\n" + "=" * 50)
    print("Grep Demo")
    print("=" * 50)

    pattern = "ContextStore"

    results = grep(".", pattern)

    if not results:
        print(f"No matches found for '{pattern}'")
    else:
        print(f"Found {len(results)} match(es):\n")

        for result in results:
            print(
                f"{result['file']}:{result['line']} -> {result['text']}"
            )
        # -----------------------------
    # Run Shell Demo (Day 3)
    # -----------------------------
    print("\n" + "=" * 50)
    print("Run Shell Demo")
    print("=" * 50)

    result = run_shell("pwd")

    print(f"Success     : {result['success']}")
    print(f"Return Code : {result['returncode']}")

    print("\nSTDOUT:")
    print(result["stdout"])

    if result["stderr"]:
        print("\nSTDERR:")
        print(result["stderr"])
if __name__ == "__main__":
    main()
