def nod(m, n):
    while m != 0:
        m, n = n % m, m
    return n

def nok(m, n):
    return (m * n) / nod(m, n)

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))

print('Наибольшее общее кратное = ', nok(a, nok(b, c)))