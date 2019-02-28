import math

a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))
c = float(input('Введите значение c: '))
d = float(input('Введите значение d: '))

y = math.cos((min(d, b, c) + max(c, a)) / (math.sqrt(math.fabs(min(a, b, d) - a))))

print('Значение y равно: ', y)