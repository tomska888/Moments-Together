import json
import random
import os
from utilities import load_data, save_data

class DateIdeas:
    def __init__(self, filename="data/date_ideas.json"):
        self.filename = filename
        self.ideas = load_data(filename, [])

    def load_ideas(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []

    def save_ideas(self):
        with open(self.filename, "w") as f:
            json.dump(self.ideas, f, indent=4)

    def add_date_idea(self, idea):
        self.ideas.append(idea)
        save_data(self.filename, self.ideas)
        print("Date idea added successfully!")

    def get_random_idea(self):
        if not self.ideas:
            return "No date ideas available. Add some first!"
        return random.choice(self.ideas)
