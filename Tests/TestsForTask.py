from collections import Counter

import pytest
import requests
import json
from jsonschema import validate

endpoint: str = "https://swapi.co/api/people/"
people_list = []


@pytest.fixture
def get_people_list():
    global people_list
    if len(people_list) is 0:
        next_url = endpoint
        while True:
            json_response = get_page(next_url)
            lastrequestpeople = json_response["results"]
            people_list.extend(lastrequestpeople)
            if json_response["next"] is not None:
                next_url = json_response["next"]
            else:
                break
    return people_list


def get_people_count():
    count = get_page(endpoint)["count"]
    return count


def search(what_to_search):
    search_result = get_page(endpoint + "?search=" + what_to_search)["results"]
    return search_result


def get_page(url):
    response = requests.get(url)
    json_content = json.loads(response.content)
    return json_content


def test_people_count(get_people_list):
    assert (len(get_people_list) == get_people_count())


def test_people_uniqueness(get_people_list):
    names_list = []
    for hero in get_people_list:
        names_list.append(hero["name"])
    counter = Counter(names_list)
    assert len(names_list) == len(counter)


def test_search_insensitive_upper(get_people_list):
    test_name = get_people_list[0]["name"]
    result = search(test_name[0:3].upper())
    print(result[0]["name"])


def test_search_insensitive_lower(get_people_list):
    test_name = get_people_list[0]["name"]
    result = search(test_name[2:4].upper())
    print(result[0]["name"])


def test_search_secondword_partial_upper():
    assert requests.get("https://swapi.co/api/people/?page=0").status_code == 404


@pytest.mark.parametrize("name, expected", [("Skywalker", 3), ("Vader", 1), ("Darth", 2)])
def test_wtf(name, expected):
    assert len(search(name)) == expected


schema = {
    "type": "object",
    "properties": {
        "count": {"type": "number"},
        "next": {"type": "string"},
        "previous": {"type": ["string", "null"]}
    },
}


@pytest.fixture
def get_people_schema():
    people_schema = {
      "type": "object",
      "required": [
        "name",
        "height",
        "mass",
        "hair_color",
        "skin_color",
        "eye_color",
        "birth_year",
        "gender",
        "homeworld",
        "films",
        "species",
        "vehicles",
        "starships",
        "created",
        "edited",
        "url"
      ],
      "properties": {
        "name": {
          "type": "string",
        },
        "height": {
          "type": "string",
        },
        "mass": {
          "type": "string",
        },
        "hair_color": {
          "type": "string",
        },
        "skin_color": {
          "type": "string",
        },
        "eye_color": {
          "type": "string",
        },
        "birth_year": {
          "type": "string",
        },
        "gender": {
          "type": "string",
        },
        "homeworld": {
          "type": "string",
        },
        "films": {
          "type": "array",
          "items": {
            "type": "string",
          }
        },
        "species": {
          "type": "array",
          "items": {
            "type": "string",
          }
        },
        "vehicles": {
          "type": "array",
          "items": {
            "type": "string",
          }
        },
        "starships": {
          "type": "array",
          "items": {
            "type": "string",
          }
        },
        "created": {
          "type": "string",
        },
        "edited": {
          "type": "string",
        },
        "url": {
          "type": "string",
        }
      }
    }
    return people_schema


@pytest.fixture
def people_schema():
    response = requests.get(endpoint + "schema")
    return json.loads(response.content)


def test_new_schema(people_schema, get_people_list):
    for pupil in get_people_list:
        validate(pupil, people_schema)


def test_people_schema(get_people_schema, get_people_list):
    for pupil in get_people_list:
        validate(pupil, get_people_schema)


def test_peo(get_people_schema, get_people_list):
    validate(get_people_list[0], get_people_schema)


# if __name__ == '__main__':
