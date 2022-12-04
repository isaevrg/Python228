from random import *

# 1 задание

# def func1(a):
#     def func2(b):
#         return a * b
#     return func2
#
#
# res1 = func1(2)
# print(res1(15))
# print(res1(20))
# res2 = func1(3)
# print(res2(15))
# print(res2(20))

# 2 задание - Вариант 1
# def func1(a, b, c):
#     def func2(x, y):
#         s = x * y
#         return s
#
#     return 2 * (func2(a, b) + func2(b, c) + func2(a, c))
#
#
# print(func1(2, 4, 6))
# print(func1(5, 8, 2))
# print(func1(1, 6, 8))


# 2 задание - Вариант 2


# def func1(a, b, c):
#     s = 0
#
#     def func2(x, y):
#         nonlocal s
#         s = x * y
#         return s
#
#     return 2 * (func2(a, b) + func2(b, c) + func2(a, c))
#
#
# print(func1(2, 4, 6))
# print(func1(5, 8, 2))
# print(func1(1, 6, 8))


# 2 задание - Вариант 3
s = 0


def func1(a, b, c):
    def func2(x, y):
        global s
        s = x * y
        return s

    return 2 * (func2(a, b) + func2(b, c) + func2(a, c))


print(func1(2, 4, 6))
print(func1(5, 8, 2))
print(func1(1, 6, 8))





