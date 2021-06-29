"""Напишите программу, которая считывает с клавиатуры два числа a и b, считает и
выводит на консоль среднее арифметическое всех чисел из отрезка [a; b][a;b], которые кратны числу 3."""


a = int(input())
b = int(input())
summa = 0
count = 0
for i in range(a,b+1):
    if i % 3 == 0:
        summa += i
        count +=1
    else: continue
print (summa/count)
