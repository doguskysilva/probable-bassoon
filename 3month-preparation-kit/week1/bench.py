import timeit
from typing import List
from collections import Counter

# Original version
def original_plus_minus(arr: List[int]) -> List[float]:
    less_zero = greather_zero = equal_zero = 0
    size_arr = len(arr)
    for i in arr:
        if i < 0:
            less_zero += 1
        elif i > 0:
            greather_zero += 1
        else:
            equal_zero += 1
    return [
        round(greather_zero / size_arr, 6),
        round(less_zero / size_arr, 6),
        round(equal_zero / size_arr, 6)
    ]

# Counter version
def counter_plus_minus(numbers: List[int]) -> List[float]:
    size = len(numbers)
    counts = Counter(1 if x > 0 else -1 if x < 0 else 0 for x in numbers)
    return [
        round(counts[1] / size, 6),
        round(counts[-1] / size, 6),
        round(counts[0] / size, 6)
    ]

# Test with larger array
test_arr = [-1, 2, 0, 3, -5, 0, 7, -3, 0] * 10000

# Benchmark
print("Original:", timeit.timeit(lambda: original_plus_minus(test_arr), number=1000))
print("Counter:", timeit.timeit(lambda: counter_plus_minus(test_arr), number=1000))
