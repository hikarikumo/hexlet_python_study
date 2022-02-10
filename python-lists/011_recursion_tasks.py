'''
A: От 1 до n
Дано натуральное число n. Выведите все числа от 1 до n.
Ввод 	Вывод

5       1 2 3 4 5

В задачах этого листка нельзя использовать циклы и массивы.
'''
from typing import NoReturn
import pytest


def all_naturals(initial: int, max: int) -> NoReturn:
    if initial < max:
        print(initial)
        initial += 1
        all_naturals(initial, max)
    elif initial == max:
        print(initial)


@pytest.mark.parametrize(
    ("initial", "input", "result"),
    [
        (1, 5, [1, 2, 3, 4, 5])
    ]
)
def test_all_naturals(initial, input, result):
    assert all_naturals(initial, input) == result


if __name__ == "__main__":
    all_naturals(1,5)