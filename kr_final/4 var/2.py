import random
_list = []
for i in range(0, 16):
    _list.append(random.randint(-5, 10))
print(_list)
_count = []
for firstKey in range(0, 16):
    for secondKey in range(0, 16):
        if (firstKey != secondKey & secondKey > firstKey):
            if (_list[firstKey] == _list[secondKey]):
                _count.append(_list[firstKey])
                break
print('Количество повторяющихся элементов:', len(list(set(_count))))