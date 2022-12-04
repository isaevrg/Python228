from random import *

# 1 задание
# def proiz(*a):
#     res = 1
#     for i in a:
#         res *= i
#     return res
#
#
# print(proiz(10, 9))
# print(proiz(2, 3, 4))
# print(proiz(3, 5, 10, 6))

# 2 задание

# def func(*a):
#     z = 0
#     for i in a:
#         z += i
#         print(z, end=" ")
#     print()
#
#
# func(3, 9, 1)
# func(2, 5, 4, 2)
# func(3, 5, 10, 6, 3)

# 3 задание
import math


def square(figure_type, **kwargs):
    if figure_type == 'rhombus':
        s = (kwargs['d1'] * kwargs['d2']) / 2
        return s
    elif figure_type == 'square':
        s = kwargs['a'] ** 2
        return s
    elif figure_type == 'trapezoid':
        s = 1/2 * (kwargs['a'] + kwargs['b']) * kwargs['h']
        return s
    elif figure_type == 'circle':
        s = math.pi * kwargs['r'] ** 2
        return s
    else:
        return 'invalid data'


print(square(figure_type='rhombus', d1=10, d2=8))
print(square(figure_type='square', a=5))
print(square(figure_type='trapezoid', a=12, b=3, h=6))
print(square(figure_type='circle', r=18))
print(square(figure_type='unknown', a=1, b=2, c=3))















