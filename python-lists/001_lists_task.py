'''
src/solution.py

Для успешного прохождения этой практики вам нужно будет реализовать две функции:

    get_square_roots_roots()
    get_range()

Функция get_square_roots_roots() должна принимать число и возвращать список квадратных корней этого числа. Например для аргумента 9 функция должна вернуть [-3, 3]. Тест ожидает, что сначала в списке будет идти отрицательный корень, если таковой имеется. Также корень может быть и один, если аргумент равен нулю. А ещё корней может и не быть, если аргумент отрицательный.

>>> get_square_roots_roots(25)

[-5.0, 5.0]

    Для решения используйте функцию sqrt() из модуля math (модуль нужно будет импортировать).

get_range() должна для заданного положительного числа аргумента n возвращать список чисел от нуля до n, не включая само число n. Если при вызове было передано отрицательное число или ноль, функция должна возвращать пустой список.

>>> get_range(5)

[0, 1, 2, 3, 4]

    Для решения используйте цикл while и метод списка append.
'''
import math, pytest


def get_square_roots(sqrt_number):
    """Функция get_square_roots_roots() должна принимать число и возвращать список квадратных корней этого числа. 
    Например для аргумента 9 функция должна вернуть [-3, 3]. 
    Тест ожидает, что сначала в списке будет идти отрицательный корень, если таковой имеется. 
    Также корень может быть и один, если аргумент равен нулю. А ещё корней может и не быть, если аргумент отрицательный.
        >>> get_square_roots_roots(25)
        [-5.0, 5.0]

    Args:
        sqrt_number ([int]): [изначальный квадрат числа]

    Returns:
        [int]: [число]
    """
    list_of_results = list()
    if sqrt_number < 0:
        return list_of_results
    elif sqrt_number > 0:
        root_value = math.sqrt(sqrt_number)
        return [-root_value, root_value]
    return [0]

def test_get_square_roots_general():
    sqrt_number = 25
    assert get_square_roots(sqrt_number) == [-5.0, 5.0]


def test_get_square_roots_zero():
    sqrt_number = 0
    assert get_square_roots(sqrt_number) == [0]


def test_get_square_roots_negative():
    sqrt_number = -25
    assert get_square_roots(sqrt_number) == []


def get_range(some_number):
    result_list = list()
    index = 0 
    while index < some_number:
        result_list.append(index)
        index += 1
    return result_list


def test_get_range_general():
    results_list = [0, 1, 2, 3, 4, 5]
    some_number = 6
    assert get_range(some_number) == results_list


def test_get_range_zero():
    results_list = list()
    some_number = 0
    assert get_range(some_number) == results_list


def test_get_range_negative():
    results_list = list()
    some_number = -5
    assert get_range(some_number) == results_list
