y = int(input())
x = int(input())
if x < 0:
    y = x**2
    print(y)
elif x > 0:
    y = 1/x**2
    print (y)
else: 
    y = 0
    print('Ошибка')
a = int(input())
b = int(input())
if a < b:
    print ('Первое число меньше')
elif a > b:
    print ('Второе число меньше')
else:
    print('Числа равны')
km = int(input())
fut = int(input())

if km > fut * 0.00045:
    print (km)
else:
    print (fut)
y = int(input())
x = int(input())
if x < 1:
    y = a**2 + x**2
    print(y)
elif x > 1:
    y = a**2 - x**2
    print (y)
else: 
    y = 0
    print('Ошибка')
y = int(input())
x = int(input())
if x and y != 0: 
    if x<y:
        c = y/x
        print(c)
    elif y<x:
        c = x/y
        print(c)
else:
    print('ошибка')
km = int(input())
metr = int(input())
if km > metr * 3.6:
    print ('первое значение больше')
elif km < metr * 3.6:
    print ('второе значение больше')
else:
    print('скорости равны')
from math import sqr, pi
a = int(input())
b = int(input())
if a**2 > pi*(r**2):
    print ('У квадрата больше')
else:
    print('У круга')
from math import sqr, pi, cos, sin 
y = int(input())
x = int(input())
if x <= (pi/4):
    y = sin x 
    print(y)
elif x > (pi/4):
    y = cos x
    print (y)
else: 
    print('Ошибка')
ml = int(input())
d = int(input())
if ml > d * 25.4:
    print ('первое значение больше')
elif ml < d * 25.4:
    print ('второе значение больше')
else:
    print('Оба значения равны')
    

m1 = int(input())
V1 = int(input())
m2 = int(input())
V2 = int(input())
p1 = m1/V1
p2 = m2/V2
if p1 > p2:
    print('Первая плотность больше')
elif p1 < p2:
    print('вторая плотность больше')
else:
    print('оба равны')

print(p)

