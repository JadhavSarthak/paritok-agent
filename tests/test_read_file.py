from agent.tools.read_file import read_file


def test_existing_file():
    content = read_file("README.md")
    assert len(content) > 0


def test_missing_file():
    content = read_file("missing_file.txt")
    assert "does not exist" in content