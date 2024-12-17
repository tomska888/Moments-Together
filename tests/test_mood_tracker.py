import pytest
from models.mood_tracker import MoodTracker

def test_add_mood(tmp_path):
    test_file = tmp_path / "moods.json"
    moods = MoodTracker(filename=test_file)
    moods.add_mood("Happy")
    assert len(moods.moods) == 1
    assert moods.moods[0]["mood"] == "Happy"
