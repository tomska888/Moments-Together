import pytest
from models.special_dates import SpecialDates

def test_add_date(tmp_path):
    test_file = tmp_path / "dates.json"
    dates = SpecialDates(filename=test_file)
    dates.add_date("Anniversary", "2024-12-25")
    assert len(dates.dates) == 1
    assert dates.dates[0]["name"] == "Anniversary"
