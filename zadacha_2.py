# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
import math

n = int(input('Введите натуральное число: '))

def multipliers (num):
    multipliers_list = []
    for i in range (1, math.ceil(num / 2) + 1):
        if num % i == 0:
            multipliers_list.append(i)
            x = int(num / i)
            multipliers_list.append(x)
    return set(multipliers_list)
print(n)
result = multipliers(n)
print(result)