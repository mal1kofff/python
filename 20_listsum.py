"""Напишите программу, на вход которой подается одна строка с целыми числами.
Программа должна вывести сумму этих чисел.
"""

a = [int(i) for i in input().split()]
print(sum(a))
