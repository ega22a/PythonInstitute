import math

def combination(_first, _second):
    return math.factorial(_second) / (math.factorial(_first) * math.factorial( _second - _first))

m = int(input('Введите значение переменной m: '))
while (m < 0):
    print('Значение переменной не может быть равно меньше нуля!')
    m = int(input('Введите значение переменной m: '))
n = int(input('Введите значение переменной n: '))
while (n < 0):
    print('Значение переменной не может быть равно меньше нуля!')
    n = int(input('Введите значение переменной n: '))
k = int(input('Введите значение переменной k: '))
while (k < 0):
    print('Значение переменной не может быть равно меньше нуля!')
    k = int(input('Введите значение переменной k: '))
while (k > n or m > n):
    print('Переменные k или m не могут больше переменной n!')
    m = int(input('Введите значение переменной m: '))
    n = int(input('Введите значение переменной n: '))
    k = int(input('Введите значение переменной k: '))

output = (combination(m, n) + combination(k, n)) / (combination(m, n) - combination(k, n))

print('Ответ: ', output)