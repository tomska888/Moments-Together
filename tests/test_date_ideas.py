import pytest
from models.date_ideas import DateIdeas

def test_add_date_idea(tmp_path):
    test_file = tmp_path / "date_ideas.json"
    ideas = DateIdeas(filename=test_file)
    ideas.add_date_idea("Go stargazing")
    assert len(ideas.ideas) == 1
    assert ideas.ideas[0] == "Go stargazing"

def test_random_date_idea(tmp_path):
    test_file = tmp_path / "date_ideas.json"
    ideas = DateIdeas(filename=test_file)
    ideas.add_date_idea("Go stargazing")
    assert ideas.get_random_idea() == "Go stargazing"
