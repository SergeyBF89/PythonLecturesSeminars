# Задача 1. Напишите программу, которая принимает на вход строку и отслеживает, сколько раз каждый символ уже встречался.
# Колличество повторов добавляется к символам с помощью постфикса _n
# d g h t r g r h t j h b v f d s d f
# d g h t r g_2 r_2 h_2 t_2 j h_3 b v f d_2 s d_3 f_2
"""
nabor = 'd g h t r g r h t j h b v f d s d f'
print(nabor)
print()
my_list = nabor.split()  # создали список
my_dict = {}  # создали словарь

new_list = []  # новый список

for letter in my_list:
    my_dict[letter] = my_dict.get(letter, 0) + 1
    if my_dict.get(letter) > 1:
        new_list.append(letter + '_' + str(my_dict.get(letter)))  # если буква встречается более одного раза
    else:
        new_list.append(letter)  # если буква встречается один раз
print(' '.join(new_list))
"""

# второй вариант, подходит если мало элементов задано!
"""
str = 'd g h t r g r h t j h b v f d s d f'.split()

for i in range(len(str)):
    k = 1
    for j in range(i + 1, len(str)):
        if str[i] == str[j]:
            k += 1
            str[j] = f'{str[j]}_{k}'
print(*str)
"""

# Задача 2. Пользователь вводит текст(строка). Словом считаеттся последовательность непробельных символов идущих подрят,
# слова разделены одним или большим числом пробелов.
# Определите сколько различных символов содержиться в этой строке.
# sdsgf sdgsg sdgsg d    gfgfht ssr
"""
string = 'sdsgf sdgsg sdgsg d    gfgfht ssr'
my_list = string.split()  # создали список
my_dict = set(my_list)  # переконвертировали в словарь
print(len(my_dict))  # 5
"""

# Вариант от преподователя
"""
text = input('Введите текст: ')
# print(text)
text = text.split()  # разделили по пробелам
# print(text)
text = set(text)  # переводим во множество(уникальные элементы, которые повторяются один раз)
# print(text)
print(f' В вашем тексте {len(text)} уникальных слова')
"""
# короткий вариант решения
"""
text = set(input('введите текст: ').split())
print(f' В вашем тексте {len(text)} уникальных слова')
"""
# вариант через цикл
"""
text = input('Введите текст: ')
text = text.split()
new_list = []
for word in text:
    if not word in new_list:
        new_list.append(word)
print(f' В вашем тексте {len(new_list)} уникальных слова')
"""

# Задача 3. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# [1, 2, 3, 5, 1, 5, 3, 10]
# => [2, 20]
"""
num = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = []
my_dict = {}

for n in num:
    my_dict[n] = my_dict.get(n, 0) + 1
for i in my_dict:
    if my_dict.get(i) == 1:
        new_list.append(i)
print(new_list)
"""

# вариант от преподователя
"""
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
new_list = []

for i in my_list:
    if my_list.count(i) == 1:
        new_list.append(i)
print(my_list)
print()
print(f'Уникальные элементы {new_list}')
"""

# короткий вариант через List comprehension
"""
my_list = [1, 2, 3, 5, 1, 5, 3, 10]
print(f' Уникальные элементы {[i for i in my_list if my_list.count(i) == 1]}')
"""