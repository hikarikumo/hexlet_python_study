'''
функция count_all(). 
Эта функция должна принимать на вход iterable источник и возвращать словарь, 
ключами которого являются элементы источника, 
а значения отражают количество повторов элемента в коллекции-источнике.
>>> count_all(["cat", "dog", "cat"])
{"cat": 2, "dog": 1}
>>> count_all("hello")
{'h': 1, 'e': 1, 'l': 2, 'o': 1}
>>> count_all("*" * 20)
{'*': 20}
'''
import pytest
from typing import Union

def count_all(source: Union[list, str, tuple]) -> dict:
    elem_count_dict = dict()
    for elem in source:
        if elem in elem_count_dict:
            elem_count_dict.update({elem: elem_count_dict.get(elem) + 1 })
        else:
            elem_count_dict.update({elem: 1})
    return elem_count_dict

# golden solution


def count_all(items):
    counters = {}
    for item in items:
        counters[item] = counters.get(item, 0) + 1
    return counters
    

@pytest.mark.parametrize(
    ('input_iterable', 'output_dictionary'),
    [
        (["cat", "dog", "cat"], {"cat": 2, "dog": 1}),
        ("hello", {'h': 1, 'e': 1, 'l': 2, 'o': 1}),
        ("*" * 20, {'*': 20}),
    ]
)
def test_count_all(input_iterable, output_dictionary):
    assert count_all(input_iterable) == output_dictionary