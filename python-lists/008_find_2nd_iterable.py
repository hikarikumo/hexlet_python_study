'''
Цель данного упражнения — реализовать функцию find_second_index(). 
В этом упражнении вам пригодится функция find_index(), 
которую вы реализовали в прошлом упражнении. 
Напоминаю, эта функция возвращает индекс первого элемента последовательности, 
равного заданному значению. 
Функция find_second_index() же должна возвращать индекс второго подходящего элемента в последовательности. 
Если подходящих элементов в последовательности меньше двух или же последовательность пуста, 
нужно всё так же возвращать None.

>>> find_second_index('b', 'bob')

2

>>> find_second_index('a', 'cat') is None

True

Новую функцию вам следует реализовывать с помощью уже имеющейся find_index(). 
И не забудьте, что итератор сохраняет позицию, 
в которой остановился обход — это знание поможет вам в решении поставленной задачи!
'''
import pytest
from typing import Union


def find_index(
        search_position: Union[str, list, tuple],
        source_data: Union[str, list, tuple]) -> Union[int, None]:
    if source_data:
        for (index, item) in enumerate(source_data):
            if item == search_position:
                return index
    return None


def find_second_index(
        search_position: Union[str, list, tuple],
        source_data: Union[str, list, tuple]) -> Union[int, None]:
    search = iter(source_data)
    first_index = find_index(search_position, search)
    second_index = find_index(search_position, search)
    if second_index is not None:
        return first_index + second_index + 1


@pytest.mark.parametrize(
    ("search_position", "source_data", "index"),
    [
        ('b', 'bob', 2),
        ('c', 'aarococ', 6),
        ('n', 'banana', 4),
        ('n', 'cannon', 3),
        ('a', 'cat', None),
    ],
)
def test_find_second_index(search_position, source_data, index):
    assert find_second_index(search_position, source_data) == index


if __name__ == "__main__":
    print(find_second_index('n', 'cannon'))