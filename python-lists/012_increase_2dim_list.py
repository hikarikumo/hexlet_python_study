'''
Python: Увеличение двумерного списка
Реализуйте функцию enlarge(), которая принимает изображение в виде двумерного списка строк
 и увеличивает его в два раза, то есть удваивает каждый символ по горизонтали и вертикали.
>>> def show(image):
...     for line in image:
...         print(line)
...
>>> dot = ['@']
>>> show(enlarge(dot))
@@
@@
>>> frame = [
...     '****',
...     '*  *',
...     '*  *',
...     '****'
... ]
>>> show(frame)
****
*  *
*  *
****
>>> show(enlarge(frame))
********
********
**    **
**    **
**    **
**    **
********
********

'''
import pytest


def enlarge(obj: list) -> list:
    double_dim_list = list()
    for item in obj:
        elements = [elem for elem in item]
        double_line = list()
        for elem in elements:
            double_line.extend([elem, elem])
        row = ''.join(double_line)
        double_dim_list.extend([row, row])
    return double_dim_list


def return_star_space_count(obj: list) -> tuple:
    frame_star_counter = 0
    frame_space_counter = 0
    for item in obj:
        frame_star_counter += item.count('*')
        frame_space_counter += item.count(' ')
    return (frame_star_counter, frame_space_counter)


if __name__ == "__main__":
    frame = [
             '****',
             '*  *',
             '*  *',
             '****'
        ]
    frame_2x = [
        '********',
        '********',
        '**    **'
        '**    **'
        '**    **'
        '**    **'
        '********',
        '********',
    ]
    # frame_star_counter, frame_space_counter = return_star_space_count(frame)
    # print(f'* = {frame_star_counter}, "  =" {frame_space_counter}')
    # frame_star_counter2, frame_space_counter2 = return_star_space_count(frame_2x)
    # print(f'* = {frame_star_counter2}, "  =" {frame_space_counter2}')
    double_dim = enlarge(frame_2x)
    for item in double_dim:
        print(f'{item}')