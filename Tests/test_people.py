from collections import Counter

import requests
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


def test_page0_dont_exists():
    assert requests.get(endpoint + "?page=0").status_code == 404


def test_people0_dent_exists():
    assert requests.get(endpoint + "0/").status_code == 404


def test_people_schema(people_schema, people_list):
    for person in people_list:
        validate(person, people_schema)

# status code is 200 implicit check
# Проверка того, что все ссылки в ответе рабочие (возвращают ответ 200)
# при отправке запроса по http перекидывает на https
# проверка что вуки - это json
# кейс с именами большие и маленькие буквы.
# выбрать поля, в которых содержатся ссылки
#
