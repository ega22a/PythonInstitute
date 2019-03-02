import random

arr = []
secArr = []
sumOfSecArr = 0

for i in range(0, 5):
    subArr = []
    for j in range(0, 6):
        subArr.append(random.randint(-3, 8))
    arr.append(subArr)

secArr = sorted(arr[1] + arr[3])

for i in range(0, len(secArr)):
    sumOfSecArr += secArr[i]

print('Созданный список:')
for i in range(0, len(arr)):
    print(arr[i])
print('Конкатенация второй и предпоследней строки списка: ', secArr)
print('Сумма конкатенации: ', sumOfSecArr)