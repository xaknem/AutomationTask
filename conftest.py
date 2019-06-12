import pytest
import json
import requests

# use endpoint with "people" resource because there is no other tests
endpoint: str = "https://swapi.co/api/people/"


@pytest.fixture(scope="module")
def people_list():
    people_list = []
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


@pytest.fixture(scope="module")
def people_schema():
    response = requests.get(endpoint + "schema")
    return json.loads(response.content)


@pytest.fixture(scope="module")
def people_count():
    count = get_page(endpoint)["count"]
    return count


@pytest.fixture
def search_in_peoples():
    def search(what_to_search):
        search_result = get_page(endpoint + "?search=" + what_to_search)["results"]
        return search_result
    return search


def get_page(url):
    response = requests.get(url)
    json_content = json.loads(response.content)
    return json_content
