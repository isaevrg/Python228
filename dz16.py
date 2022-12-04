from random import *


def func1(fn):
    def wrap(arg1, arg2, arg3, arg4):
        s = (arg1 + arg2 + arg3 + arg4) / 4
        fn(arg1, arg2, arg3, arg4)
        print("Среднее арифметическое чисел ", arg1, ", ", arg2, ", ", arg3, ", ", arg4, " = ",  s, sep="")

    return wrap


@func1
def func2(a, b, c, d):
    sum1 = a + b + c + d
    print("Сумма чисел ", a, ", ", b, ", ", c, ", ", d, " = ", sum1, sep="")


func2(2, 3, 3, 4)

























