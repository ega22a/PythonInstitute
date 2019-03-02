import random

arr = []
sumOfArr = 0

for i in range(0, 6):
    secArr = []
    for j in range(0, 6):
        secArr.append(random.randrange(9, 40))
    arr.append(secArr)
for i in range(5, -1, -1):
    if (arr[5 - i][i] % 2 == 1):
        sumOfArr += arr[5 - i][i]

print('Созданный список:')
for i in range(0, 6):
    print(arr[i])
print('Сумма нечётных элементов побочной диагонали: ', sumOfArr)