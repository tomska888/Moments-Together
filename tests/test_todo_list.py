import pytest
from models.todo_list import ToDoList

def test_add_task(tmp_path, monkeypatch):
    test_file = tmp_path / "todo.json"
    todo = ToDoList(filename=test_file)

    def mock_get_weather(location):
        return "Cloudy, 20°C"
    monkeypatch.setattr("utilities.get_weather", mock_get_weather)

    todo.add_task("Complete project", "TestLocation")
    assert len(todo.tasks) == 1
    assert todo.tasks[0]["task"] == "Complete project"

def test_mark_complete(tmp_path):
    test_file = tmp_path / "todo.json"
    todo = ToDoList(filename=test_file)
    todo.add_task("Complete project", "TestLocation")
    todo.mark_complete(1)
    assert todo.tasks[0]["completed"] is True
