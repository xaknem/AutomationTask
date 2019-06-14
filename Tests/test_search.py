import pytest
import string


def test_partial_from_the_beginning(search_in_peoples):
    name = "C-3"
    result = search_in_peoples(name)
    assert result[0]["name"] == "C-3PO"


def test_partial_from_the_middle(search_in_peoples):
    name = "-3P"
    result = search_in_peoples(name)
    assert result[0]["name"] == "C-3PO"


def test_entirely_upper(search_in_peoples):
    name = "Boba Fett"
    result = search_in_peoples(name.upper())
    assert result[0]["name"] == name


def test_entirely_lower(search_in_peoples):
    name = "Boba Fett"
    result = search_in_peoples(name.lower())
    assert result[0]["name"] == name


@pytest.mark.parametrize("name, expected", [("Skywalker", 3), ("Vader", 1), ("Darth", 2)])
def test_wtf(name, expected, search_in_peoples):
    assert len(search_in_peoples(name)) == expected


@pytest.mark.parametrize("what_to_search", [x for x in (string.ascii_lowercase + string.digits)])
def test_incredible(what_to_search, search_in_peoples):
    if what_to_search not in ["0", "6", "9"]:
        assert len(search_in_peoples(what_to_search)) > 0
