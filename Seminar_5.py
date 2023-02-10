# Задача 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#
# Требуется найти N-е число Фибоначчи.
"""
def fibonacci(num):
    if num == 0:
        fib = 0
    elif num == 1:
        fib = 1
    else:
        fib = fibonacci(num - 1) + fibonacci(num - 2)
    return fib


n = int(input('Введите число: '))
for i in range(n):
    print(fibonacci(i))
"""
# вариант от преподователя
"""
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input('Введите число: '))
for i in range(n):
    print(fibonacci(i))
"""
# Задача 2. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
"""
n = int(input('Введите кол-во оценок: '))
list_1 = []
list_1 = [int(input('Введите оценку: '))for i in range(n)]
temp = int
min_mark = 5
max_mark = 0

for i in list_1:
    if i < min_mark:
        min_mark = i
    if i > max_mark:
        max_mark = i
print(min_mark, max_mark)
print(list_1)

for i in range(len(list_1)):
    if list_1[i] == max_mark:
        list_1[i] = min_mark
print(list_1)
"""

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
"""
def easy(n):
    for i in range(2, n - 1):
        if n % i == 0:
            return 'не простое'
        return 'простое'


print(easy(int(input('Введите число: '))))
"""
# вариант от преподователя
"""
def simple(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 'не простое'
        return 'простое'

print(simple(int(input('Введите число: '))))
"""