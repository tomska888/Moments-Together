from datetime import datetime
from utilities import load_data, save_data

class MoodTracker:
    def __init__(self, filename="data/moods.json"):
        self.filename = filename
        self.moods = load_data(filename, [])

    def add_mood(self, mood):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.moods.append({"date": date, "mood": mood})
        save_data(self.filename, self.moods)
        print("Mood logged successfully.")

    def view_moods(self):
        if not self.moods:
            print("No moods logged yet.")
            return
        for mood in self.moods:
            print(f"[{mood['date']}] Mood: {mood['mood']}")
