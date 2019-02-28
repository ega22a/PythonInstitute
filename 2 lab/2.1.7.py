import math

start = float(input('Введите начальную скорость:'))
end = float(input('Введите конечную скорость: '))
time = float(input('Введите время прохождения пути (в часах): '))

if (start == end):
    print('Равномерное движение')
elif (start > end):
    print('Равнозамедленное движение')
elif (start < end):
    print('Равноускоренное движение')