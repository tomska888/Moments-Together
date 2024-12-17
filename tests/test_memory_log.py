import pytest
from models.memory_log import MemoryLog

def test_add_memory(tmp_path, monkeypatch):
    test_file = tmp_path / "memory.json"
    log = MemoryLog(filename=test_file)

    def mock_get_weather(location):
        return "Sunny, 25°C"
    monkeypatch.setattr("utilities.get_weather", mock_get_weather)

    log.add_memory("A day to remember", "TestLocation")
    assert len(log.memories) == 1
    assert log.memories[0]["description"] == "A day to remember"

def test_view_memories(tmp_path, capsys):
    test_file = tmp_path / "memory.json"
    log = MemoryLog(filename=test_file)
    log.add_memory("A day to remember", "TestLocation")
    log.view_memories()
    captured = capsys.readouterr()
    assert "A day to remember" in captured.out
