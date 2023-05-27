# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X
#
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5

import random
from random import randint

my_list = []
quantity = int(input('Введите колличество элементов в списке: '))
number = int(input('Введите число для поиска близких по величине элементов к числу: '))
for _ in range(quantity):
    my_list.append(random.randint(0, 10))
print(my_list)
my_list.append(number)
my_list = sorted(my_list)
position = my_list.index(number)
if position == len(my_list) - 1:
    print(f'самый близкий по величине элемент к заданному числу {number} это {my_list[position - 1]}')
elif position == 0:
    print(f'самый близкий по величине элемент к заданному числу {number} это {my_list[position + 1]}')
elif my_list[position] - my_list[position - 1] < my_list[position + 1] - my_list[position]:
    print(f'самый близкий по величине элемент к заданному числу {number} это {my_list[position - 1]}')
elif my_list[position] - my_list[position - 1] > my_list[position + 1] - my_list[position]:
    print(f'самый близкий по величине элемент к заданному числу {number} это {my_list[position + 1]}')
elif my_list[position] - my_list[position - 1] == my_list[position + 1] - my_list[position]:
    print(
        f'самый близкий по величине элемент к заданному числу {number} это {my_list[position - 1], my_list[position + 1]}')
