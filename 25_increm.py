"""Напишите программу, которая выводит часть последовательности 1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 ...
(число повторяется столько раз, чему равно). На вход программе передаётся неотрицательное целое число n — столько
элементов последовательности должна отобразить программа. На выходе ожидается последовательность чисел,
записанных через пробел в одну строку.
"""


n = int(input())
a = []
for i in range(n+1):
    a += [i] * i
print(*a[:n])