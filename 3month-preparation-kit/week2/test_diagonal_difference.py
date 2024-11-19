from timeit import timeit
from typing import List
import pytest
import random


def diagonal_difference(arr: List[List[int]]) -> int:
    size = len(arr)
    left_right_diagonal, right_left_diagonal = 0, 0

    for i in range(size):
        left_right_diagonal += arr[i][i]
        right_left_diagonal += arr[size - i - 1][i]

    return abs(left_right_diagonal - right_left_diagonal)


def diagonal_difference_pythonic(matrix):
    size = len(matrix)
    
    primary_diagonal = sum(matrix[i][i] for i in range(size))
    secondary_diagonal = sum(matrix[i][size - 1 - i] for i in range(size))
    
    return abs(primary_diagonal - secondary_diagonal)

def compare_performance(matrix_size = 100, iterations = 1000):
    
    # create test matrix
    matrix = [[random.randint(-100, 100) for _ in range(matrix_size)] 
              for _ in range(matrix_size)]

    original_time = timeit(
        lambda: diagonal_difference(matrix),
        number=iterations
    )

    pythonic_time = timeit(
        lambda: diagonal_difference_pythonic(matrix),
        number=iterations
    )

    print(f"\nPerformance comparison with {matrix_size}x{matrix_size} matrix over {iterations} iterations:")
    print(f"Original solution:     {original_time:.4f} seconds")
    print(f"Pythonic solution:     {pythonic_time:.4f} seconds")

    fastest_time = min(original_time, pythonic_time)
    print("\nRelative performance (lower is better):")
    print(f"Original solution:     {original_time/fastest_time:.2f}x")
    print(f"Pythonic solution:     {pythonic_time/fastest_time:.2f}x")
    print("\n")


@pytest.mark.parametrize(
    "test_input,test_expected",
    [
        ([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15),
        ([[6, 8], [-6, 9]], 13)
    ],
)
def test_diagonal_difference(test_input, test_expected):
    assert diagonal_difference(test_input) == test_expected
    assert diagonal_difference_pythonic(test_input) == test_expected


if __name__ == "__main__":    
    for size in [10, 100, 1000, 10000]:
        compare_performance(matrix_size=size, iterations=10000 if size < 1000 else 100)

