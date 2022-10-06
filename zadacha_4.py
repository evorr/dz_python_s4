# Задана натуральная степень k. Сформировать случайным образом
# список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#
# *Пример:*
#
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

a = random.randrange(0, 100)
str_res = str(a)
k = 5
f = open('file_z4.txt','w')
for i in range (1, k):
    a = random.randrange(0, 100)
    str_res = str(a) + 'x^' + str(i) + '+' + str_res
    f.write(str_res + '=0 \n')
f.close()



