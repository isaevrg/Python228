from random import *

while True:
    a = int(input("-> "))
    if a != 0:
        b = str(bin(a))
        print(b[2:])
    else:
        break




