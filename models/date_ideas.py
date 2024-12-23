import random
from utilities import load_data, save_data

class DateIdeas:
    def __init__(self, filename="data/date_ideas.json"):
        self.filename = filename
        self.ideas = load_data(filename, [])

    def add_date_idea(self, idea):
        self.ideas.append(idea)
        save_data(self.filename, self.ideas)
        print("Date idea added successfully!")

    def get_random_idea(self):
        if not self.ideas:
            return "No date ideas available. Add some first!"
        return random.choice(self.ideas)
