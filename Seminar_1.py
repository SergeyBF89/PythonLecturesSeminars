# Задача 1. Посчитать сумму трех введенных чисел.
"""
n1 = int(input('Введите первое число: '))
n2 = int(input('Введите второе число: '))
n3 = int(input('Введите третье число: '))
sum = n1 + n2 + n3
print(sum)
"""

# Задача 2. Пользователь вводит стороны прямоугольника, вывести его площадь и периметр.
"""
a = float(input('Введите сторону а: '))
b = float(input('Введите сторону b: '))
s = a * b
p = 2 * (a + b)
print(f'плащадь прямоугольника = {s}, периметр прямоугольника = {p}')
"""

# Задача 3. Пользователь вводит два целый числа, вывести меньшее из них.
"""
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
if num1 < num2:
    print(num1)
elif num1 == num2:
    print('Числа равны')
else:
    print(num2)
"""

# Задача 4. Пользователь вводит целое число. Вывести Yes, если это число является четырех значным.
# No, если не является.
# Вариант целочисленный.
"""
number = int(input('Введите число: '))
if 1000 <= number <= 9999 or -9999 <= number <= -1000:
    print('YES')
else:
    print('NO')
"""
# Вариант строковый.
"""
number = input('Введите число: ')
if '-' in number:  # если число будет с минусом
    if len(number) == 5:
        print('YES')
    else:
        print('NO')
else:
    if len(number) == 4:
        print('YES')
    else:
        print('NO')
"""

# Задача 5. Пользователь вводит строки, пока не введет пустую, гарантируется,
# что в строках лежат только цифры.
# Найти сумму введенных чисел, кратных четырем.
"""
summa = 0
while True:
    a = input()
    if a == '':  # проверка на пустую строку
        break
    if int(a) % 4 == 0:  # проверка на кратность
        summa += int(a)  # если совпадает кратность, добовляем число в сумму
print(summa)
"""

# Задача 6. За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
# **Input:**
#
# n = 700
#
# m = 750
#
# **Output:**
#
# 2
"""
n = int(input())
m = int(input())
print((n + m - 1) // n)
"""

# Задача 7. В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
# #
# **Input:**
#
# 20
#
# 21
#
# 22
#
# **Output:**
#
# 32
"""
a = int(input())
b = int(input())
c = int(input())
print((a // 2 + a % 2) + (b // 2 + b % 2) + (c // 2 + c % 2))  # 32
print(math.ceil(a / 2) + math.ceil(b / 2) + math.ceil(c / 2))  # 32 вариант с библиотекой
"""

# Задача 8. Дано натуральное число. Требуется определить, является ли год с данным номером високосным.
# Если год является високосным, то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем, год является високосным, если его номер кратен 4,
# но не кратен 100, а также если он кратен 400.
#
# **Input:**
#
# 2016
#
# **Output:**
#
# YES
"""
year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')
"""
