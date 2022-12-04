from random import *

# 1 задание
print((lambda a: (lambda b: (lambda c: a * b * c)))(2)(5)(5))


# 2 задание
students = [{'name': 'Jennifer', 'final': 95},
            {'name': 'David', 'final': 92},
            {'name': 'Nikolas', 'final': 98}
            ]
res1 = sorted(students, key=lambda item: item['name'])
print(res1)
res2 = sorted(students, key=lambda item: item['final'], reverse=True)
print(res2)

# 3 задание
students = [{'name': 'Jennifer', 'final': 95},
            {'name': 'David', 'final': 92},
            {'name': 'Nikolas', 'final': 98}
            ]

res1 = max(students, key=lambda item: item['name'])
print(res1)
res2 = min(students, key=lambda item: item['final'])
print(res2)

# 4 задание
nums = [3, 5, 7, 3, 9, 5, 7, 2]
print(nums)
res1 = (lambda i: i ** 2)
res2 = (lambda i: i ** 3)
print(list(map(res1, nums)))
print(list(map(res2, nums)))






