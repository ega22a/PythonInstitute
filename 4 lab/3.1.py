import math, random

arr = []
average = 0.0
sumOfMoreThanAverage = 0

for i in range(0, 30):
    arr.append(random.randrange(2, 25))
average = sum(arr) / 20
for i in range(0, 20):
    if (arr[i] % 2 == 1 and arr[i] < 15):
        sumOfMoreThanAverage += 1
print('Весь список: ', arr)
print('Среднее значение: ', average)
print('Сумма нечётных чисел списка, меньше 15-ти: ', sumOfMoreThanAverage)