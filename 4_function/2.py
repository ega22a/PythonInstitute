import random

def replace(_list, _key):
    _returnedList = []
    _returnedList.append(_list[_key - 1])
    for i in range(0, len(_list)):
        if (i != _key -1):
            _returnedList.append(_list[i])
    return _returnedList

newList = []
key = 0
for i in range(0, 10):
    secList = []
    for j in range(0, 10):
        secList.append(random.randint(0, 1000))
    newList.append(secList)
print('Созданный список:')
for i in range(0, 10):
    print(i + 1, ':', newList[i])
key = int(input('Какой список вы желаете передвинуть на первое место: '))
while (key < 1 or key > 10):
    print('Вы можете ввести число от одного до десяти!')
    key = int(input('Какой список вы желаете передвинуть на первое место: '))
print('Ваш новый список:')
l = replace(newList, key)
for i in range(0, 10):
    print(i + 1, ':', l[i])