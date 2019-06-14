from conftest import *


def test_assumption_keys_encodes(people_list):
    response = get_page(endpoint + "1" + format_wookiee)
    assert len(response.values()) == len(people_list[0].values())
    for x in people_list[0].keys():
        assert x not in response.keys()


def test_number_values_not_encodes(people_list, people_count):
    response = get_page(endpoint + str(people_count) + format_wookiee)
    person = people_list[1]
    for parameter in response.keys():
        field = response[parameter]
        if type(field) == "string":
            if field.isdigit():
                assert field in person.values()
