'''
Реализуйте функцию is_continuous_sequence(), которая проверяет, 
является ли переданная последовательность целых чисел возрастающей непрерывно 
(не имеющей пропусков чисел). 
Например, последовательность [4, 5, 6, 7] — непрерывная, а [0, 1, 3] — нет. 
Последовательность может начинаться с любого числа. 
Главное условие — отсутствие пропусков чисел. 
Последовательность из одного числа не может считаться возрастающей.
'''
import pytest

def is_continuous_sequence(sequence: list) -> bool:
    if len(sequence) >= 2:
        new_seq = [item for item in range(sequence[0], sequence[-1] + 1)]
        if new_seq == sequence:
            return True
    return False

# решение учителя

# def is_continuous_sequence(source):
#     if len(source) < 2:
#         return False
#     for x, y in zip(source, source[1:]):
#         if (y - x) != 1:
#             return False
#     return True


@pytest.mark.parametrize(
    ('sequence', 'check_value'),
    [
        ([10, 11, 12, 13], True),
        ([-5, -4, -3], True),
        ([10, 11, 12, 14, 15], False),
        ([1, 2, 2, 3], False),
        ([7], False),
        ([],False),
    ]
)
def test_is_continuous_sequence(sequence, check_value):
    assert is_continuous_sequence(sequence) == check_value