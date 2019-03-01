import random

def lastNumeral(_number):
    return _number % 10

arr = []
sumOfLastNumeral = 0
for i in range(0, 10):
    arr.append(random.randrange(0, 1000000))
    sumOfLastNumeral += lastNumeral(arr[i])

print('Список случайных чисел: ', arr)
print('Сумма последних цифр каждого элемента списка: ', sumOfLastNumeral)
