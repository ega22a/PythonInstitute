def nod(m, n):
    while m != 0:
        m, n = n % m, m
    return n

a = int(input('Введите a: '))
b = int(input('Введите b: '))

nok = a * b / nod(a, b)

print('nok = ', nok)