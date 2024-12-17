from utilities import load_data, save_data, get_weather

class ToDoList:
    def __init__(self, filename="data/todo.json"):
        self.filename = filename
        self.tasks = load_data(filename, [])

    def add_task(self, task, location):
        weather = get_weather(location)
        self.tasks.append({"task": task, "completed": False, "location": location, "weather": weather})
        save_data(self.filename, self.tasks)
        print("Task added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks added yet.")
            return
        for i, task in enumerate(self.tasks):
            status = "Done" if task["completed"] else "Pending"
            weather = task.get("weather", "Weather data not available")
            location = task.get("location", "-")
            print(f"{i + 1}. {task['task']} [{status}] (Weather in {location}: {weather})")

    def mark_complete(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            save_data(self.filename, self.tasks)
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
