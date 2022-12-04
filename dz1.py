import re
from random import *

# sales = {
#     'John':  {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694},
#     'Tom':   {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612},
#     'Anne':  {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859},
#     'Fiona': {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}
# }
#
# for i in sales:
#     print(i, sep="")
#     for a in sales[i]:
#         print(a, " : ", sales[i][a], sep="")
#
# while True:
#     n = input("Имя: ")
#     for i in sales:
#         if n == i:
#             cnt = input("Регион: ")
#             for a in sales[i]:
#                 if cnt == a:
#                     print(sales[i][a])
#                     new = int(input("Новое значение: "))
#                     sales[i][a] = new
#             print(sales[i])
#             break
#     else:
#         print("Нет такого имени в списке")
#     break


# 1 задание
# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
# d = a | b | c
# print(d)
# print({**a, **b, **c})

# 2 задание
# emp = {
#     'emp1':  {'name': 'Jhon', 'salary': 7500},
#     'emp2':  {'name': 'Emma', 'salary': 8000},
#     'emp3':  {'name': 'Brad', 'salary': 6500},
# }
#
# for i in emp:
#     print(i, sep="")
#     for a in emp[i]:
#         if i == 'emp3':
#             emp[i]['salary'] = 8500
#             print(a, " : ", emp[i][a], sep="")


# 3 задание

# n = int(input("Введите количество студентов: "))
# a = {}
# sum1 = 0
# for i in range(n):
#     name = input(str(i + 1) + "-й студент: ")
#     p = int(input("Бал: "))
#     a[name] = p
#     sum1 += p
#
# sred = sum1 / n
# print("Средний балл: ", round(sred, 1))
# print("Студент с баллом выше среднего: ")
# for i in a:
#     if a[i] > sred:
#         print(i)

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
# import math
#
#
# def square(figure_type, **kwargs):
#     if figure_type == 'rhombus':
#         s = (kwargs['d1'] * kwargs['d2']) / 2
#         return s
#     elif figure_type == 'square':
#         s = kwargs['a'] ** 2
#         return s
#     elif figure_type == 'trapezoid':
#         s = 1/2 * (kwargs['a'] + kwargs['b']) * kwargs['h']
#         return s
#     elif figure_type == 'circle':
#         s = math.pi * kwargs['r'] ** 2
#         return s
#     else:
#         return 'invalid data'
#
#
# print(square(figure_type='rhombus', d1=10, d2=8))
# print(square(figure_type='square', a=5))
# print(square(figure_type='trapezoid', a=12, b=3, h=6))
# print(square(figure_type='circle', r=18))
# print(square(figure_type='unknown', a=1, b=2, c=3))

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
# @func1
# def func3():
#
#     print()


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
# s = 0
#
#
# def func1(a, b, c):
#     def func2(x, y):
#         global s
#         s = x * y
#         return s
#
#     return 2 * (func2(a, b) + func2(b, c) + func2(a, c))
#
#
# print(func1(2, 4, 6))
# print(func1(5, 8, 2))
# print(func1(1, 6, 8))


# 1 задание
# print((lambda a: (lambda b: (lambda c: a * b * c)))(2)(5)(5))


# 2 задание
# students = [{'name': 'Jennifer', 'final': 95},
#             {'name': 'David', 'final': 92},
#             {'name': 'Nikolas', 'final': 98}
#             ]
# res1 = sorted(students, key=lambda item: item['name'])
# print(res1)
# res2 = sorted(students, key=lambda item: item['final'], reverse=True)
# print(res2)

# 3 задание
# students = [{'name': 'Jennifer', 'final': 95},
#             {'name': 'David', 'final': 92},
#             {'name': 'Nikolas', 'final': 98}
#             ]
#
# res1 = max(students, key=lambda item: item['name'])
# print(res1)
# res2 = min(students, key=lambda item: item['final'])
# print(res2)

# 4 задание
# nums = [3, 5, 7, 3, 9, 5, 7, 2]
# print(nums)
# res1 = (lambda i: i ** 2)
# res2 = (lambda i: i ** 3)
# print(list(map(res1, nums)))
# print(list(map(res2, nums)))


# def func1(fn):
#     def wrap(arg1, arg2, arg3, arg4):
#         s = (arg1 + arg2 + arg3 + arg4) / 4
#         fn(arg1, arg2, arg3, arg4)
#         print("Среднее арифметическое чисел ", arg1, ", ", arg2, ", ", arg3, ", ", arg4, " = ",  s, sep="")
#
#     return wrap
#
#
# @func1
# def func2(a, b, c, d):
#     sum1 = a + b + c + d
#     print("Сумма чисел ", a, ", ", b, ", ", c, ", ", d, " = ", sum1, sep="")
#
#
# func2(2, 3, 3, 4)

# def func1(fn):
#     def wrap(*args):
#         a = ''
#         for i in args:
#             a += str(i) + ", "
#         print("Среднее арифметическое чисел ", a[:-2], " = ",  fn(*args) / len(args))
#
#     return wrap
#
#
# @func1
# def func2(*ar):
#     a = ''
#     for i in ar:
#         a += str(i) + ", "
#     print("Сумма чисел ", a[:-2], " = ", sum(ar), sep=" ")
#     return sum(ar)
#
#
# func2(2, 3, 3, 4)


# a = int(input("-> "))
# print(bin(a))
#
# a = int(input("-> "))
# print(bin(a))
#
# a = int(input("-> "))
# print(bin(a))

# def func():
#     pass


# while True:
#     a = int(input("-> "))
#     if a != 0:
#         b = str(bin(a))
#         print(b[2:])
#     else:
#         break

# 1 задание
# a = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
# print(a[a.find("("):a.find(")") + 1])

# 2 задание
# str1 = input("Введите строку: ")
# str2 = input("Ее заменяемая строка: ")
# str3 = input("Новая подстрока: ")
# i = str1.find(str2)
# while i != -1:
#     l = len(str2)
#     str1 = str1[0:i] + str3 + str1[i + l:]
#     i = str1.find(str2)
# print(str1)

# 3 задание
# test = "Ежевика для ежат\n" \
#        "Принесли два ежа\n" \
#        "Ежевику еле-еле\n" \
#        "Ежата возле ели съели."
# print(test)
# print(test.count("е"))

# a = 'Замените в этой строке все появившиеся буквы "о" на букву "О", кроме первого и последнего вхождения.'
# print(a)
# print(a.replace("о", "О", a.count("о")-1).replace("О", "о", 1))


# def login(a):
#     return re.findall(r'^[A-z0-9_@-]{6,18}$', password)
#
#
# password = input("Задайте пароль: ")
# print(login(password))

s1 = input("Введите дату в формате dd-mm-YYYY: ")
reg = r'([0-2][0-9]|[3][0-1])-([0][0-9]|[1][0-2])-(\d{4})'
print(re.findall(reg, s1))

# Я не знаю как избавится от круглых скобок




