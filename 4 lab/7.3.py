def splitList(_list):
    zeroArr = []
    numericArr = []
    for index in _list:
        if (index == 0.0):
            zeroArr.append(index)
        else:
            numericArr.append(index)
    return zeroArr + numericArr       

arr = []

countOfArr = int(input('Введите количество элементов списка: '))

for i in range(0, countOfArr):
    arr.append(float(input('Введите число для элемента № ' + str(i + 1) + ': ')))

print('Введённый вами список: ', arr)
print('Изменённый список: ', splitList(arr))