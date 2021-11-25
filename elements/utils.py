import json
from pathlib import Path

from hamcrest import assert_that, is_not, equal_to


def get_config():
    path = Path().joinpath("./config.json")
    return json.loads(path.read_text())


def verify_objects_not_equal(object, object2):
    assert_that(object, is_not(object2))


def verify_objects_are_equal(object, object2):
    assert_that(object, equal_to(object2))


def convert_str_to_lst(str):
    return str.split("\n")
