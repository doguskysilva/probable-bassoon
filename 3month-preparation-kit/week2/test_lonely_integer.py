from typing import List

import pytest


def lonely_integer(arr: List[int]):
    lonely = 0

    for i in set(arr):
        if arr.count(i) == 1:
            lonely = i
            break

    return lonely


def lonely_integer_pythonic(arr: List[int]) -> int:
    return next(i for i in arr if arr.count(i) == 1)


@pytest.mark.parametrize(
    "test_input,test_expected",
    [
        ([1, 2, 3, 4, 3, 2, 1], 4),
    ],
)
def test_lonely_integer(test_input, test_expected):
    assert lonely_integer(test_input) == test_expected
    assert lonely_integer_pythonic(test_input) == test_expected
