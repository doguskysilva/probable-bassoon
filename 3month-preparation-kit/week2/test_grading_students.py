from typing import List

import pytest


def grading_students(grades: List[int]) -> List[int]:
    output = []
    multiple = 5

    for grade in grades:
        if grade < 38:
            output.append(grade)
            continue

        diff_multiple_grade = multiple - (grade % 5)

        if diff_multiple_grade < 3:
            output.append(grade + diff_multiple_grade)
        else:
            output.append(grade)

    return output


def round_grade(grade: int) -> int:
    if grade < 38:
        return grade

    next_multiple = 5 - (grade % 5)

    return (grade + next_multiple) if next_multiple < 3 else grade


def grading_students_pythonic(grades: List[int]) -> List[int]:
    return [round_grade(grade) for grade in grades]


@pytest.mark.parametrize(
    "test_input,test_expected",
    [
        ([73, 67, 38, 33], [75, 67, 40, 33]),
    ],
)
def test_grading_students(test_input, test_expected):
    assert grading_students(test_input) == test_expected
    assert grading_students_pythonic(test_input) == test_expected
