from datetime import datetime

class Analytics:
    def __init__(self, memory_log, todo_list, special_dates):
        self.memory_log = memory_log
        self.todo_list = todo_list
        self.special_dates = special_dates

    def show_summary(self):
        print("\n=== Analytics Dashboard ===")
        print(f"Total memories logged: {len(self.memory_log.memories)}")
        completed_tasks = sum(1 for task in self.todo_list.tasks if task['completed'])
        pending_tasks = len(self.todo_list.tasks) - completed_tasks
        print(f"Tasks completed: {completed_tasks}")
        print(f"Tasks pending: {pending_tasks}")
        today = datetime.now().date()
        upcoming_dates = [date for date in self.special_dates.dates if datetime.strptime(date['date'], "%Y-%m-%d").date() > today]
        print(f"Upcoming special dates: {len(upcoming_dates)}")
