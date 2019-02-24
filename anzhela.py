a1 = float(input('Введите a1: '))
b1 = float(input('Введите b1: '))
a2 = float(input('Введите a2: '))
b2 = float(input('Введите b2: '))

if (a1 == a2) and (b1 != b2):
    print('Прямые параллельны.')
if (a1 == a2) and (b1 == b2):
    print('Прямые совпадают.')
if (a1 != a2) and (b1 != b2):
    print('Прямые пересекаются')