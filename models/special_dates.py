from datetime import datetime
from utilities import load_data, save_data

class SpecialDates:
    def __init__(self, filename="data/dates.json"):
        self.filename = filename
        self.dates = load_data(filename, [])

    def add_date(self, name, date):
        self.dates.append({"name": name, "date": date})
        save_data(self.filename, self.dates)
        print("Special date added successfully.")

    def view_dates(self):
        if not self.dates:
            print("No special dates saved yet.")
            return
        today = datetime.now().date()
        for date in self.dates:
            event_date = datetime.strptime(date['date'], "%Y-%m-%d").date()
            days_left = (event_date - today).days
            status = "(Today!)" if days_left == 0 else f"({days_left} days left)"
            print(f"{date['name']} - {date['date']} {status}")
