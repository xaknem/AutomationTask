from conftest import *


def test_assumption_that_keys_encodes(people_list):
    response = get_page(endpoint + "1" + format_wookiee)
    person = people_list[0]
    assert len(response.values()) == len(person.values())
    for x in person.keys():
        assert x not in response.keys()


def test_digit_values_not_encodes(people_list, people_count):
    person = people_list[0]
    wookiee_person = get_page(endpoint + "1" + format_wookiee)
    digit_values = 0
    values = wookiee_person.values()
    for value in values:
        if not isinstance(value, list) and value.isdigit():
            digit_values += 1
            assert value in person.values()
    # to exclude false positive test passing
    assert digit_values > 0
