from models.memory_log import MemoryLog
from models.todo_list import ToDoList
from models.special_dates import SpecialDates
from models.mood_tracker import MoodTracker
from models.analytics import Analytics
from models.date_ideas import DateIdeas
from utilities import get_quote

def main_menu():
    memory_log = MemoryLog()
    todo_list = ToDoList()
    special_dates = SpecialDates()
    mood_tracker = MoodTracker()
    analytics = Analytics(memory_log, todo_list, special_dates)
    date_ideas = DateIdeas()

    while True:
        print("\n=== Moments Together ===")
        print("1. Memory Management")
        print("2. To-Do List Management")
        print("3. Special Dates Management")
        print("4. Mood Tracker")
        print("5. Date Ideas")
        print("6. Analytics Dashboard")
        print("7. Exit")

        print("\nToday's Love Quote:")
        print(get_quote())

        choice = input("\nEnter your choice: ")

        if choice == "1":
            memory_management(memory_log)
        elif choice == "2":
            todo_list_management(todo_list)
        elif choice == "3":
            special_dates_management(special_dates)
        elif choice == "4":
            mood_tracker_management(mood_tracker)
        elif choice == "5":
            date_ideas_management(date_ideas)
        elif choice == "6":
            analytics.show_summary()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def memory_management(memory_log):
    while True:
        print("\n=== Memory Management ===")
        print("1. Add Memory")
        print("2. View Memories")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            description = input("Enter memory description: ")
            location = input("Enter location for weather info: ")
            memory_log.add_memory(description, location)
        elif choice == "2":
            memory_log.view_memories()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def todo_list_management(todo_list):
    while True:
        print("\n=== To-Do List Management ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            task = input("Enter task description: ")
            location = input("Enter location for weather info: ")
            todo_list.add_task(task, location)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            todo_list.view_tasks()
            try:
                task_number = int(input("Enter task number to mark as complete: "))
                todo_list.mark_complete(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def special_dates_management(special_dates):
    while True:
        print("\n=== Special Dates Management ===")
        print("1. Add Special Date")
        print("2. View Special Dates")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter the name of the special occasion: ")
            date = input("Enter the date (YYYY-MM-DD): ")
            special_dates.add_date(name, date)
        elif choice == "2":
            special_dates.view_dates()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def mood_tracker_management(mood_tracker):
    while True:
        print("\n=== Mood Tracker ===")
        print("1. Log Mood")
        print("2. View Moods")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            mood = input("Enter your mood (happy, neutral, sad): ")
            mood_tracker.add_mood(mood)
        elif choice == "2":
            mood_tracker.view_moods()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def date_ideas_management(date_ideas):
    while True:
        print("\n=== Date Ideas ===")
        print("1. Add a Date Idea")
        print("2. Get a Random Date Idea")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        if choice == "1":
            idea = input("Enter your date idea: ")
            date_ideas.add_date_idea(idea)
        elif choice == "2":
            print("\n=== Random Date Idea ===")
            print(f"Try this: {date_ideas.get_random_idea()}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()