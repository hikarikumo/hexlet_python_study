'''
chunk.py

Реализуйте функцию chunked, которая принимает на вход число и последовательность. 
Число задает размер чанка (куска). 
Функция должна вернуть список, состоящий из чанков указанной размерности. 
При этом список должен делиться на куски-списки, строка — на строки, кортеж — на кортежи!

>>> chunked(2, ['a', 'b', 'c', 'd'])

[['a', 'b'], ['c', 'd']]

>>> chunked(3, ['a', 'b', 'c', 'd'])

[['a', 'b', 'c'], ['d']]

>>> chunked(3, 'foobar')

['foo', 'bar']

>>> chunked(10, (42,))

[(42,)]
'''
import pytest
from typing import Union


# def chunked(chunk_num: int, sequence: Union[list, tuple, str]) -> Union[list, tuple, str]:
#     new_sequence = list()
#     if not sequence[:chunk_num]:
#         new_sequence = []
#     elif sequence[chunk_num:]:
#         if len(sequence[:chunk_num]) < len(sequence[chunk_num:]):
#             new_sequence.append(sequence[:chunk_num])
#             new_sequence.extend(chunked(chunk_num, sequence[chunk_num:]))
#         else:
#             new_sequence.append(sequence[:chunk_num])
#             new_sequence.append(sequence[chunk_num:])

#     else:
#         new_sequence = [sequence[:chunk_num]]
#     return new_sequence

# golden solution
def chunked(size, source):
    result = []
    index = 0
    while index < len(source):
        result.append(source[index:index + size])
        index += size
    return result



@pytest.mark.parametrize(
    ('chunk_number', 'input_sequence', 'result'),
    [
        (2, ['a', 'b', 'c', 'd'], [['a', 'b'], ['c', 'd']]),
        (3, ['a', 'b', 'c', 'd'], [['a', 'b', 'c'], ['d']]),
        (3, 'foobar', ['foo', 'bar']),
        (10, (42,), [(42,)]),
        (2, ['a', 'b', 'c', 'd'], [['a', 'b'], ['c', 'd']]),
        (3, ['e', 'f', 'h', 'i'], [['e', 'f', 'h'], ['i']]),
        (4, ['g', 'k', 'l', 'm'], [['g', 'k', 'l', 'm']]),
        (4, [], []),
        (2, ['n'], [['n']]),
        (2, ['a', 'b', 'c', 'd', 'e', 'f'], [['a', 'b'], ['c', 'd'], ['e', 'f']]),
    ]
)
def test_chunked(chunk_number, input_sequence, result):
    assert chunked(chunk_number, input_sequence) == result

if __name__ == "__main__":
    print(chunked(2, ['a', 'b', 'c', 'd']))
    print(chunked(2, 'foobar'))
    print(chunked(10, (42,)))
    print(chunked(2, (42,43,45,56,44,25,55,22)))
