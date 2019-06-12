import pytest
import requests
import string
from collections import Counter
from jsonschema import validate

from conftest import endpoint


def test_people_count(people_list, people_count):
    assert (len(people_list) == people_count)


def test_people_uniqueness(people_list):
    names_list = []
    for hero in people_list:
        names_list.append(hero["name"])
    counter = Counter(names_list)
    assert len(names_list) == len(counter)


def test_search_insensitive_upper(people_list, search_in_peoples):
    test_name = people_list[0]["name"]
    result = search_in_peoples(test_name[0:3].upper())
    print(result[0]["name"])


def test_search_insensitive_lower(people_list, search_in_peoples):
    test_name = people_list[0]["name"]
    result = search_in_peoples(test_name[2:4].upper())
    print(result[0]["name"])


def test_page0_dont_exists():
    assert requests.get(endpoint + "?page=0").status_code == 404


@pytest.mark.parametrize("name, expected", [("Skywalker", 3), ("Vader", 1), ("Darth", 2)])
def test_wtf(name, expected, search_in_peoples):
    assert len(search_in_peoples(name)) == expected


def test_people_schema(people_schema, people_list):
    for person in people_list:
        validate(person, people_schema)


@pytest.mark.parametrize("what_to_search", [x for x in (string.ascii_lowercase + string.digits)])
def test_incredible(what_to_search, search_in_peoples):
    if what_to_search not in ["0", "6", "9"]:
        assert len(search_in_peoples(what_to_search)) > 0
