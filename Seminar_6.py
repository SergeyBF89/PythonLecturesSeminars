# Задача 1. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве),
# которых нет во втором массиве. Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива.
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива
"""
array = []
N = int(input())
array_1 = []
M = int(input())
for i in range(N):
    array.append(int(input()))
print(array)

for i in range(M):
    array_1.append(int(input()))
print(array_1)

array_2 = []

for i in array:
    if array_1.count(i) < 1:
        array_2.append(i)
print(array_2)
"""
# Вариант от преподователя
"""
first_list = [int(input('Введите элементы массива: ')) for _ in range(int(input('Введите кол-во элементов массива: ')))]
second_list= [int(input('Введите элементы массива: ')) for _ in range(int(input('Введите кол-во элементов массива: ')))]
for i in first_list:
    if i not in second_list:
        print(i)
"""
# Вариант от преподователя 2 (быстрее работа алгоритма по времени)
"""
first_list = [int(input('Введите элементы массива: ')) for _ in range(int(input('Введите кол-во элементов массива: ')))]
second_list= [int(input('Введите элементы массива: ')) for _ in range(int(input('Введите кол-во элементов массива: ')))]
second_net = set(second_list)
for i in first_list:
    if i not in second_list:
        print(i)
"""

# Задача 2. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов, у которых два соседних и,
# при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.
"""
array = []
N = int(input('Введите кол-во элементов в массиве: '))
for i in range(N):
    array.append(int(input('Введите элементы массива: ')))
print(array)
count = 0
for i in range(2, len(array) - 1):
    if array[i] > array[i - 1] and array[i] > array[i + 1]:
        count += 1
print(count)
"""
# Вариант от преподователя
"""
some_list = [int(input('Введите элементы массива: ')) for _ in range(int(input('Введите кол-во элементов массива: ')))]
count = 0
for i in range(1, len(some_list) - 1):
    if some_list[i - 1] < some_list[i] > some_list[i + 1]:
        count += 1
print(some_list)
print(count)
"""
# Задача 3. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента,
# равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.
"""
array = []
n = int(input('Введите ко-во чисел: '))
for i in range(n):
    array.append(int(input('Введите числа: ')))
print(array)
array_1 = []
count = 0
for i in array:
    if array.count(i) > 1 and i not in array_1:
        count += 1
        array_1.append(i)
print(array_1)
print(count)
"""
# Вариант от преподователя
"""
some_list = []
while True:
    number = int(input('Введите числа: '))
    if number == 0:
        break
    some_list.append(number)

count_dict = {}
for i in some_list:
    if count_dict.get(i):
        count_dict[i] += 1
    else:
        count_dict[i] = 1
print(count_dict)
"""




