# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.
import random
def sequence (a,b):
    numbers_list = []
    for i in range (1,a + 1):
        numbers_list.append(random.randrange(b))
    return numbers_list

num_list = sequence(10,9)
print(f'{num_list} исходный список')
num_set = list(set(num_list))
print(num_set)
for i in range(0,len(num_set)):
    x = num_set[i]
    num_list.remove(x)
print(f'{num_list} повторяющиеся элементы')
result = set(num_set).difference(set(num_list))
print(f'{result} итог')