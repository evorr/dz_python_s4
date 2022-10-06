# Вычислить число c заданной точностью d
# 	Пример:
# 	при d = 0.001, π = 3.141        10^-1 <= d <= 10^-10

import math
print(math.pi)
for i in range (1,11):
    print(round(math.pi,i),end = ";  ") # тут округляется
print()
for i in range (1,11):
    pi = int(math.pi * (10**i))/10**i  # тут просто отбрасывается
    print(pi, end = ";  ")
