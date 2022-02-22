'''
функция collect_indexes(). 
Эта функция должна принимать на вход коллекцию (некий iterator/iterable) и возвращать словарь (или подобная ему коллекция!), 
где ключом будет элемент коллекции, 
а значением для ключа — список индексов коллекции, по которым встречается этот элемент.
>>> d = collect_indexes("hello")
>>> d["h"]
[0]
>>> d["e"]
[1]
>>> d["l"]
[2, 3]
'''
import pytest
from collections import defaultdict
from typing import Union


def collect_indexes(items: Union[str, list, tuple]) -> defaultdict:
    counters = defaultdict(list)
    for index, item in enumerate(items):
        counters[item].append(index)
    return counters


@pytest.mark.parametrize(
    ('input_iterable', 'output_count_dict'),
    ['hello', {'h': [0], 'e': [1], 'l': [2, 3], 'o': [4]}],
)
def test_collect_indexes(input_iterable, output_count_dict):
    assert collect_indexes(input_iterable) == output_count_dict


if __name__ == "__main__":
    d = collect_indexes("hello")
    print(d["l"])
