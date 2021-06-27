"""Напишите программу, на вход которой даются четыре числа a, b, c и d,
каждое в своей строке. Программа должна вывести фрагмент таблицы умножения для всех чисел
отрезка [a; b][a;b] на все числа отрезка [c;d][c;d].

Числа a, b, c и d являются натуральными и не превосходят 10"""


a = int(input())
b = int(input())
c = int(input())
d = int(input())
for i in range(c,d+1):
    print('\t', str(i), end='')
print(end='\n')
for i in range(a,b+1):
    print(str(i)+'\t',end='')
    for j in range (c,d+1):
        print(str(j*i),'\t', end='')
    print(end='\n')

