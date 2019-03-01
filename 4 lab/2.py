import math

m = int(input('Введите значение переменной m: '))
n = int(input('Введите значение переменной n: '))

combination = math.factorial(n) / (math.factorial(m) * math.factorial(n - m))

print('Соотношение равно: ', combination)