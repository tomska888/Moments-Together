# Moments Together - Personal Life Tracker
Moments Together is a comprehensive personal life tracker that helps you stay organized, track memories, manage tasks, monitor your mood, and keep important dates in check. This application also provides daily love quotes for a more personalized experience. All data is stored persistently, ensuring you can revisit your moments anytime.

## Features
### 📝 Memory Logging
- Log memories with a description, location, and weather details.
- Easily review all logged memories.
### ✅ Task Management
- Add tasks with descriptions and weather context based on location.
- View tasks with status indicators (Pending/Done).
- Mark tasks as completed.
### 💖 Mood Tracker
- Log your daily mood (Happy, Neutral, or Sad).
- Review past moods to analyze trends over time.
### 📅 Special Dates
- Track special dates like anniversaries, birthdays, or events.
- View how many days are left until an event.
### 🌟 Date Ideas
- Add creative date ideas to a personalized collection.
- Get a random date idea for inspiration.
### 📊 Analytics Dashboard
- See an overview of:
- Total memories logged.
- Tasks completed and pending.
- Upcoming special dates.
### 🌦️ Weather Integration
- Fetch real-time weather data for tasks and memories using the WeatherStack API.
### 💌 Daily Love Quotes
- Enjoy motivational love quotes fetched from the API Ninjas service.
- Quote updates automatically once per day.
### 🔒 Data Persistence
- All data is stored securely in JSON files within a data/ directory.
Project Structure         

## Setup
1. Prerequisites
Ensure you have Python 3.x installed on your system.

2. Clone the Repository
    ```
    git clone https://github.com/yourusername/moments-together.git
    cd moments-together
    ```
3. Install Required Libraries
Install the necessary Python packages:
    ```
    pip install -r requirements.txt
    ```
4. Configure API Keys
Sign up for free API keys from:

    - [WeatherStack](https://weatherstack.com/) (for weather data).
    - [API Ninjas](https://www.api-ninjas.com/) (for love quotes).

    Add your API keys to the config.json file in the following format:
    ```
    {
    "weatherstack_api_key": "your_weatherstack_api_key_here",
    "api_ninjas_key": "your_api_ninjas_key_here"
    }
    ```

## Usage
Run the application by executing:
```
python main.py
```
You will see a structured main menu divided into sections:

### Main Menu
1. Memories
- Log a Memory: Add a new memory with a description and location-based weather.
- View Memories: See all your logged memories.
2. Tasks
- Add Task: Create a task with a description and location-based weather.
- View Tasks: List all tasks with their status (Pending/Done).
- Mark Task Complete: Mark a selected task as completed.
3. Moods
- Log Mood: Record your current mood.
- View Moods: Review your mood history.
4. Special Dates
- Add Special Date: Add an important date.
- View Special Dates: See all upcoming dates with days left until the event.
5. Date Ideas
- Add Date Idea: Save a creative idea for dates or activities.
- Random Date Idea: Get a randomly selected date idea.
6. Analytics
- See a summary of:
    * Memories logged.
    * Tasks completed and pending.
    * Upcoming special dates.
7. Exit
- Quit the application.

## Data Storage
All data is stored in JSON format under the ```data/``` directory:

- ```todo.json```: Stores tasks.
- ```memories.json```: Stores memories.
- ```moods.json```: Stores mood entries.
- ```dates.json```: Stores special dates.
- ```date_ideas```: Stores date ideas.
- ```quote.json```: Stores today's quote.

This ensures persistence between sessions, so your data is always available.

## APIs Used
### Weather Data
- API: WeatherStack
- Purpose: Provides current weather data for a given location.
### Daily Love Quotes
- API: API Ninjas Quotes
- Purpose: Fetches daily motivational quotes related to love.

## Future Enhancements
- User Authentication: Allow multiple users to maintain separate data.
- Advanced Analytics: Add mood trends and weather impact analysis on tasks.