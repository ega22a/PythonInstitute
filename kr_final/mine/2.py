import random
_list = []
_subList = []
for i in range(0, 25):
    _list.append(random.randint(-10, 10))
print(_list)
for value in _list:
    if (str(value)[-1] == '3'):
        _subList.append(value)
print('Обработанный список:')
print(sorted(_subList))