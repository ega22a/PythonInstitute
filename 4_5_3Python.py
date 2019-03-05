def sumUntilNotLastPositive(_list):
    trigger = False
    answer = 0
    for value in _list[::-1]:
        if (value > 0):
            trigger = True
        if (trigger):
            answer += value
    return answer
        
            
count = int(input('Введите число, определяющее количество элементов списка: '))
fullList = []
for i in range(0, count):
    fullList.append(float(input('Введите число для элемента списка №' + str(i + 1) + ': ')))
print('Сумма элементов списка (до последнего положительного числа):', sumUntilNotLastPositive(fullList))

