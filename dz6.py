# 1 задание
# k = 0
# lst = []
# s = []
# n = int(input("Введите длину списка: "))
# for num in range(n):
#     x = int(input('Введите элемент списка: '))
#     s.append(x)
#     if x > 0:
#         lst.append(x)
#     if k < x:
#         k = x
# print("Список: ", s)
# print("Новый список, состоящий из положительных элементов: ", lst)
# print("Наибольший элемент списка: ", k)


# 2 задание
# n = [int(input('-> ')) for i in range(int(input('Введите элементы списка: \nn = ')))]
# k = (int(input('Введите индекс: \nk = ')))
# c = (int(input('Введите значение: \nc = ')))
# n.insert(k, c)
# print(n)

# 3 задание
n = [int(input('-> ')) for i in range(int(input('Введите элементы списка: \nn = ')))]
ch = (int(input('Введите число: \nch = ')))
print(n)
if ch in n:
    print("Число присутствует в элементах списка")
else:
    print("Число отсутствует в элементах списка")



