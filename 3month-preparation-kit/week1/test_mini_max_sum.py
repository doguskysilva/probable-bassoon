import pytest


def mini_max_sum(arr):
    sorted_arr = sorted(arr)
    return [sum(sorted_arr[:-1], start=0), sum(sorted_arr[1:], start=0)]


@pytest.mark.parametrize(
    "test_input,test_expected",
    [([1, 3, 5, 7, 9], [16, 24]), ([1, 2, 3, 4, 5], [10, 14])],
)
def test_mini_max_sum(test_input, test_expected):
    assert mini_max_sum(test_input) == test_expected
