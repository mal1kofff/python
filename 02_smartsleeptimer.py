"""Коля каждый день ложится спать ровно в полночь и недавно узнал, что оптимальное время для его
сна составляет X минут. Коля хочет поставить себе будильник так, чтобы он прозвенел ровно через X минут
после полуночи, однако для этого необходимоуказать время сигнала в формате часы, минуты.
Помогите Коле определить, на какое время завести будильник."""
time = int(input())
print(time//60)
print(time%60)
