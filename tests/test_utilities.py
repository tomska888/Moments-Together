import os
import json
import pytest
from utilities import load_data, save_data, get_weather, get_quote, get_api_key

def test_load_data(tmp_path):
    test_file = tmp_path / "test.json"
    data = {"key": "value"}
    save_data(test_file, data)
    loaded_data = load_data(test_file, {})
    assert loaded_data == data

def test_save_data(tmp_path):
    test_file = tmp_path / "test.json"
    data = {"key": "value"}
    save_data(test_file, data)
    with open(test_file, 'r') as f:
        assert json.load(f) == data

def test_get_weather(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def json(self):
                return {
                    "current": {
                        "weather_descriptions": ["Sunny"],
                        "temperature": 25
                    }
                }
            def raise_for_status(self):
                pass
        return MockResponse()
    
    monkeypatch.setattr("requests.get", mock_get)
    weather = get_weather("TestLocation")
    assert weather == "Sunny, 25°C"

def test_get_quote(monkeypatch):
    def mock_get(*args, **kwargs):
        class MockResponse:
            def json(self):
                return [{"quote": {get_quote}}]
            def raise_for_status(self): 
                pass
        return MockResponse()
    
    monkeypatch.setattr("requests.get", mock_get)
    quote = get_quote()
    assert "love" in quote

def test_get_api_key():
    weatherstack_key = get_api_key("weatherstack")
    assert weatherstack_key is not None

    quotes_key = get_api_key("quotes")
    assert quotes_key is not None