import math
a = float(input("Введите переменную a: "))
b = float(input("Введите переменную b: "))
print('y = ', math.tan(math.fabs(b - a)) / math.sqrt(a ** 2 + b ** 2))