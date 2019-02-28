import math

y = 0
x = math.pi * (-2) - math.pi / 15

for i in range(0, 61):
    x = x + math.pi / 15
    y = math.cos(x) ** 3
    print('f(', x, ') = ', y, ';')