# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

f = open('file_5_1.txt','r')
first = f.read()
print(first)
f_list = first.split('x^2')
ff = f_list[1].split('x')

s = open('file_5_2.txt','r')
second = s.read()
print(second)
s_list = second.split('x^2')
ss = s_list[1].split('x')

a = int(f_list[0]) + int(s_list[0])
b = int(ff[0]) + int(ss[0])
c = int(ff[1]) + int(ss[1])
print(a,b,c)

with open('file_5_3.txt','w') as t:
    t.write(f'{a}x^2+{b}x+{c}')
    t.close()