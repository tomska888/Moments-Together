from datetime import datetime
from utilities import load_data, save_data, get_weather

class MemoryLog:
    def __init__(self, filename="data/memories.json"):
        self.filename = filename
        self.memories = load_data(filename, [])

    def add_memory(self, description, location):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        weather = get_weather(location)
        self.memories.append({"date": date, "description": description, "location": location, "weather": weather})
        save_data(self.filename, self.memories)
        print("Memory added successfully.")

    def view_memories(self):
        if not self.memories:
            print("No memories logged yet.")
            return
        for memory in self.memories:
            weather = memory.get("weather", "Weather data not available")
            location = memory.get("location", "-")
            print(f"[{memory['date']}] {memory['description']} (Weather in {location}: {weather})")
