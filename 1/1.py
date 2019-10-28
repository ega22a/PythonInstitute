from math import sqrt
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if (a != 0):
    _dis = b ** 2 - 4 * a * c
    if (_dis > 0):
        print("x1 = ", (-b + sqrt(_dis)) / (2 * a))
        print("x1 = ", (-b - sqrt(_dis)) / (2 * a))
    elif (_dis == 0):
        print("x = ", (-b) / (2 * a))
    elif (_dis < 0):
        print("Действительных корней нет.")
else:
    print("Переменная a не может быть равна нулю!")