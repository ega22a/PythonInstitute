import math

def lenOfVector(_first, _second, _third):
    return math.sqrt(_first ** 2 + _second ** 2 + _third ** 2)

a1 = float(input('Введите первую координату вектора: '))
a2 = float(input('Введите вторую координату вектора: '))
a3 = float(input('Введите третью координату вектора: '))

print('Длина вектора равна: ', lenOfVector(a1, a2, a3))