"""
プロダクトコードを直す
「Red」->「Green」
"""

import pytest


class MyYear:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def is_leap(self):
        if self.value % 4 != 0:
            return False
        if self.value % 100 == 0 and self.value % 400 != 0:
            return False
        return True


def test_initialize():
    target_year = 2020
    actual = MyYear(target_year).value
    expected = target_year

    assert actual == expected


def test_str_magic_method():
    target_year = 2020
    actual = str(MyYear(target_year))
    expected = str(target_year)

    assert actual == expected


@pytest.mark.parametrize("target_year, expected", [
    (2020, True),
    (2019, False),
    (2100, False),
    (2000, True),
])
def test_is_leap(target_year, expected):
    actual = MyYear(target_year).is_leap()

    assert actual == expected
