import re
from random import *


def login(a):
    return re.findall(r'^[A-z0-9_@-]{6,18}$', password)


password = input("Задайте пароль: ")
print(login(password))






