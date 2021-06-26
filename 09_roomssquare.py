"""Жители страны Малевии часто экспериментируют с планировкой комнат.
Комнаты бывают треугольные, прямоугольные и круглые. Чтобы быстро вычислять жилплощадь,
требуется написать программу, на вход которой подаётся тип фигуры комнаты и соответствующие параметры,
которая бы выводила площадь получившейся комнаты.
Для числа π в стране Малевии используют значение 3.14."""

figure = input()
if figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
if figure == 'прямоугольник':
    a = int(input())
    b = int(input())
    s = a * b
    print(s)
if figure == 'круг':
    r = int(input())
    s = 3.14 * (r ** 2)
    print(s)

