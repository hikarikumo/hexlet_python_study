'''
Треугольник Паскаля — бесконечная таблица биномиальных коэффициентов, имеющая треугольную форму. 
В этом треугольнике на вершине и по бокам стоят единицы. 
Каждое число равно сумме двух расположенных над ним чисел. 
Строки треугольника симметричны относительно вертикальной оси.

0:           1
1:          1 1
2:         1 2 1
3:        1 3 3 1
4:       1 4 6 4 1
5:      1 5 10 10 5 1
6:     1 6 15 20 15 6 1

Напишите функцию triangle(), которая возвращает указанную строку треугольника Паскаля в виде списка.
Пример:
>>> triangle(0)
[1]
>>> triangle(4)
[1, 4, 6, 4, 1]
'''
from numpy import number
import pytest


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


def triangle(num: int) -> list:
    result_list = list()
    result_list.append(1)
    for item in range(1, num + 1):
        result_list.append(int(
            factorial_alt(num)/(
                factorial_alt(item)*factorial_alt(num - item))))
    return result_list


@pytest.mark.parametrize(
    ("initial_num", "result_num_list"),
    [
        (0, [1]),
        (1, [1, 1]),
        (2, [1, 2, 1]),
        (3, [1, 3, 3, 1]),
        (4, [1, 4, 6, 4, 1]),
    ]
)
def test_triangel(initial_num, result_num_list):
    assert triangle(initial_num) == result_num_list


if __name__ == "__main__":
    print(triangle(6))