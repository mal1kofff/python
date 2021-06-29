'''Напишите программу, которая считывает список чисел lst из первой строки и число x
из второй строки, которая выводит все позиции, на которых встречается число x в переданном списке lst.
'''

list = [int(i) for i in input().split()]
x = int(input())
for i in range(len(list)):
    if x == list[i]:
        print(i, end=' ')
if x not in list:
        print('Отсутствует')