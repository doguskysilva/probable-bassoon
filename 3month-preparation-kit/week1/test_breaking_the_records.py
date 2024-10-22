import pytest


def breaking_records(scores):
    most_least_scores = [0, 0]

    min_score = scores[0]
    max_score = scores[0]

    for score in scores:
        if score > max_score:
            max_score = score
            most_least_scores[0] += 1
        if score < min_score:
            min_score = score
            most_least_scores[1] += 1

    return most_least_scores


@pytest.mark.parametrize(
    "test_input,test_expected",
    [
        ([12, 24, 10, 24], [1, 1]),
        ([3, 4, 21, 36, 10, 28, 35, 5, 24, 42], [4, 0]),
        ([10, 5, 20, 20, 4, 5, 2, 25, 1], [2, 4])
    ],
)
def test_breaking_records(test_input, test_expected):
    assert breaking_records(test_input) == test_expected
