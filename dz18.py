from random import *

# 1 задание
a = 'Дана ст(рока символов, среди которых есть одна открыв)ающаяся'
print(a[a.find("("):a.find(")") + 1])

# 2 задание
str1 = input("Введите строку: ")
str2 = input("Ее заменяемая строка: ")
str3 = input("Новая подстрока: ")
i = str1.find(str2)
while i != -1:
    l = len(str2)
    str1 = str1[0:i] + str3 + str1[i + l:]
    i = str1.find(str2)
print(str1)

# 3 задание
test = "Ежевика для ежат\n" \
       "Принесли два ежа\n" \
       "Ежевику еле-еле\n" \
       "Ежата возле ели съели."
print(test)
print(test.count("е"))











