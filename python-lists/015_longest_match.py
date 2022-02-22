'''
Реализуйте функцию find_longest_length(), 
принимающую на вход строку и возвращающую длину максимальной последовательности из неповторяющихся символов. 
Подстрока может состоять из одного символа. Например в строке qweqrty, можно выделить следующие подстроки: qwe, weqrty. 
Самой длинной будет weqrty, а её длина — 6 символов.
'''
import pytest


# def find_duplicates(elements: list) -> list:
#     duplicates = list()
#     elements_list = list(elements)
#     for index, elem in enumerate(elements_list):
#         copied_list = elements_list[:]
#         copied_list.remove(elem)
#         if elem in copied_list:
#             duplicates.append((index, elem))
#     return duplicates


# def find_longest_length(elements: str) -> int:
#     duplicates_with_index = find_duplicates(elements)
#     result = list()
#     if elements == '':
#         return 0
#     elif len(elements) == 1:
#         return 1
#     elif not duplicates_with_index:
#         return len(elements)
#     elif len(duplicates_with_index) == 2:
#         for index_dup, dup in duplicates_with_index:
#             tmp_result = elements[:index_dup + 1]
#             if len(set(tmp_result)) == len(tmp_result):
#                 result.append(tmp_result)
#             tmp_result2 = elements[index_dup + 1:]
#             if len(set(tmp_result2)) == len(tmp_result2):
#                 result.append(tmp_result2)
#         return max([len(item) for item in result])
#     elif len(duplicates_with_index) > 2:
#         duplicate_idx = [item[0] for item in duplicates_with_index]
#         for index, elem in enumerate(elements):
#             for idx_dup in duplicate_idx:    
#                 tmp_result = elements[idx_dup:index + 1]
#                 if len(set(tmp_result)) == len(tmp_result):
#                     result.append(tmp_result)
#                 tmp_result2 = elements[index + 1:idx_dup]
#                 if len(set(tmp_result2)) == len(tmp_result2):
#                     result.append(tmp_result2)
#         return max([len(item) for item in result])

#golden solution


def unique_sequence_length(string):
    unique_sequence = set()
    length = 0
    for char in string:
        if char in unique_sequence:
            break
        unique_sequence.add(char)
        length += 1
    return length


def find_longest_length(string):
    longest_length = 0
    for i, _ in enumerate(string):
        substring_length = unique_sequence_length(string[i:])
        if longest_length < substring_length:
            longest_length = substring_length
    return longest_length



@pytest.mark.parametrize(
    ('seq', 'unique_items_len'),
    [
        ('abcdeef', 5),
        ('jabjcdel', 7),
        ('abcddef', 4),
        ('abbccddeffg', 3),
        ('abcd', 4),
        ('1234561qweqwer', 9),
    ]
)
def test_find_longest_length(seq, unique_items_len):
    assert find_longest_length(seq) == unique_items_len


if __name__ == "__main__":
    print(find_longest_length('abcdeefqws'))
    print(find_longest_length('jabjcdel'))
    print(find_longest_length('abcddef'))
    print(find_longest_length('abbccddeffg'))
    print(find_longest_length('1234561qweqwer'))
