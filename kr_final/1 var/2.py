import random
_list = []
_subList = []
for i in range(0, 20):
    _list.append(random.randint(-5, 12))
for value in _list:
    if (value % 2 == 0):
        _subList.append(value)
print('Сгенерированный список:')
print(_list)
print('Только четные элементы, сортированные по возрастанию:')
print(sorted(_subList))