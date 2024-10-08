import pytest

def plus_minus(arr):
    less_zero = 0
    greather_zero = 0
    equal_zero = 0
    size_arr = len(arr)

    for i in arr:
        if i < 0:
            less_zero += 1
        elif i > 0:
            greather_zero += 1
        else:
            equal_zero += 1

    return [round(greather_zero / size_arr, 6), 
            round(less_zero / size_arr, 6), 
            round(equal_zero / size_arr, 6)]

@pytest.mark.parametrize(
    "test_input,test_expected",
    [
        ([1, 1, 0, -1, -1], [0.400000, 0.400000, 0.200000]),
        ([-4, 3, -9, 0, 4, 1], [0.500000, 0.333333, 0.166667])
    ]
)
def test_plus_minus(test_input, test_expected):
    assert plus_minus(test_input) == test_expected

