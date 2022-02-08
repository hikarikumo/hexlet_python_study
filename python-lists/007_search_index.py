'''
 этом упражнении вы будете реализовывать классический цикл поиска. 
 Функция find_index(), которую вам предстоит написать, 
 должна принимать значение и нечто, по чему можно итерироваться — строку, список, кортеж. 
 В ответ функция должна вернуть индекс первого элемента итерируемой последовательности, равного заданному значению. 
 Если же значение в последовательности не встречается или же последовательность окажется пустой, 
 функция должна вернуть None.

>>> find_index('t', 'cat')

2

>>> find_index(5, [1, 2, 3, 4, 5, 6, 7])

4

>>> find_index(42, []) is None

True

>>> find_index('!', 'abc') is None

True

    При выполнении воспользуйтесь циклом for и функцией enumerate().
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


@pytest.mark.parametrize(
    ("search_position", "source_data", "index"),
    [
        ('t', 'cat', 2),
        ('b', 'bob', 0),
        ('c', 'aarococ', 4),
        (5, [1, 2, 3, 4, 5, 6, 7], 4),
        (42, [], None),
        ('!', 'abc', None),
    ],
)
def test_find_index(search_position, source_data, index):
    assert find_index(search_position, source_data) == index


if __name__ == "__main__":
    print(find_index('t', 'cat'))
