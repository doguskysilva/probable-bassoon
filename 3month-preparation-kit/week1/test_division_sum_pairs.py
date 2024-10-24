from typing import List

import pytest


def divisible_sum_pairs(size: int, divisor: int, numbers: List[int]) -> int:
    divisible_pairs = 0

    for idx_i in range(size - 1):
        for idx_j in range(idx_i + 1, size):
            sum_pair = numbers[idx_i] + numbers[idx_j]
            if (sum_pair % divisor) == 0:
                divisible_pairs += 1

    return divisible_pairs


@pytest.mark.parametrize(
    "test_input_a,test_input_b,test_input_c,test_expected",
    [(6, 5, [1, 2, 3, 4, 5, 6], 3), (6, 3, [1, 3, 2, 6, 1, 2], 5)],
)
def test_divisible_sum_pairs(test_input_a, test_input_b, test_input_c, test_expected):
    assert (
        divisible_sum_pairs(test_input_a, test_input_b, test_input_c) == test_expected
    )
