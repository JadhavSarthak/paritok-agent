from agent.tools.run_shell import run_shell


def test_pwd():
    result = run_shell("pwd")

    assert result["success"] is True
    assert result["returncode"] == 0
    assert result["stdout"] != ""


def test_ls():
    result = run_shell("ls")

    assert result["success"] is True
    assert result["returncode"] == 0


def test_python_version():
    result = run_shell("python --version")

    assert result["success"] is True
    assert "Python" in result["stdout"] or "Python" in result["stderr"]


def test_empty_command():
    result = run_shell("")

    assert result["success"] is False
    assert result["returncode"] == -1


def test_blocked_command():
    result = run_shell("rm -rf /")

    assert result["success"] is False
    assert result["returncode"] == -1