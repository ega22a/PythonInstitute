import math

i = -5.0
while (i <= 5.0):
    print('x = ', i, '; y = ', math.cos(i ** 2 - math.pi * i))
    i += 0.2