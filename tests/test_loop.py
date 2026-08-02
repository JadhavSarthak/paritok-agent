from agent.loop import AgentLoop


def test_read_command():
    agent = AgentLoop()

    result = agent.run("Read README.md")

    assert isinstance(result, str)
    assert "TokenLean Agent" in result


def test_find_command():
    agent = AgentLoop()

    result = agent.run("Find ContextStore")

    assert isinstance(result, list)
    assert len(result) > 0


def test_run_command():
    agent = AgentLoop()

    result = agent.run("Run pwd")

    assert result["success"] is True
    assert result["returncode"] == 0


def test_unknown_command():
    agent = AgentLoop()

    result = agent.run("Dance")

    assert "Unknown task" in result


def test_memory_storage():
    agent = AgentLoop()

    agent.run("Read README.md")

    history = agent.memory.get_history()

    assert len(history) >= 2
    assert history[0]["role"] == "user"