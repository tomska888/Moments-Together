import os
import json
import requests
from datetime import datetime

def load_data(filename, default):
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            return json.load(f)
    return default

def save_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def get_api_key(service_name):
    config = load_data("config.json", {})
    if service_name == "weatherstack":
        key = config.get("WEATHERSTACK_API_KEY")
    elif service_name == "quotes":
        key = config.get("API_NINJAS_KEY")
    else:
        raise ValueError("Invalid service name. Use 'weatherstack' or 'quotes'.")

    if not key:
        raise RuntimeError(f"API key for {service_name} not found in config.json.")
    
    return key

def get_weather(location):
    api_key = get_api_key("weatherstack")
    if not api_key:
        return "API key for weather not found!"
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={location}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if "current" in data:
            weather = data["current"]["weather_descriptions"][0]
            temperature = data["current"]["temperature"]
            return f"{weather}, {temperature}°C"
        else:
            return "Weather data unavailable"
    except requests.RequestException:
        return "Weather data unavailable"

def get_quote():
    quote_file = "data/quote.json"
    today = datetime.now().strftime("%Y-%m-%d")
    
    # Check if quote already exists for today
    quote_data = load_data(quote_file, {})
    if quote_data.get("date") == today:
        return quote_data.get("quote", "No quote available for today.")
    
    api_key = get_api_key("quotes")
    if not api_key:
        return "API key for quotes not found!"
    url = "https://api.api-ninjas.com/v1/quotes?category=love"
    headers = {"X-Api-Key": api_key}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if data:
            quote_text = f"{data[0]['quote']} - {data[0]['author']}"
            save_data(quote_file, {"date": today, "quote": quote_text})
            return quote_text
        return "No love-related quote available."
    except requests.RequestException as e:
        return f"Could not fetch quote: {str(e)}"