"""Напишите программу, на вход которой подаётся список чисел одной строкой.
Программа должна для каждого элемента этого спискавывести сумму двух его соседей. Для элементов списка,
являющихся крайними, одним из соседей считается элемент, находящий на противоположном конце этого списка.
Например, если на вход подаётся список "1 3 5 6 10", то на выход ожидается список "13 6 9 15 7" (без кавычек).

Если на вход пришло только одно число, надо вывести его же."""

a = [int(i) for i in input().split()]
for i in range(len(a)):
    if len(a)==1:
        print(a[0])
        break
    if i == 0:
        print((a[1]+a[-1]), end=' ')
    if 0 < i < (len(a)-1):
        print(a[i-1]+a[i+1], end=' ')
    if i == len(a)-1:
        print(a[i-1]+a[0])
