import random

arr = []
negArr = []
posArr = []
sumOfPos = 0

for i in range(0, 20):
    arr.append(random.randrange(-9, 9))
    if (arr[i] >= 0):
        posArr.append(arr[i])
        sumOfPos += i
    else:
        negArr.append(arr[i])

print('Полный список: ', arr)
print('Только отрцательные числа: ', negArr)
print('Только положительные числа и ноль (если имеется): ', posArr)
print('Сумма индексов всех положительных чисел списка: ', sumOfPos)