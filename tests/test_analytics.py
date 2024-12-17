from models.analytics import Analytics
from models.memory_log import MemoryLog
from models.todo_list import ToDoList
from models.special_dates import SpecialDates

def test_analytics_summary(tmp_path):
    memory_log = MemoryLog(filename=tmp_path / "memory.json")
    todo_list = ToDoList(filename=tmp_path / "todo.json")
    special_dates = SpecialDates(filename=tmp_path / "dates.json")
    analytics = Analytics(memory_log, todo_list, special_dates)

    memory_log.add_memory("A wonderful day", "TestLocation")
    todo_list.add_task("Test Task", "TestLocation")
    special_dates.add_date("Anniversary", "2024-12-25")

    assert analytics.memory_log.memories[0]["description"] == "A wonderful day"
    assert len(analytics.todo_list.tasks) == 1
    assert len(analytics.special_dates.dates) == 1
