import random

def sumForArr(_arr, _num):
    a = []
    sumOfNum = 0
    for i in range(0, len(_arr)):
        b = []
        for j in range(0, len(_arr[i])):
            if (_arr[i][j] % 2 == 0 and _arr[i][j] > 0):
                b.append(_arr[i][j])
                sumOfNum += _arr[i][j]
        a.append(sorted(b))
    if (_num == 1):
        return a
    elif (_num == 2):
        return sumOfNum

columns = int(input('Введите количество столбцов: '))
rows = int(input('Введите количество строк: '))
arr = [[0] * columns] * rows

for i in range(0, columns):
    for j in range(0, rows):
        arr[i][j] = random.randint(-20, 20)

print('Введенный список:')
for i in range(0, len(arr)):
    print(arr[i])
print('Четные положительные элементы списка, отсортированные в порядке возрастания:')
for i in range(0, len(sumForArr(arr, 1))):
    print(sumForArr(arr, 1)[i])
print('Сумма элементов: ', sumForArr(arr, 2))