_pseudoDB = []
for i in range(0, 15):
    _pseudoDB.append({
        'name': input('Введите наименование товара: '),
        'price': float(input('Введите цену товара: '))
    })

print('\tТовар\tЦены\t')
for piece in _pseudoDB:
    print('\t' + piece.get('name') + '\t' + str(piece.get('price')))

_max = _pseudoDB[0]
for piece in _pseudoDB:
    if (_max.get('price') < piece.get('price')):
        _max = piece
print('Товар с максимальной ценой: ', _max)

_average = 0
for piece in _pseudoDB:
    _average += piece.get('price')
_average = _average / len(_pseudoDB)
_subDB = []
for piece in _pseudoDB:
    if (piece.get('price') < _average):
        _subDB.append(piece)
for piece in _subDB:
    print(piece)

for i in range(0, 3):
    _pseudoDB.append({
        'name': input('Введите наименование товара: '),
        'price': float(input('Введите цену товара: '))
    })