import random, math

_list = []
_subList = []
average = 0

for i in range(25):
    _list.append(random.randint(-10, 10))
average = sum(_list) / len(_list)

for value in _list:
    if (value < average):
        _subList.append(value)

print('Сгенерированный список: ', _list)
print('Среднее значение: ', average)
print('Элементы списка меньше среднего значения в порядке возрастания: ', sorted(_subList, reverse = False))