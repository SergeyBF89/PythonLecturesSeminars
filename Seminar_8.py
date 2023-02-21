# -----------------------------------Работа с файлами-----------------------------------------
# ------------Открыть файл---------------
# with open('seminar_8.txt', 'r', encoding='utf-8') as file:
#     text = file.read().splitlines()
#     print(text)
#
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line.strip())

# --------------Запись и создание файла-------------
# with open('filetest.txt', 'w', encoding='utf-8') as file:
#     some_list = ['привет', 'пока']
#     for word in some_list:
#         file.write(word + '\n')

# Задача 1. Создать файл и посчитать ко-во буквы, которую введи с клавиатуры.

"""
with open('task_1.txt', 'r', encoding='utf-8') as file:
    lit = input()
    text = file.read()
    count = 0
    for el in text:
        if el == lit:
            count += 1
    print(count)
"""
"""
with open('task_1.txt', 'r', encoding='utf-8') as file:
    letter = input()
    print(file.read().count(letter))
"""

# Задача 2. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
"""
from random import randint
n = int(input('Введите кол-во элементов в списке: '))
some_list = [randint(-n, n) for _ in range(n)]
print(some_list)
with open('task_2.txt', 'w',encoding='utf-8') as file:
    for _ in range(randint(1, n)):
        file.write(str(randint(0, n - 1)) + '\n')

with open('task_2.txt', 'r',encoding='utf-8') as file:
    mult = 1
    for i in file.read().splitlines():
        mult *= some_list[int(i)]
print(mult)
"""


