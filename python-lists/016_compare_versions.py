'''
Реализуйте функцию compare_version(), которая сравнивает переданные версии version1 и version2. 
Если version1 > version2, то функция должна вернуть 1, 
если version1 < version2, то -1, 
если же version1 = version2 — 0.

Версия — это строка, 
в которой два числа (мажорная и минорные версии) разделены точкой, например: 12.11. 
Важно понимать, что версия — это не число с плавающей точкой, а несколько чисел не связанных между собой. 
Проверка на больше/меньше производится сравнением каждого числа независимо. 
Поэтому версия 0.12 больше версии 0.2.
Пример порядка версий:

0.1 < 1.1 < 1.2 < 1.11 < 13.37

>>> compare_version("0.1", "0.2")
-1
>>> compare_version("0.2", "0.1")
1
>>> compare_version("4.2", "4.2")
0

Подробнее о версиях: http://semver.org/lang/ru/
Подсказки

Разобрать строку на части, разделённые некоторой подстрокой, можно так:

>>> 'foo::bar::baz'.split('::')
['foo', 'bar', 'baz']

'''
import pytest


def compare_version(version1: str, version2: str) -> int:
    major_ver1, minor_ver1 = version1.split('.')
    major_ver2, minor_ver2 = version2.split('.')
    if int(major_ver1) == int(major_ver2):
        if (int(minor_ver1) - int(minor_ver2)) < 0:
            return -1
        elif (int(minor_ver1) - int(minor_ver2)) > 0:
            return 1
        elif int(minor_ver1) == int(minor_ver2):
            return 0
    elif int(major_ver1) - int(major_ver2) < 0:
        return -1
    elif int(major_ver1) - int(major_ver2) > 0:
        return 1

#golden 


def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0


def compare_version(first, second):
    [a1, b1] = first.split('.')
    [a2, b2] = second.split('.')

    major = sign(int(a1) - int(a2))
    minor = sign(int(b1) - int(b2))

    return major if major != 0 else minor
    

@pytest.mark.parametrize(
    ('version1', 'version2', 'result'),
    [
        ("0.1", "0.2", -1),
        ("0.2", "0.1", 1),
        ("4.2", "4.2", 0),
        ('3.2', '4.12', -1),
    ]
)
def test_compare_version(version1, version2, result):
    assert compare_version(version1, version2) == result

if __name__ == "__main__":
    print(compare_version('3.2', '4.12'))
