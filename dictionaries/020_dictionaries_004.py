'''
функцию all_unique(), которая должна принимать итератор (в т.ч. и те, которые не перезапускаемые!) и возвращать True,
 если элементы в итераторе не повторяются (если элементов нет, то ничего не повторяется!)

>>> all_unique([])
True
>>> all_unique("cat")
True
>>> all_unique([1, 2, 3])
True
>>> all_unique([1, 2, 1])
False
'''
import pytest
from typing import Union

def all_unique(iterator: Union[list, str, tuple]) -> bool:
    length = list(iterator)
    if len(length) != len(set(length)):
        return False
    return True

# golden


def all_unique(iterable):
    items = list(iterable)
    return len(items) == len(set(items))
