import math

a = float(input('Введите переменную a: '))
b = float(input('Введите переменную b: '))
c = float(input('Введите переменную c: '))
d = float(input('Введите переменную d: '))
e = float(input('Введите переменную e: '))

print('y = ', math.sqrt(math.fabs((max(a, d) - max(c, b, e)) / (min(b, c, a, e)))))