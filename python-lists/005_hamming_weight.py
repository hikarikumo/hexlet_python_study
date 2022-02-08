'''
Вес Хэмминга это количество единиц в двоичном представлении числа.
solution.py

Реализуйте функцию hamming_weight, которая считает вес Хэмминга.
'''
import pytest


def hamming_weight(num: int) -> int:
    bin_num = bin(num)[2::]
    num_of_ones = 0
    for item in bin_num:
        num_of_ones += int(item)
    return num_of_ones


# def hamming_weight(number):
#         return bin(number).count('1')


@pytest.mark.parametrize(
    ("input_number", "result_number"),
    [
        (0, 0),
        (4, 1),
        (101, 4),
    ],
)

def test_hamming_weight_01(input_number, result_number):
    assert hamming_weight(input_number) == result_number

