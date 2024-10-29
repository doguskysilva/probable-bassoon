import pytest


def convert_decimanl_binary(n: int) -> str:
    if n == 0:
        return "0"

    binary = []
    tmp = abs(n)

    while tmp:
        binary.append(str(tmp % 2))
        tmp //= 2

    return "".join(binary[::-1])


def convert_binary_decimal(binary_str: str) -> int:
    decimal = 0

    for digit in binary_str:
        decimal = (decimal << 1) | int(digit)

    return decimal


def flip_bit(bit: str) -> str:
    return "0" if bit == "1" else "1"


def flipping_bits(n: int) -> int:
    fully_binary = convert_decimanl_binary(n).zfill(32)
    flipped_binary = "".join([flip_bit(bit) for bit in fully_binary])

    return convert_binary_decimal(flipped_binary)


def flipping_bits_pythonic(n: int) -> int:
    binary_str = bin(n)[2:].zfill(32)
    flipped_binary_str = "".join([flip_bit(bit) for bit in binary_str])
    return int(flipped_binary_str, 2)

    return 1


@pytest.mark.parametrize(
    "test_input,test_expected",
    [(9, "1001"), (32, "100000")],
)
def test_convert_decimnal_binary(test_input, test_expected):
    assert convert_decimanl_binary(test_input) == test_expected


@pytest.mark.parametrize(
    "test_input,test_expected",
    [(9, 4294967286), (2147483647, 2147483648), (1, 4294967294), (0, 4294967295)],
)
def test_flipping_bits(test_input, test_expected):
    assert flipping_bits(test_input) == test_expected
    assert flipping_bits_pythonic(test_input) == test_expected
