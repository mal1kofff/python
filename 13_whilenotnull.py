"""Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке,
и после первого введенного нуля выводит сумму полученных на вход чисел."""

i = 1
s = 0
while i!=0:
    i = int(input())
    s += i
print(s)
