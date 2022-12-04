# name = "Roman"
# print("Hello,", name)
# age = 20
# print(age)
# print(type(name))
# print(type(age))
# a = 4
# b = 5
# a = b
# print(id(a))
# print(id(b))  # id
import ast
# a = b = c = 1
# print(a, b, c)
# print(id(a))
# print(id(b))
# print(id(c))

# a, b, c = 5, "Hello", 9.2
# print(a, b, c)

# name_name = "Bob"
# print(name_name)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = "Hello"
# print(type(a))
# a = 3
# print(type(a))

# name = "Roman"
# age = 20
#
# print("Меня зовут: " + name + ". Мне " + str(age) + " лет")

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
# c = a
# a = b
# b = c
# a, b = b, a

# a = a + b  # a=1+2=3
# b = a - b  # b=3-2=1
# a = a - b  # a=3-1=2
# print(a)
# print(b)
# print("a:", a)
# print("b:", b)

# print("строка \
#   ")
# print('строка')
#
# print("Документ  \n\"script.py\" ")

# s1 = "Hello"
# s2 = "Hel"
# print(s1 + ", " + s2 + "!\t\t")
# print("*" * 30)

# number = 6 + 4 * 5 ** 2 + 7
# print(number)

# num = 10
# num += 5  # num = num + 5
# print(num)

# num = 4321
# a = num % 10
# print(a)
# b = (num // 10) % 10
# print(b)
# c = (num // 100) % 10
# print(c)
# d = (num // 1000) % 10
# print(d)
# e = a * 1000 + b * 100 + c * 10 + d
# print(e)

# num1 = 4321
# print(num1)
# res = (num1 % 10) * 1000
# num1 = num1 // 10
# res += (num1 % 10) * 100
# num1 = num1 // 10
# res += (num1 % 10) * 10
# num1 = num1 // 10
# res += num1 % 10
# print(res)

# int() - преобразовывает к целочисленному типу данных
# float() - преобразовывает к вещественному типу данных
# str() - преобразовывает к строковому типу данных

# print(int(3.8))
# print(round(3.8324))
# print(round(3.89, 2))
# float()
# a = '5.2'
# b = 10
# c = float(a) + b
# print(c)

# a = 1
# b = 2
# print("a: ", a, "\nb: ", b)

# name = "Виктор"
# age = 28
# print("Меня зовут", name, ". Мне", age, "лет.")
# print("Меня зовут " + name + ". Мне " + str(age) + " лет.")
# print("Меня зовут", name, ". Мне", age, "лет.", sep=" ", end="!!!")
# print("Я учу Python")

# name = input("Ваше имя: ")
# city = input("Ваш город: ")
# print(name, city)


# a = int(input("Введите число: "))
# b = int(input("Введите степень: "))
# c = a ** b
# print(c)
# print("Введите четыре числа: ")
# a = int(input("1: "))
# b = int(input("2: "))
# c = int(input("3: "))
# d = int(input("4: "))
# sum1 = a + b
# sum2 = c + d
# del1 = sum1 / sum2
# print("Результат:", round(del1, 2))

# a = True
# b = False
# print(a + 5)
# print(b * 5)

# print(bool("python"))  # True
# print(bool(""))  # False
# print(bool(0.00001))  # True
# print(bool(None))  # True

# test = None
# print(test)
# test = 5
# print(test)

# print(7 == 7)
# print(2 + 5 != 7)
# print(8 > 7)
# print(8 < 7)
# print("Привет" == "привет")

# print(2 < 5 < 9)
# print(2 * 5 > 7 >= 4 + 3)
# print(9 * 3 <= 7 >= 2)

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)

# print(not 9-7)

# cnt = 155
# if cnt < 10:
#     cnt += 1
# print(cnt)

# age = int(input("Введите свой возраст: "))
# if age >= 18:
#     print("Доступ на сайт разрешен")
# else:
#     print("Доступ запрещен")

# a = 15
# b = 15
# if a > b:
#     print("a > b")
# elif a == b:
#     print("a == b")
# else:
#     print("b > a")

# print("Введите стороны треугольника")
# a = int(input("Введите сторону 1: "))
# b = int(input("Введите сторону 2: "))
# c = int(input("Введите сторону 3: "))
#
# if a == b and b == c and c == a:
#     print("Равносторонний")
# elif a == b or b == c or c == a:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# a = int(input("Введите номер месяца: "))
# if 0 < a < 13:
#     if a == 1 or a == 2 or a == 12:
#         print("Зима")
#     if a == 3 or a == 4 or a == 5:
#         print("Весна")
#     if a == 6 or a == 7 or a == 8:
#         print("Лето")
#     if a == 9 or a == 10 or a == 11:
#         print("Осень")
# else:
#     print("Ошибка ввода данных")

# day = int(input("Введите день недели (цифрой): "))
# if 1 <= day <= 5:
#     print("Рабочий день - ", end="")
#     if day == 1:
#         print("понедельник")
#     if day == 2:
#         print("вторник")
#     if day == 3:
#         print("среда")
#     if day == 4:
#         print("четверг")
#     if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ", end="")
#     if day == 6:
#         print("суббота")
#     if day == 7:
#         print("воскресенье")
# else:
#     print("Такого дня недели не существует!")

# n = int(input("Введите количество ворон: "))
# if 0 <= n <= 9:
#     print("На ветке ", end="")
#     if n == 1:
#         print(n, "ворона")
#     elif 2 <= n <= 4:
#         print(n, "вороны")
#     else:
#         print(n, "ворон")
# if n == 1:
#     print(n, "ворона")
# if 2 <= n <= 4:
#     print(n, "вороны")
# if 5 <= n <= 9 or n == 0:
#     print(n, "ворон")
# else:
#     print("Ошибка ввода данных")

# a = int(input("Введите число от 1 до 99: "))
# kop = a
# if 11 <= a <= 14:
#     print(a, "копеек")
# elif 1 <= kop <= 10 or 15 <= kop <= 99:
#     kop = kop % 10
#     if kop == 1:
#         print(a, "копейка")
#     elif 2 <= kop <= 4:
#         print(a, "копейки")
#     else:
#         print(a, "копеек")
# else:
#     print("Некорректный ввод ")

# Тернарное выражение
# a, b = 30, 20
# minim = a if a < b else b
# print(minim)

# a, b = 30, 0
# print("Делить на ноль нельзя" if b == 0 else a / b)

# try:
#     n = int(input("Введите целое число: "))
#     print(n * 2)
# except ValueError:
#     print("Что-то пошло не так")
# print("Код далее")

# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except ValueError:
#     print("Нельзя вводить строки")
# except ZeroDivisionError:
#     print("Нельзя делить на ноль")
# try:
#     n = int(input("Введите делимое: "))
#     m = int(input("Введите делитель: "))
#     print(n / m)
# except (ValueError, ZeroDivisionError):
#     print("Нельзя вводить строки")
#     print("Нельзя делить на ноль")
# else:
#     print("Вы ввели числа", n, "и", m)
# finally:
#     print("Конец программы")

# n = input("Введите первое число: ")
# m = input("Введите первое число: ")
# try:
#     n = int(n)
#     m = int(m)
# except ValueError:
#     n = str(n)
#     m = str(m)
# finally:
#     print(n + m)

# i = 0
# while i < 5:
#     i += 1  # i = i + 1
#     print("i =", i)

# i = 1
# while i < 21:
#     if i % 2 == 0:
#         print("i =", i)
#     i += 1  # i = i + 1

# i = 0
# while i < 20:
#     i += 2  # i = i + 1
#     print("i =", i)

# n = int(input("Укажите количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Укажите количество символов: "))
#
# while n > 0:
#     print("*", end="")
#     n -= 1

# sum1 = 0
# n = input("Введите начало диапазона: ")
# m = input("Введите конец диапазона: ")
# if n < m:
#     while n <= m:
#         if n


# sum1 = 0
# i = int(input("Введите начало диапазона: "))
# p = int(input("Введите конец диапазона: "))
# if i <= p:
#     while i <= p:
#         if i % 2 != 0:
#             sum1 += i
#         i += 1
#     print(sum1)
# else:
#     while p <= i:
#         if p % 2 != 0:
#             sum1 += p
#         p += 1
#     print(sum1)

# n = input("Введите целое число: ")
# while type(n) != int:
#     try:
#         n = int(n)
#     except ValueError:
#         print("Число не целое!")
#         n = input("Введите целое число: ")
#
#
# if n % 2 == 0:
#     print("Четное число")
# else:
#     print("Нечетное число")

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#
#     if i == 5:
#         break
#     i += 1
# print("\nЦикл завершен")

# while True:
#     n = int(input("Введите положительное число: "))
#     if n > 0:
#         break
# s = 1
# while True:
#     n = int(input("Введите  число: "))
#     if n == 0:
#         break
#     s *= n
# print("Произведение: ", s)

# i = 0
# while i < 10:
#     if i == 5:
#         break
#     print(i)
#     i += 1
# else:
#     print("Цикл окончен, i = ", i)

# i = 1
# while i < 5:
#     print("Внешний цикл: i =", i)
#     j = 1
#     while j < 4:
#         print("\tВнутренний цикл: j =", j)
#         j += 1
#     i += 1

# i = 1
# while i <= 9:
#
#     j = 1
#     while j <= 9:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 3:
#     j = 0
#     while j < 6:
#         print('^', end='')
#         j += 1
#     print()
#     i += 1


# i = 1
# while i <= 5:
#     j = 0
#     while j < 20:
#         if j % 2 != 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1


# for i in 'Hello':
#     print(i)

# for color in 'red', 'orange', 'yellow':
#     print("color: ", color, type(color))

# range(stat, stop, step)
# for i in range(2, 9, 3):
#     print(i, end=" ")
# print()
# j = 2
# while j < 9:
#     print(j, end=" ")
#     j += 1

# n = int(input('Введите целое число: '))
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i, end=' ')

# for i in range(10, 100):
#     if i // 10 == i % 10:
#         print(i, end=" ")

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
# else:
#     print('done')

# for i in range(3):
#     print("+++")
#     for j in range(2):
#         print("-----")

# a = int(input("Введите длину прямоугольника: "))
# b = int(input("Введите высоту прямоугольника: "))
# for i in range(b):
#     for j in range(a):
#         print("*", end="")
#     print()

# a = int(input("высота прямоугольника: "))
# b = int(input("Ширина прямоугольника: "))
# for i in range(a):
#     print()
#     for j in range(b):
#         if 0 < i < a - 1 and 0 < j < b - 1:
#             print(" ", end="")
#         else:
#             print("*", end="")


# a = int(input("высота прямоугольника: "))
# b = int(input("Ширина прямоугольника: "))
# for i in range(a):
#     for j in range(b):
#         if i == 0 or j ==0 or i == a - 1 or j == b - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# a = 123
# b = 2
# res = 0
# if a < b:  # a, b = ((a, b) if a < b else (b, a))
#     while a <= b:
#         if a % 2 != 0:
#             res += a
#         a += 1
# else:
#     while b <= a:
#         if b % 2 != 0:
#             res += b
#         b += 1
# print(res)

# a = [i * 3 for i in "Hello"]
# print(a)
#
# for i in "Hello":
#     print(i * 3)

# num = [i for i in range(30) if i % 2 == 0]
# print(num)

# Списки list
# num = [8, 3, 9, 4, 1,[1,2,3]]
# print(num)
# print(type(num))
# print(num[1])
# print(num[5][1])
# print(num[-1])
# num[2] = 256
# print(num)
# num[1] += 100
# print(num)

# num = [8, 3, "one", 3.2, [1, 2, 3]]
# print("Длина списка:", len(num))

# s = []
# print(type(s))
# b = list("Hello")
# print(b)

# s = [5, 1] * 6
# print(s)

# n = list(range(2, 10, 2))
# print(n)
#
# n2 = [2, 4, 6, 8]
# print(n2)
# if n == n2:
#     print("Списки равны")
# else:
#     print("Списки разные")

# [выражение for переменная in последовательность]
# n = 5
# a = [i ** 2 for i in range(1, n + 1)]
# print(a)

# a = [1, 2, 3]
# b = [5, 6]
# c = b + a
# print(c)
# d = c * 2
# print(d)

# a = [0] * int(input("Введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = int(input("-> "))
# print(a)

# a = [int(input("-> ")) for i in range(int(input("Количество элементов: ")))]
# print(a)

# a = [4, 8, 9, 3, 2]
# for i in range(len(a)):
#     print(a[i], end=" ")
# print()
# for i in a:
#     print(i, end=" ")

# let = ['один']
# sum1 = 0
# a = [0] * int(input("Введите количество элементов списка: "))
# for i in range(len(a)):
#     a[i] = int(input("-> "))
#     if a[i] < 0:
#         sum1 += a[i]
# print(sum1)

# n = list(range(21, 41))
# print(n)
# k = s = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("Количество четных элементов -", k)
# print("Сумма нечетных элементов -", s)

# n = 5
# zero_elem = 0
# sum1 = 0
# lst = [int(input('-> ')) for _ in range(n)]
# for i in lst:
#     if i == 0:
#         zero_elem += 1
#     sum1 += i
# print('Среднее арифметическое - ', sum1 / (n - zero_elem))

# a = [int(input('-> '))for i in range(int(input('Введите количество элементов: ')))]
# count = 0
# summa = 0
# for i in a:
#     summa += i
#     count += 1 if i != 0 else 0
# print('Среднее арифметическое: ', summa/count)

# a = [int(input('-> ')) for i in range(int(input('Введите количество элементов: ')))]
# for i in range(len(a)):
#     if i % 2 == 0:
#         print(a[i], end=' ')

# a = [7, 8, 2, 1, 17]
# print(a)
# a[0], a[-1]= a[-1], a[0]
# print(a)

# size = int(input("Введите размер поля: "))
# symbol = int(input("Введите количество символов: "))
# for i in range(size):
#     for j in range(symbol):
#         for n in range(size):
#             for m in range(symbol):
#                 print("  " if (i + n) % 2 else "* ", end="")
#         print()

# Срезы

# Списки[start:stop:step]
# s = [5, 9, 3, 7, 1, 8]
# print(s[1:4])
# print(s[2:])
# print(s[:2])
# print(s[::-1])
# print(s[-2:2:-1])
# print(s[1:4:-1])
# print(s[1:4:-1])

# s = [1, 2, 3, 4, 5, 6, 7]
# print(s[:])
# print(s[::-1])
# print(s[::2])
# print(s[1::2])
# print(s[:1])
# print(s[-1:])
# print(s[3:4])
# print(s[4:])
# print(s[-3:1:-1])
# print(s[2:5])

# s[1:3] = [0, 0, 0, 0]
# print(s)
# s[1:2] = [20]
# print(s)
# s[3] = 30
# print(s)
# s=[]
# for i in range(1, 11):
#     s.extend([i ** 2])
# print(s)
# Методы списков

# s = [1, 20, 0, 30, 4, 5, 6, 7]
# print(s)
# s.append(99)  # добавляет один элемент в конец списка
# print(s)
# s.extend([9, 8, 7])  # добавляет множество элементов в конец списка
# print(s)
# s.extend('add')
# print(s)
# s.insert(0, 100)  # добавляет заданное значение (второй параметр) по указанному индексу (первый параметр)
# print(s)
# s1 = []
# s1.extend([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(s1)
#
# s = []
# for i in range(1, 11):
#     s.extend([i ** 2])
# print(s)


# lst = []
# n = int(input("Количество элементов списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     # lst.append(x)
#     # lst.extend([x])
#     lst.insert(-1, x)
#
# print(lst)

# n = int(input("Кол-во элементов списка: "))
# i = 0
# lst = []
# while i < n:
#     x = int(input('Введите число кратное 3: '))
#     if x % 3 != 0:
#         print(x, 'число не делится на 3 без остатка')
#     else:
#         lst.append(x)
#     i += 1
# print(lst)
# lst = []
# n = int(input("Кол-во элементов списка: "))
# for num in range(n):
#     x = int(input('Введите число кратное 3: '))
#     if x % 3 != 0:
#         print(x, 'число не делится на 3 без остатка')
#     else:
#         lst.append(x)
# print(lst)


# a = [5, 9, 2, 1, 4, 3]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i == c:
#             continue
#         if i == j:
#             c.append(i)
#             break
# print(c)

# a = [1, 2, 3, 4, 2]
# b = [11, 22, 33]
# c = []
# print("a =", a)
# print("b =", b)
# if len(b) > len(a):
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)): #  range(3, 5)
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(b[i])
#         c.append(a[i])
#     for i in range(len(b), len(a)):  # range(3, 5)
#         c.append(a[i])
# print(c)

# s = [1, 20, 0, 30, 4, 5, 6, 7, 0, 2]
# # s[3:] = []
# # s[2:6] = []
# if 20 in s:
#     s.remove(20)  # удаляет элемент по значению, первое совпадение
# print(s)
# i = 0
# while i in s:
#     s.remove(i)
#     i += 1
# print(s)
# last = s.pop()  # УДАЛЯЕТ последний элемент из списка и возвращает удаленный элемент
# print(last)
# print(s)
# second = s.pop(-2)  # Удаляет элемент по индексу
# print(second)
# print(s)
# s.clear()
# del s[:]
# del s[2]
# print(s)

# n = [int(input('-> ')) for i in range(int(input('Введите количество элементов: \nn = ')))]
# k = (int(input('Введите количество элементов: \nk = ')))
# del n[k]
# print(n)

# print(dir(list))

# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# num = s.count(0)  # считает количество заданных значений в списке
# print(num)
# ind = s.index(0, 6, -1)  # возвращает положение первого индекса с заданным значением
# print(ind)

# a = [1, 2, 3]
# b = a
# s_copy = a.copy()  # возвращает копию списка, расположенную по другому адресу
# print("a = ", a)
# print("b = ", b)
# print("s_copy = ", s_copy)
# a.append(20)
# b.append(4)
# s_copy.append(444)
# print("a = ", a)
# print("b = ", b)
# print("s_copy = ", s_copy)
# print(id(a))
# print(id(b))
# print(id(s_copy))

# s = [1, 20, 0, 30, 4, 0, 5, 6, 7, 0, 2]
# s.reverse()  # возвращает None, переставляет элементы списка в обратном порядке
# print(s)
#
# s.sort(reverse=False)
# print(s)
#
# s2 = ["Виталий", "Сергей", "Александр", "Анна"]
# s2.sort(key=len, reverse=True)
# print(s2)

# srt = sorted(s)
# print(srt)
# print(s)

# Генерация случайных данных

# import random
# from random import randint, randrange
#
# print(random.random())
#
# print(randint(0, 100))  # от 0 до 100
# print(randrange(0, 100, 1))  # от 0 до 99 с шагом

# from random import *
# print(randint(0, 100))  # от 0 до 100
# print(randrange(0, 100, 1))
# print(round(uniform(10.5, 25.5), 2))
#
# s = [55, 66, 77, 88, 99, 20, 30, 80, 90]
# print(choice(s))  # возвращает одно значение из списка
# print(choices(s, k=3))  # возвращает случайные элемент списка и может повторяться
# print(s)
# shuffle(s)
# print(s)
#
# mas = [randint(0, 20) for i in range(10)]
# print(mas)

# lst = [5, 3, 2, 4, 1]
# print(len(lst))
# print(sum(lst))  # только с числами
# print(min(lst))
# print(max(lst))
from random import *
# lst = [randint(0, 100) for i in range(10)]
# max_ = max(lst)
# print(lst)
# print(max_)
# lst.remove(max_)
# lst.insert(0, max_)
# print(lst)


# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# l = lst.pop(lst.index(max(lst)))
# lst.insert(0, l)
# print(lst)

# lst = [randint(-20, 20) for i in range(10)]
# print(lst)
# lst.sort(reverse=True)
# print(lst)

# lst = [randint(0, 100) for i in range(10)]
# print(lst)
# m = min(lst)
# print("Min: ", m)
# li = lst.index(m)
# print("Index min:", li)
# # lst[:li] = []
# del lst[:li]
# print(lst)

# x = list('1a2b3c4d')
# print(x)
# print('a' in x)
# print('e' in x)
# print('a' not in x)
# print('e' not in x)

# lst = []
# # if len(lst) == 0:
# print(bool(lst))
# if not lst:
#     print("Список пустой")

# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
# a = [randint(0, 10) for i in range(n1)]
# b = [randint(0, 10) for j in range(n2)]
# print("Первый список:", a)
# print("Второй список:", b)
# c = a + b
# print("Третий список:", c)
# c = []
# for i in range(len(a)):
#     if a[i] not in c:
#         c.append(a[i])
# for i in range(len(b)):
#     if b[i] not in c:
#         c.append(b[i])
# print("Элементы обоих списков без повторений:", c)
#
# c = []
# for i in range(len(a)):
#     if a[i] in b and a[i] not in c:
#         c.append(a[i])
# print("Элементы общие для двух списков:", c)
#
# c = [min(a), min(b), max(a), max(b)]
# print(c)

# k = int(input("Размер списка: "))
# s = []
# while len(s) < k:
#     n = randint(0, k - 1)
#     if n not in s:
#         s.append(n)
# print(s)

# n1 = int(input("Размер списка: "))
# a = [randint(0, n1 - 1) for i in range(n1)]
# s = []
# for i in range(n1):
#     a = [randint(0, n1 - 1)]
#     if a[i] not in s:
#         a.append(a[i])
# print(s)

# m = [
#     [1, 2, 3, 4],  # строка 0
#     [5, 6, 7, 8],  # строка 1
#     [9, 10, 11, 12]  # строка 2
# ]
# print(m)
# print(m[1][2])

# for row in range(len(m)):
#     # print(m[row])
#     for col in range(len(m[row])):
#         print(m[row][col], end="\t")
#     print()

# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()
#
# m = [
#     [0, 0, 0, 0, 0],  # строка 0
#     [0, 0, 0, 0, 0],  # строка 1
#     [0, 0, 0, 0, 0]  # строка 2
# ]
# for row in m:
#     # print(row)
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
#
# q = [[x ** 2 for x in row] for row in m]
# for row in q:
#     for x in row:
#         print(x, end="\t\t")
#     print()

# n, m = int(input('Введите высоту матрицы: ')), int(input('Введите ширину матрицы: '))
# matr = [[0 for i in range(m)] for j in range(n)]
# for row in matr:
#     for x in row:
#         print(x, end='\t')
#     print()

# for x, y in [1, 2], [3, 4], [5, 6], [7, 8]:
#     print(x, "+", y, "=", x + y)

# w, h = 5, 4
# matrix = [[randint(1, 30) for x in range(w)]for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t')
#     print()

# w, h = 3, 4
# matrix = [[randint(0, 4) for x in range(w)]for y in range(h)]
# count = 0
# for row in matrix:
#     for x in row:
#         if x < 0:
#             count += x
#         print(x, end='\t\t')
#     print()
# print("Количество отрицательных элементов:", count)

# w, h = 3, 4
# matrix = [[randint(0, 4) for x in range(w)]for y in range(h)]
# count = 1
# for row in matrix:
#     for x in row:
#         if x != 0:
#             count *= x
#         print(x, end='\t\t')
#     print()
# print("Количество отрицательных элементов:", count)

# w, h = 6, 6
# matrix = [[randint(0, 10) for x in range(w)]for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end='\t\t')
#     print()
# print()
#
# for row in range(len(matrix)):
#     if row % 2 == 0:
#         for col in range(len(matrix[row])):
#             print(matrix[row + 1][col], end="\t\t")
#         print()
#         for col in range(len(matrix[row])):
#             print(matrix[row][col], end="\t\t")
#         print()

import math

# print(dir(math))
# num1 = math.sqrt(2)
# print(num1)
# num2 = math.ceil(3.2)
# print(num2)
# num3 = math.floor(3.8)
# print(num3)
# print(math.pi)
#
# radius = 2
# print("Площадь окружности с радиусом", radius, "=>", math.pi * (radius ** 2))

# a = int(input("Введите радиус окружности: "))
# print("Длина окружности:", round(2 * math.pi * a, 2))

import time

# second = time.time()
# print(second)
# localtime = time.ctime()
# print(localtime)
# res = time.localtime()
# print(res)
# print(res.tm_year)
# print(time.strftime("Today is %b %d, %Y, %Z"))
#
# pause = 5
# print("Program started...")
# time.sleep(pause)
# print(pause, "seconds.")

# text = input("Название напоминания: ")
# local_time = float(input("Через сколько минут: "))
# local_time = local_time * 60
# time.sleep(local_time)
# print(text)

# start = time.monotonic()
# time.sleep(2)
# finish = time.monotonic()
# res = finish - start
# print(res)
# import locale
# locale.setlocale(locale.LC_ALL, "ru")
# print(time.strftime("Сегодня %B %d, %Y"))


# def hello(name, word):
#     print("Hello,", name, "Say", word)
#
#
# hello("Irina", "hi")
# hello("Ivan", "hello")


# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)

# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#
#
# symbol(9, "+", "-")
# print()
# symbol(7, "X", "0")


# def get_sum(a, b):
#     return a + b
#
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)
# print(get_sum(1, 8))


# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))


# def maximum(one, two):
#     if one > two:
#         return one - two
#     else:
#         return one + two
#
#
# a = int(input("a = "))
# b = int(input("b = "))
# c = maximum(a, b)
# print(c)

# def change(lst):
#     # lst[0], lst[-1] = lst[-1], lst[0]
#     start = lst.pop()
#
#     end = lst.pop(0)
#     lst.append(end)
#     lst.insert(0, start)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(["с", "л", "о", "н"]))

# def is_greater(x, y):
#     if x > y:
#         return True
#     else:
#         return False
#
#
# print(is_greater(10, 5))
# print(is_greater(5, 10))

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_num = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif "a" <= ch <= "z":
#             has_lower = True
#         elif "0" <= ch <= "9":
#             has_num = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_num:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#
#     print("Это надежный пароль")
# else:
#     print("Это не надежный пароль")

# def get_sum(a, b, c=0, d=0):
#     return a + b + c + d
#
#
# q = 2
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5, d=q))

# def symbol(a=20, b="-"):
#     return a * b
#
#
# print(symbol())
#
# x = int(input("Введите количество символов: "))
# y = input("Введите символ: ")
#
# print(symbol(x, y))


# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         cur_digit = n % 10
#         if even and cur_digit % 2 == 0:
#             s += cur_digit
#         elif not even and cur_digit % 2:
#             s += cur_digit
#         n //= 10
#     return s
#
#
# print("Сумма четных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("Сумма нечетных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))

# def display_info(name, age):
#     print("Name:", name, "\nAge:", age)
#
#
# display_info("Roman", 38)
# display_info(38, "Roman")
# display_info(age=38, name="Roman")
# display_info("Igor", age=38, name="Roman")

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2)
# print(lt1 is lt2)
#
# a = "Hello"
# b = "Hello"
# print(a == b)
# print(a is b)

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1.append(4)
# print(lt1)
# print(id(lt1))
# lt1.pop(1)
# print(lt1)
# print(id(lt1))
# lt1[1] = "Hello"
# print(lt1)
# print(id(lt1[1]))
# print(id(lt1))

# s = "Hello"
# print(id(s))
# s += "World"
# print(s)
# print(id(s))

# a = 5
# print(id(a))
# a += 1
# print(a)
# print(id(a))

# s = "Hello"
# print(id(s))
# s = s[1:-1]
# print(s)
# print(id(s))
#
# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1 = lt1[1:-1]
# print(lt1)
# print(id(lt1))

# lt1 = [1, 2, 3]
# print(id(lt1))
# lt1 = lt1 + [4, 5]
# print(lt1)
# print(id(lt1))

# Кортеж (tuple)
# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())

# a = (1, 2, 3, 4, 5)
# print(type(a))
# print(a)
# b = tuple()
# print(type(b))

# c = tuple("Hello")
# print(c)

# t = (1,)
# print(t)
# print(type(t))

# b = tuple((1, 2, 3, 4, 5))
# print(b)
# print(b[2])
# print(b[1:3])
# print(id(b[2]))

# s = tuple(int(input("-> ")) for i in range(3))
# print(s)

# s = input("Строка: ")
# a = tuple(s)
# print(a)

# mas = [randint(0, 100) for i in range(10)]
# print(mas)
# trl = tuple(mas)
# print(trl)
# print(tuple(randint(0, 100) for _ in range(10)))

# mas = tuple(2 ** i for i in range(1, 13))
# print(mas)
# t1 = tuple('hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3)
# print(len(t3))
# print(t3.count('l'))
# print(t3.count('a'))
# print(t3.index('l', 4))
# for i in t3:
#     print(i, end=' ')

# def slicer(a, b):
#     if b in a:
#         if a.count(b) > 1:
#             first = a.index(b)
#             second = a.index(b, first + 1)
#             return a[first:second + 1]
#         else:
#             return a[a.index(b):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
# def ran(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# mas1 = ran(0, 6)
# mas2 = ran(-5, 0)
# mas3 = mas1 + mas2
# print(mas1)
# print(mas2)
# print(mas3)
# print("0 =", mas3.count(0))

# t = (10, 11, [1, 2, 3], (4, 5, 6), ['hello', 'world'])
# print(t, id(t))
# t[-1][0] = 'new'
# t[4].append('hi')
# print(t, id(t))

# def a(lst):
#     s = []
# for i in lst[::-1]:
#     if i not in s:
#         s.append(i)
#     [s.append(i) for i in reversed(lst) if i not in s]
#     return tuple(s)
#
#
# print(a([1, 2, 3, 3, 2]))
# print(a([2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]))

# t = (1, 2, 3)
# # x = t[0]
# # y = t[1]
# # z = t[2]
# x, y, z = t  # распаковка кортежа
# print(x, y, z)

# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# print(user[0])
# name1, age1, is_married1 = user
# print(name1)

# a = (1, 2, 3)
# # del a
# print(a)
# lst = list(a)
# lst.append(4)
# print(lst)
# tpl = tuple(lst)
# print(tpl)

# countries = (
#     ('Германия', 80.2, (('Берлин', 3.326), ('Гамбург', 1.718))),
#     ('Франция', 66, (('Париж', 2.2), ('Марсель', 1.6)))
# )
#
# print(countries, end='\n\n')
#
# for country in countries:
#     # print(country)
#     countryName, countryPopulation, cities = country
#     print("\nСтрана:", countryName, "население =", countryPopulation, cities)
#     for city in cities:
#         # print(city)
#         cityName, cityPopulation = city
#         print("\tГород", cityName, "население =", cityPopulation)

# Множество (set)

# s = {"banana", "apple", "orange", "apple", "banana"}
# print(type(s))
# print(s)
# print(len(s))

# a = set('hello')
# print(type(a))
# print(a)

# s = {x * x for x in range(10)}
# print(s)

# num = [1, 2, 2, 2, 3, 3, 4, 4, 5, 6]
# num = set(num)
# print(num)
# num = list(num)
# print(num)

# def to_set(element):
#     return set(element), len(set(element))
#
#
# print(to_set('я обычная строка'))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {'red', 'green', 'blue'}
# # print('green' in t)
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = {i for i in r if 'a' not in i}
# a = {'A' + i[1:] for i in r if i[0] == 'a'}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r}
# a = {'A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c'}
# print(a)


# a = {"Tom", "Bob", 0, 1, 2, 3}
# a.add("Ann")
# print(a)
# # a.remove("Tom")
# # print(a)
# user = "Tom"
# if user in a:
#     a.remove(user)
# print(a)
# a.discard("Bob")
# print(a)
# a.pop()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# c = a.union(b)
# c = a | b
# print(c)
# a |= b
# c = a & b
# a &= b
# print(a)
# c = a - b
# c = a ^ b
# print(c)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# print(len(s))
# print(min(s))
# print(max(s))

# s1 = "Hello"
# s2 = "How are you"
# c = set(s1) & set(s2)
# print(c)

# s1 = "Python"
# s2 = "Programming language"
# s = set(s1) - set(s2)
# print(s)

# drawing = {"Марина", "Женя", "Света"}
# music = {"Костя", "Женя", "Илья"}
# both = drawing & music
# only = drawing ^ music
# print("Одно хобби: ", only)
# print("Два хобби: ", both)
#
# drawing = drawing - both
# print(drawing)

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
#
# a = frozenset({"hello", "world"})
# print(a)

# Словари (dict)

# s = ['one', 'two']
# print(s)
# d = {1: 'one', 2: 'two'}
# print(d)

# d = {'one': 1, 'two': 2}
# print(d)
# print(type(d))
#
# d1 = dict(one=1, two=2)
# print(d1)
# print(type(d1))

# a = [
#     ('igor@gmail.com', 'igor'),
#     ('irina@gmail.com', 'irina'),
#     ('anna@gmail.com', 'anna')
#
# ]
# d = dict(a)
# print(d)

# d = {a: a ** 2 for a in range(1, 7)}
# print(d)
# print(d[2])
# d[2] = 15
# print(d)
# d[6] = 4 ** 2
# print(d)

# d = {0: 'text', "one": 45, (1, 2.3): "кортеж", 42: [2, 3, 6, 7], True: 1}
# print(d)
# print(d[(1, 2.3)])
# print(d[42][1])
# print(d[42])
# print('one' in d)
# print('two' in d)
#
#
# print(d.keys())
# if 'one' in d:
#     print('TRUE')

# print(d[2])

# key = 'four'
# key = 2

# if key in d:
#     del d[key]

# try:
#     del d[key]
# except KeyError:
#     print("No element " + str(key) + " in words")
# print(d)

# for key in d:
#     print(key, d[key])

# a = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# c = a['x1'] * a['x2'] * a['x3'] * a['x4']
# print(c)
# b = 1
# for key in a:
#     b *= a[key]
# print(b)
#
# d = dict()
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")

# d = {a: input("-> ") for a in range(1, 5)}
# print(d)
# a = int(input("Какой элемент исключить: "))
# if a in d:
#     del d[a]
#     print(d)
# else:
#     print("Такого элемента нет")

# capitals = dict()
# capitals['Россия'] = 'Москва'
# capitals['Италия'] = 'Рим'
# capitals['Испания'] = 'Мадрид'
# print(capitals)
# countries = ['Россия', 'Италия', 'Франция', 'Испания']
#
# for country in countries:
#     if country in capitals:
#         print('Столица страны ' + country + ": " + capitals[country])
#     else:
#         print("В базе нет такой страны с названием " + country)

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400]
# }
#
# for i in goods:
#     print(i, ') ', goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input("№: ")
#     if n != '0':
#         cnt = int(input("Количество: "))
#         goods[n][1] = cnt
#     else:
#         break
#
# for i in goods:
#     print(i, ') ', goods[i][0], " - ", goods[i][1], " шт. по ", goods[i][2], "руб", sep="")
#
#
# d = {'a': 1, 'b': 2, 'c': 3 }
# print(d['b'])
# value = d.get('e', 'False')
# print(value)
# print(d)
# item = d.items()
# print(item)
# key = d.keys()
# print(key)
# value = d.values()
# print(value)
#
# for i in d:
#     print(i)
# for i in d.values():
#     print(i)
# for i, j in d.items():
#     print(i, "->", j)

# d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# print(d)
# d.clear()
# item = d.pop('b', 5)
# print(item)
# it = d.popitem()
# print(it)
# item = d.setdefault('e', 5)
# # print(item)
# d.update({'a': 7, 'q': 9})  # [('a', 7), ('q', 9)]
# print(d)
# d2 = d.copy()
#
# print("D =", d)
# print("D2 =", d2)
#
# d['e'] = 7
# d2['b'] = 5
# print("D =", d)
# print("D2 =", d2)

# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# z = x.copy()
# z.update(y)
# z = x | y
# print(z)

# d = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# new_d = dict()
#
# new_d['name'] = d.pop('name')
# new_d['salary'] = d.pop('salary')
#
# print(d)
# print(new_d)
# d['location'] = d.pop('city')
# print(d)

# a = {
#     'First': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'Second': {
#         4: 'four',
#         5: 'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print('\t', y,": ", a[x][y], sep="")

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# a = {key: value for key, value in d.items() if value <= 2}
# print(a)

# a = {i: i * 5 for i in [10, 20, 30, 40]}
# print(a)

# a = {i: i * 5 for i in "Hello"}
# print(a)

# value = int(input('-> '))
# # lt = [1, 2, 3, 4, 5]
# a = {i: value for i in range(1, 9)}
# print(a)

# d = dict.fromkeys(['a', 'b'], 100)
# print(d)

# list()

# figures = {1: 'Rectangle', 2: 'Triangle', 3: 'Circle'}
# value = list(figures)
# value = list(figures.values())
# value = list(figures.items())
# print(value)

# a = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# d = {}
# s = ''
#
# for i in a:
#     if type(i) == str:
#         d[i] = []
#         s = i
#     else:
#         d[s].append(i)
#
# print(d)


# zip()

# d = dict(zip([12, 1, 2], ['Dec', 'Jan', 'Feb']))
# print(d)

# a = [12, 1, 2]
# b = ['Dec', 'Jan', 'Feb']
# f = {k: v for k, v in zip(a, b)}
# print(f)

# a = [1, 2, 3]
# print(list(zip(a)))

# print(list(zip(range(5), range(100))))

# a = {'name': 'Igor', 'last_name': 'Doe', 'job': 'Consultant'}
# b = {'name': 'Irina', 'last_name': 'Smith', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(a.items(), b.items()):
#     print(k1, '-> ', v1, v2)

# a = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
# x, y = zip(*a)
# print(x)
# print(y)

# lt1 = [22, 1, 41, 433]
# lt2 = ['a', 'c', 'd', 'b']
# a1 = list(zip(lt1, lt2))
# print(a1)
# a1.sort()
# a = sorted(zip(lt1, lt2))
# print(a)

# month = ['January', 'February', 'March']
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
#
# for sales, cost, m in zip(total_sales, prod_cost, month):
#     res = sales - cost
#     print("Чистая прибыль в", m, "=", res)

# one = {'apple': 0.4, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})
#
# for k, v in {**one, **two}.items():
#     print(k, "-> ", v)

# en = ["red", "green", "blue"]
# j = 1
# for i in en:
#     print(j, "-ый цвет: ", i, sep="")
#     j += 1

# en = ["red", "green", "blue"]
# for j, i in enumerate(en, 1):
#     print(j, "-ый цвет: ", i, sep="")

# en = {0: 1, 1: 2, 2: 3}
#
# for i, j in enumerate(en, 1):
#     print(i, ": ", j, "->", en[j], sep="")

# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)


# def func(*args):
#     return args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# num1 = summa(1, 2, 3, 4, 5, 6, 7, 8)
# num2 = summa(6, 7, 8)
# print(num1)
# print(num2)


# def to_dict(*args):
#     return {i: i for i in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict('gray', (2, 17), 3.11, -4))

# def a(*b):
#     res = []
#     sred = sum(b) / len(b)
#     print(sred)
#     for i in b:
#         if i < sred:
#             res.append(i)
#     return res
#
#
# print(a(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(a(3, 6, 1, 9, 5))


# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 'abc'))


# def print_scores(stud, *scores):
#     print("Student name: ", stud)
#     for score in scores:
#         print(score, end=" ")
#     print()
#
#
# print_scores("Jonatan", 100, 95, 88, 92, 99)
# print_scores("Rick", 96, 20, 33)


# def func(*args):
#     res = []
#     for i in args:
#         res.append(int(str(i)[::-1]))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))

# def reverse_num(n):
#     s = str(n)
#     return int(s[::-1])
#
#
# def func(*args, only_odd=False):
#     res = []
#     for i in args:
#         if not only_odd or (only_odd and i % 2):
#             res.append(reverse_num(i))
#     return res
#
#
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91))
# print(func(12, 2345, 323, 4456, 5687, 62, 734, 81, 91, only_odd=True))

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(a="Python"))

# def info(**data):
#     for k, v in data.items():
#         print(k, "->", v)
#
# info(fist_name="Irina", last_name="Petrova", age=22, phone=1234567890)
# info(fist_name="Igor", last_name="Ivanov", age=36,  email='igor@gmail.com',country="Russia" ,phone=6789012345)
# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict ={'one': 'first'}
# db(k1=22, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, weight=61, eyes_color='grey')
# print("my_dict =", my_dict)

# def func1(*args):
#     print(args[0])
#
#
# def func2(**kwargs):
#     print(kwargs['one'])
#
#
# func1(1, 2, 3, 4, 5)
# func2(one=123, two=456)

# def func(a, *args, one=True, **kwargs):
#     return a, args, kwargs, one
#
#
# print(func(5, 9, 7, 8, 6, one=False, b=2, c=3, ))


# Область видимости (scope)

# for i in range(5):
#     a = 5
#     print(i)

# if True:
#     a = 5
#
# print("a =", a)

# name = "Tom"
#
#
# def hi():
#     print("Hello", name)
#
#
# def bye():
#     global name
#     name = "Bob"
#     print("Good bye", name)
#
#
# hi()
# bye()
# print(name)

# i = 5
#
#
# def func(arg=i):
#     print(arg)
#
#
# i = 6
# func()
#
#
# def func(arg=i):
#     print(arg)
#
#
# func()


# def add_two(a):
#     x = 2
#     return a + x
#
#
# print(add_two(3))


# def func(a):
#     x = 2
#
#     def inner():
#         print("x =", x)
#         return a + x
#
#     return inner()
#
#
# print(func(5))


# a = [1, 2, 3, 4, 5]
# print(min(a))


import builtins

# print(dir(builtins))

# Вложенные функции


# def outer_func(who):
#     def inner_func():
#         print("Hello,", who)
#     inner_func()
#
#
# outer_func("world!")


# def func1():
#     a = 6
#
#     def func2(b):
#         a = 4
#         print("Сумма:", a + b)
#
#     print("a:", a)
#     func2(4)
#
#
# func1()


# x = 25
# t = 0
#
#
# def fn():
#     global t
#     a = 30
#
#     print("global:", x)
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("nonlocal:", a)
#
#     inner()
#     t = a
#
#
# fn()
# z = x + t
# print("results:", z)

# x = 5
#
#
# def fn1():
#     x = 25
#
#     def fn2():
#         # x = 33
#
#         def fn3():
#             nonlocal x
#             x = 55
#
#         fn3()
#         print('fn2.x =', x)
#
#     fn2()
#     print('fn1.x =', x)
#
#
# fn1()
# print('x =', x)


# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#     inner()
#     return [a, b]
#
#
# res = outer(2, 3, -1, 4)
# print(res)


# def increment(number):
#     def inner():
#         return number + 1
#     return inner()
#
#
# res = increment(10)
# print(res)

# Замыкание

# def outer(n):
#     def inner(x):
#         return n + x
#     return inner
#
#
# res = outer(5)
# print(res(15))
#
# res2 = outer(17)
# print(res2(15))

# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a = a + 1
#         b = b + "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())

# def func(city):
#     s = 0
#
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res2 = func('Сочи')
# res2()
# res2()
# res2()
#
# res1()


# students = {
#     'Alice': 98,
#     'Bob': 67,
#     'Chris': 85,
#     'David': 75,
#     'Elise': 54,
#     'Fiona': 35,
#     'Grace': 69
# }
#
#
# def make_classifier(lower, upper):
#     def classify_student(exam):
#         return {k: v for k, v in exam.items() if lower <= v < upper}
#
#     return classify_student
#
#
# A = make_classifier(80, 100)
# B = make_classifier(70, 80)
# C = make_classifier(50, 70)
# D = make_classifier(0, 50)
# print(A(students))
# print(B(students))
# print(C(students))
# print(D(students))

# def func(a, b):
#     def add():
#         return a + b
#
#     def sub():
#         return a - b
#
#     def mul():
#         return a * b
#
#     def replace():
#         pass
#
#     replace.add = add
#     replace.sub = sub
#     replace.mul = mul
#     return replace
#
#
# obj1 = func(5, 2)
# print(obj1.add())
# print(obj1.sub())
# print(obj1.mul())
#
# obj2 = func(15, 20)
# print(obj2.add())


# Анонимные функции, lambda-выражение

# ((lambda x, y: print(x + y))(1, 2))
# print((lambda x, y: x + y)(1, 2))
# print((lambda x, y: x + y)('a', 'b'))
#
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))


# summ = lambda a=1, b=2, c=3: a + b + c
# print(summ())
# print(summ(10))
# print(summ(10, 20))

# func1 = lambda *args: args
#
# print(func1(1, 2, 3, 4, 5))
# print(func1('a', 3, 4, 5))

# c = (lambda x: x * 2,
#      lambda x: x * 3,
#      lambda x: x * 4
#      )
#
# for t in c:
#     print(t('abc_'))

# def inc(n):
#     return lambda x: x + n
#
#
# f = inc(42)
# print(f(3))
#
#
# def inc1(n):
#     def wrap(x):
#         return x + n
#
#     return wrap
#
#
# f1 = inc1(42)
# print(f1(3))
#
# inc2 = (lambda n: (lambda x: x + n))
# f2 = inc2(42)
# print(f2(3))
# print(inc2(42)(3))


# print((lambda n: (lambda x: x + n))(42)(3))


# print((lambda a: (lambda b: (lambda c: a + b + c)))(2)(4)(6))

# d = {'b': 15, 'a': 10, 'c': 24}
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1], reverse=True)
# print(lst)
#
# dict1 = dict(lst)
# print(dict1)

# players = [{'name': 'Антон', 'last name': 'Бирюков', 'raiting': 9},
#      {'name': 'Алексей', 'last name': 'Бодня', 'raiting': 10},
#      {'name': 'Федор', 'last name': 'Сидоров', 'raiting': 4},
#      {'name': 'Михаил', 'last name': 'Семенов', 'raiting': 6}
#      ]
# res = sorted(players, key=lambda item: item['last name'])
# print(res)
# players.sort(key=lambda item: item['raiting'], reverse=True)
# print(players)

# a = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# b = a[2](12, 5)
# print(b)

# a = {'one': lambda x: x - 1, 'two': lambda x: abs(x) - 1, 'three': lambda x: x}
# b = [-3, 10, 0, 5]
# for i in b:
#     if i < 0:
#         print(a['two'](i))
#     elif i > 0:
#         print(a['one'](i))
#     else:
#         print(a['three'](i))

# a = {
#     1: (lambda: print('Понедельник')),
#     2: (lambda: print('Вторник')),
#     3: (lambda: print('Среда')),
#     4: (lambda: print('Четверг')),
#     5: (lambda: print('Пятница')),
#     6: (lambda: print('Суббота')),
#     7: (lambda: print('Воскресенье'))
# }
#
# a[4]()

# maximum = (lambda a, b: a if a > b else b)
# print(maximum(15, 23))

# minimum = (lambda a, b, c: a if a < b else b if b < c else c)
# print(minimum(12, 15, 5))
#
# minimun = (lambda a, b, c: a if a < b else b if b < c else c if c < a else a)
# print(minimun(12, 15, 5))
#
# maximum = (lambda a, b, c: a if (a < b and a < c) else (b if b < a and b < c else c))
# print(maximum(12, 15, 5))


# Функция map()

# def multiple(t):
#     return t * 2


# lst = [2, 8, 12, -5, -10]
# print(list(map(multiple, lst)))
# print(list(map(lambda t: t * 2, lst)))


# t = 2.88, -1.75, 100.55
#
# print(tuple(map(lambda x: int(x), t)))
# print(list(map(lambda x: str(x), t)))
#
# a = ['2.88', '-1.75', '100.55']
# print(list(map(float, a)))
#
# print(list(map(int, map(float, a))))

# areas = [3.58212476, 5.5494955, 7.26778102369, 56.215466552, 9.01254358, 32.7755235]
# print(list(map(round, areas, (1, 9))))

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# lst = dict(map(lambda x, y: (x, y), st, num))
# print(lst)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)


# filter(func, iterable)

# t = ('abcd', 'abc', 'cdefg', 'def', 'ghi')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)
#
# b = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
# res = list(filter(lambda s: s > 70, b))
# print(res)


# lst = [randint(1, 41) for i in range(10)]
# print(lst)
# res = list(filter(lambda s: 10 <= s <= 20, lst))
# print(res)

# lst = [45, 55, 60, 37, 100, 105, 220]
# print(lst)
# res = list(filter(lambda s: s % 15 == 0, lst))
# print(res)


# Декораторы

# def hello():
#     return "Hello, I am func 'hello'"
#
#
# def super_func(func):
#     print("Hello, I am func 'super func'")
#     print(func())
#
#
# super_func(hello)
#
# test = hello
# print(test())

# def my_decorator(func):
#     def wrap():
#         print('Code before')
#         func()
#         print("Code after")
#     return wrap
#
#
# def func_test():
#     print("Hello, I am func 'super func'")
#
#
# test = my_decorator(func_test)
# test()

# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print('Code before')
#         func()
#         print("Code after")
#     return wrap
#
#
# @my_decorator
# def func_test():  # декорируемая функция
#     print("Hello, I am func 'super func'")
#
#
# func_test()


# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap
#
#
# @italic
# @bold
# def hello():
#     return "text"
#
#
# print(hello())

# def cnt(fn):
#     count = 0
#
#     def wrap():
#         nonlocal count
#         count += 1
#         fn()
#         print("Вызов функции: ", count)
#
#     return wrap
#
#
# @cnt
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()

# def args_decorator(fn):
#     def wrap(arg1, arg2):
#         print("*" * 50)
#         fn(arg1, arg2)
#         print("*" * 50)
#
#     return wrap
#
# @args_decorator
# def print_full_name(first, last):
#     print("Меня зовут", first, last)
#
#
# print_full_name("Ирина", "Лаврова")


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("*" * 50)
#         fn(*args, **kwargs)
#         print("args", args)
#         print("kwargs", kwargs)
#         print("*" * 50)
#
#     return wrap
#
#
# @args_decorator
# def print_full_name(a, b, c, study='Python'):
#     print(a, b, c, "изучают", study, end="\n")
#
#
# print_full_name("Ирина", "Борис", "Светлана", study="JavaScript")
# print()
# print_full_name("Владимир", "Екатерина", "Виктор")

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, "=", end=" ")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма:", "+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность:", "-")
# def sub(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# sub(5, 2)

# def multiply(n):
#     def return_multiply(fn):
#         def wrap(num):
#
#             print("Результат:", fn(num) * n)
#         return wrap
#     return return_multiply
#
#
# @multiply(3)
# def return_num(num):
#     return num * 2
#
#
# return_num(5)


# def typed(*args, **kwargs):
#     def wrapper(fn):
#         def wrap(*f_args, **f_kwargs):
#             for i in range(len(args)):
#                 if type(f_args[i]) != args[i]:
#                     raise TypeError("Некорректный тип данных")
#             for k in kwargs:
#                 if type(f_kwargs[k]) != kwargs[k]:
#                     raise TypeError("Некорректный тип данных")
#             return fn(*f_args, **f_kwargs)
#         return wrap
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, z=int)
# def typed_fn3(x, y, z="Hello! "):
#     return (x + y) * z


# print(typed_fn(3, 4, 5))
# print(typed_fn(3, 4, "Doge"))
# print(typed_fn2("Hello, ", "World", "!"))
# print(typed_fn3("Hello,", "World___", z=5))
# print(typed_fn3("Hello, ", "World", z="!!!"))

# def decor(tx=None, decor_text=''):
#     def wrapper(fn):
#         def wrap(*args):
#             print(decor_text, end="")
#             fn(*args)
#         return wrap
#
#     if tx is None:
#         return wrapper
#     else:
#         return wrapper(tx)
#
#
# @decor
# def hello_world2(text):
#     print(text)
#
#
# @decor(decor_text="Hello, ")
# def hello_world(text):
#     print(text)
#
#
# hello_world2("Hi!")
# hello_world("world!")


# print(int('100', 2))
# print(int('100', 8))
# print(int('100', 16))
# print(int('100', 10))

# print(bin(18))
# print(oct(18))
# print(hex(18))
#
# print(0b100 + 51)
# print(0o20)
# print(0x11)

# q = "Pyt"
# w = "hon"
# e = q + w
# print(e)
# print(e * 3)
# print('y' in e)
# print(e[::-1])
# e = e[0:3] + 't' + e[4:]
# print(e)

# def change_char(s, c_old, c_new):
#     s2 = ""
#     for i in s:
#         if i != c_old:
#             s2 += i
#         else:
#             s2 += c_new
#
#     return s2
#
# st = "Я изучаю Nuthon. Мне нравится Nuthon. Nuthon очень интересный язык программирования."
# st2 = change_char(st, 'N', '')
# print("st1 =", st)
# print("st2 =", st2)


# print(u"Привет")
# print(r"C:\file.txt")  # сырые строки
# print(r"C:\file.txt\\"[:-1])
# print(r"C:\file.txt" + "\\")
# print("C:\\file.txt\\")


# name = "Дмитрий"
# age = 25
# print("Меня зовут " + name + ". Мне " + str(age) + " лет")
# print("Меня зовут ", name, ". Мне ", age, " лет", sep="")
# print(f"Меня зовут {name}. Мне {age} лет")
#
# print(f"{round(2.3654236, 2)}")
# print(f"{2.3654236:.2f}")

# x = 10
# y = 5
# print(f"{x} * {y} / 2 = {int(x * y / 2)}")

# d = 74
# print(f"{{{{{d}}}}}")

# dir_name = 'doc'
# file_name = 'data.txt'
# print(fr'home\{dir_name}\{file_name}')


# s = """<div>
#     <a href="#">content</a>
# </div>
# """
# print(s)
#
# s1 = '''<div>
#     <a href="#">content</a>
# </div>
# '''
# print(s1)

# def square(n):
#     """Принимает число n, возвращает квадрат числа n"""
#     return n ** 2
#
#
# print(square(5))
# print(square.__doc__)
# print(min.__doc__)

# import math
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра.
#     :param h: положительное число, высота цилиндра.
#     :return: положительное число, площадь цилиндра.
#     """
#     return 2 * math.pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)

# print(ord('a'))
# print(ord('а'))

# while True:
#     n = input("-> ")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break


# my_str = "Testeee string for me"
# arr = [ord(x) for x in my_str]
# print(arr)
# arr = [int(sum(arr) / len(arr))] + arr
# print(arr)
# arr += [x for x in [ord(x) for x in (input("-> "))[:3]] if x not in arr]
# print(arr)
# if arr[-1] in arr[:-1]:
#     print(arr.count(arr[-1]) - 1)
# arr.sort(reverse=True)
# print(arr)

# print(chr(97))
# print(chr(35))
# print(chr(8364))

# a = 122
# b = 97
# while b <= a:
#     print(chr(b), end=" ")
#     b += 1
# print()
#
# a = 122
# b = 97
# while a >= b:
#     print(chr(a), end=" ")
#     a -= 1

# a = 97
# b = 122
# if a >= b:
#     for i in range(b, a + 1):
#         print(chr(i), end=" ")
# else:
#     for i in range(a, b + 1):
#         print(chr(i), end=" ")

# a, b = 122, 97
# if b < a:
#     a, b = b, a
# while a <= b:
#     print(chr(a) + " ", end="")
#     a += 1

# print('apple' == 'Apple')
# print(ord('a'))
# print(ord('A'))

from random import randint

# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126


# def random_password():
#     random_length = randint(SHORTEST, LONGEST)
#     res = ""
#     for i in range(random_length):
#         random_char = chr(randint(MIN_ASCII, MAX_ASCII))
#         res += random_char
#     return res
#
#
# print("Ваш случайны пароль: ", random_password())

# print(dir(str))

# s = "hello, WORLD! I am learning Python."
# print(s.capitalize())  # Hello, world! i am learning python.
# print(s.lower())  # hello, world! i am learning python.
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.
#
# print(s.count("l"[:], 3))  # подсчитывает количество подстроки в строру
# print(s.find("Python"))  # ищет в строке заданную подстроку, если она найдена, то возвращает индекс первого
# # вхождения подстроки, если нет - то возвращает "-1"

# a = "один два"
# b = a[:a.find(" ")]
# c = a[a.find(" ") + 1:]
# print(c, b)

# a = 'ab12c56p7dq'
# digits = []
# # for i in a:
# #     if i in '0123456789':
# #         digits.append(int(i))
# # print(digits)
#
# for i in a:
#     if '0123456789'.find(i) != -1:
#         digits.append(int(i))
# print(digits)

# print(s)
# print(s.index("Python"))  # ищет в строке заданную подстроку, если она найдена, то возвращает индекс первого
# # вхождения подстроки, если нет - то возвращает исключение ValueError

# print(s.rfind('l'))
# print(s.rindex('l'))

# a = 'I am learning Python. hello, WORLD!'
# first = a.find('h')
# last = a.rfind('h')+1
# print(a[:a.find('h')] + a[a.rfind('h')+1:])

# print('abc123'.isalnum())  # определяет состоит ли строка из букв или цифр
# print('ABCabc'.isalpha())  # определяет состоит ли строка из букв
# print('123'.isdigit())  # определяет состоит ли строка из цифр
# print('abc2!'.islower())  # определяет состоит ли строка из строчных букв
# print('ФИС'.isupper())  # определяет состоит ли строка из заглавных букв

# print('py'.center(100, '-'))

# print("             py".lstrip())
# print("py             ".rstrip())
# print("              py             ".strip())
#
# print("http:/www.python.org".lstrip('/:pths'))
# print('py.$$$;'.rstrip(';$.'))
# print("https:/www.python.org".lstrip('htps:/').rstrip('org.'))

# st = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(st)
# print(st.replace("Nython", "Python"))  # заменяет вхождение подстроки в строке


# s = "="
# seq = ("a", "b", "c")
# print(s.join(seq))
#
# print("..".join(['1', '2']))
# print(":".join("Hello"))

# print("Строка разделена пробелами".split())
# print("Строка_разделена_пробелами".split("_"))
# print("Строка_разделена_пробелами".split("а"))
#
# print("www.python.org".split(".", 1))

# a = list(map(int, input("-> ").split()))
# print(a)
# a = input("Введите ФИО: ").split()
# print(a)
# print(a[0], " ", a[1][0], ".", a[2][0], ".", sep="")

# s = input('ФИО: ').split()
# print(f'{s[0]} {s[1][0]}.{s[2][0]}.')


# print("www.python.org.ru".rsplit(".", 2))
#
# print("www....python....org...ru".split("."))


# a = input("-> ").split()
# print(a)
# print("*".join(a))

# регулярные выражения
import re

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта.1_2 3"
# reg = r' '
# print(s.find(reg))
# print(re.findall(reg, s))  # ['я', 'я'] возвращает список, содержащий совпадения
# print(re.findall("21", s))
# print(re.search(reg, s))  # местоположение первого совпадения объекта
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())

# print(re.match(reg, s))

# print(re.split(reg, s))  # возвращает список, в котором строка разбита по шаблону

# print(re.sub(reg, '!', s, 1))
#
# print(re.findall(reg, s))

# Повторения
# + - от 1 до бесконечности
# * - от 0 до бесконечности
# ? - 0 или 1

# s2 = 'Час в 24-часовом формате от 00 до 23. 2021-06-15Т21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09.'
# pat = r'[0-2][0-9]:[0-5][0-9]'
# print(re.findall(pat, s2))

# s1 = "Цифры: 7, +17, -42, 0013, 0.337653123"
# pattern = r'[+-]?\d+[.\d]*'
# print(re.findall(pattern, s1))

# s1 = "05-03-1987 # Дата рождения"
# print("Дата рождения:", re.sub(r'#.*', '', s1))
# print("Дата рождения:", re.findall(reg, re.sub(r'#.*', '', s1)))

# Дата рождения:  05.03.1987

# s1 = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831 12335994623"
# s1 = "author=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831 12335994623"
# print(s1)
# pattern = r'\w+\s*=\s*\w+\s*[.\w]*'
# print(re.findall(pattern, s1))

# s1 = '12 сентября 2021 года 64521231354'
# reg1 = r'[а-я]{2,4}'
# print(re.findall(reg1, s1))

# test = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 74994564578'
# print(re.findall(r'\+?7\d{10}', test))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта.1_2 3"
# reg = r'^\w+\s\w+'
# reg = r'\w+\s\w+$'
# print(re.findall(reg, s))


# def login(a):
#     return re.findall(r'^[\w!@#$-]{8,25}', a)
#
#
# print(login('admin_admin'))
# print(login('*admin_admin'))

# print(re.findall(r'\w+', '12 + й'))
# print(re.findall(r'\w+', '12 + й', flags=re.ASCII))
# print(re.findall(r'[я]', 'Я я', re.IGNORECASE))

# text = """
# one
# two
# """
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))
# print(re.findall(r'one.\w+', text, re.DOTALL))

# print(re.findall("""
# [A-z.-]+
# @
# [a-z_.-]+
# """, 'test@mail.ru', re.VERBOSE))

# text = 'hello world'
# print((re.findall(r'\w+', text, re.DEBUG)))

# text = """Python,
# python,
# PYTHON"""
# reg = "(?mi)^python"
# print(re.findall(reg, text))  # flags=re.IGNORECASE | re.MULTILINE

# s = "123456@i.ru, 123_456@ru.name.ru, Llogin@i.ru, логин-1@i.ru, login.3@i.ru, login.3-63@i.ru, 1login@ru.name.ru."
# reg = r'[\w.-]+@[\w.]+[\w]{2,3}'
#
# print(re.findall(reg, s))

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.+?>", text))

# {m,n}?, {,n}?, {m,}?
#
# t = "2324 786 22 4569"
# reg = r'\d{,2}'
# print(re.findall(reg, t))

# s = "<p>Изображение <img alt='картинка' src='bg.jpg'> - фон страницы</p>"
# reg = r'<img\s+[^>]*?src\s*=\s*[^>]+>'
# reg = r'<img[^>]*>'
# print(re.findall(reg, s))  # <img src='bg.jpg'>

# s = "Python (в русском языке встречаются названия питон[16] или пайтон[17]) - высокоуровненый язык программирования " \
#     "общего назначения с динамической строгой типизацией и автоматическим управлением памятью[18][19]."
# reg = r'\[\d+]'
# print(re.findall(reg, s))

# s = 'Петр и Ольга отлично учатся!'
# reg = 'Петр|Виталий|Ольга'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0, double = 8.0f"
# reg = r"(?:int|double)\s*=\s*\d+[.\w+]*"
# reg = r"int\s*=\s*\d+[.\w+]*|double\s*=\s*\d+[.\w+]*"
# print(re.findall(reg, s))

# 192.168.255.255
# s = '127.0.0.1'
# reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'
# reg = r'(?:\d{1,3}.){3}(?:\d{1,3})'
# print(re.findall(reg, s))

# s = "Word2016, PS6, AI5"
# reg = r'(([A-z]+)(\d*))'
# print(re.findall(reg, s))

# s = "5 + 7*2 - 4"
# reg = r'\s*[+*-]\s*'  # ['5', '7', '2', '4']
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))

# s = "Я ищу совпадения в 2023 году. И я их найду в 2 счёта."
# reg = r'([0-9]+)\s(\D+)'
# print(re.search(reg, s).group())
# m = re.search(reg, s)
# print(m[1])
# print(m[2])

print()




