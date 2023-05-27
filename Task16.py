# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# Пример:
# 5
# 1 2 3 4 5
# 3
# -> 1

import random
from random import randint

my_list = []
quantity = int(input('Введите колличество элементов в списке: '))
number = int(input('Введите число для поиска и расчета повторений в списке: '))
for _ in range(quantity):
    my_list.append(random.randint(0,10))
count_1 = my_list.count(number)
print(my_list)
print(f'Число {number} встречаеться в списке {count_1} раз(а)')

# count_2 = 0
# for i in range(len(my_list)):
#     if my_list[i] == number:
#         count_2+=1
# print(f'Число {number} встречаеться в списке {count_2} раз(а)')
