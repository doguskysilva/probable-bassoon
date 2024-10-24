from typing import List

import pytest


def sparse_arrays(strings: List[str], queries: List[str]) -> List[int]:
    count_queries = [0 for _ in queries]

    for idx, query in enumerate(queries):
        for text in strings:
            if query == text:
                count_queries[idx] += 1

    return count_queries


@pytest.mark.parametrize(
    "test_input_a,test_input_b,test_expected",
    [
        (["ab", "ab", "abc"], ["ab", "abc", "bc"], [2, 1, 0]),
    ],
)
def test_sparse_arrays(test_input_a, test_input_b, test_expected):
    assert sparse_arrays(test_input_a, test_input_b) == test_expected
