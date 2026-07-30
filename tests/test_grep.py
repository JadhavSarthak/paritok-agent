from pathlib import Path

from agent.tools.grep import grep


def test_existing_pattern():
    results = grep(".", "ContextStore")

    assert isinstance(results, list)


def test_missing_pattern():
    temp_dir = Path("temp_empty_test")
    temp_dir.mkdir(exist_ok=True)

    (temp_dir / "sample.txt").write_text(
        "Hello World\nPython\nAI",
        encoding="utf-8"
    )

    results = grep(str(temp_dir), "THIS_PATTERN_SHOULD_NOT_EXIST_12345")

    assert results == []

    (temp_dir / "sample.txt").unlink()
    temp_dir.rmdir()


def test_invalid_directory():
    results = grep("invalid_directory", "ContextStore")

    assert results == []


def test_multiple_matches():
    temp_dir = Path("temp_test")

    temp_dir.mkdir(exist_ok=True)

    (temp_dir / "a.txt").write_text(
        "hello\nContextStore\nbye",
        encoding="utf-8"
    )

    (temp_dir / "b.txt").write_text(
        "ContextStore\nanother line",
        encoding="utf-8"
    )

    results = grep(str(temp_dir), "ContextStore")

    assert len(results) == 2

    for file in temp_dir.iterdir():
        file.unlink()

    temp_dir.rmdir()