import math

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

d = b ** 2 - (4 * a * c)

if (d > 0):
    print('Первый корень: ', (-b + math.sqrt(d)) / (2 * a))
    print('Первый корень: ', (-b - math.sqrt(d)) / (2 * a))
elif (d == 0):
    print('Единственный корень: ', (-b) / (2 * a))
elif (d < 0):
    print('Действительных корней нет.')