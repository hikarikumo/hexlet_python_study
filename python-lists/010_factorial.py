from typing import NoReturn
import pytest
import math

def factorial_my(num: int) -> int:
    result_factorial = 1
    for number in range(1, num + 1):
        result_factorial = result_factorial*number
    return result_factorial


def factorial_alt(num: int) -> int:
    if num == 0:
        return 1
    else:
        return num * factorial_alt(num - 1)


@pytest.mark.parametrize(
    ("input_num", "result_num"),
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
    ]
)
def test_factorial(input_num, result_num):
    assert factorial_my(input_num) == result_num


@pytest.mark.parametrize(
    ("input_num", "result_num"),
    [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
    ]
)
def test_factorial_alt(input_num, result_num):
    assert factorial_alt(input_num) == result_num

@pytest.mark.parametrize(
    ("input_num"),
    [
        (0),
        (1),
        (2),
        (3),
    ]
)
def test_factorial_from_math(input_num):
    assert factorial_my(input_num) == math.factorial(input_num)


@pytest.mark.parametrize(
    ("input_num"),
    [
        (0),
        (1),
        (2),
        (3),
    ]
)
def test_factorial_from_math_alt(input_num):
    assert factorial_alt(input_num) == math.factorial(input_num)
