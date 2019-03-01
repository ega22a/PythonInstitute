import math, random

arr = []
average = 0.0
sumOfMoreThanAverage = 0

for i in range(0, 20):
    arr.append(random.randrange(5, 30))
average = sum(arr) / 20
for i in range(0, 20):
    if (arr[i] % 2 == 0 and arr[i] > average):
        sumOfMoreThanAverage += 1
print('Весь список: ', arr)
print('Среднее значение: ', average)
print('Сумма чётных чисел списка, больше среднего значения: ', sumOfMoreThanAverage)