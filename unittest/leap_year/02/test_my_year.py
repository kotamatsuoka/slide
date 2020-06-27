"""
プロダクトコードの中身の実装する
「Red」->「Green」
"""

import pytest


class MyYear:
    def __init__(self, value):
        self.value = value

    def to_string(self):
        return str(self.value)

    def is_leap(self):
        if self.value % 4 == 0:
            return True
        return False


def test_initialize():
    target_year = 2020
    actual = MyYear(target_year).value
    expected = target_year

    assert actual == expected


def test_to_string():
    target_year = 2020
    actual = MyYear(target_year).to_string()
    expected = str(target_year)

    assert actual == expected


@pytest.mark.parametrize("target_year, expected", [
    (2020, True),
    (2019, False),
])
def test_is_leap(target_year, expected):
    actual = MyYear(target_year).is_leap()

    assert actual == expected
