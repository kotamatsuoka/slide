"""
設計のレビューをしてもらえるように、関数の呼び出し方と、テストケースのみを書いてみる
テストは「Red」の状態でも良い

【閏年問題】
以下、3つのメソッドを持つMyYearクラスの実装について考える

1. 整数の引数を持ち、その引数を保持する
2. 保持した値を文字列として返す
3. 保持した値が閏年ならばtrueを返し、それ以外はfalseを返す
"""

import pytest


class MyYear:
    def __init__(self):
        pass

    def to_string(self):
        pass

    def is_leap(self):
        pass


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
