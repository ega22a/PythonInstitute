_pseudoBD = [
    {
        'name': 'Шуба',
        'price': 10000.0
    },
    {
        'name': 'Пальто',
        'price': 5000.0
    },
    {
        'name': 'Куртка',
        'price': 2500.0
    },
    {
        'name': 'Халат',
        'price': 100000.0
    },
    {
        'name': 'Кардиган',
        'price': 250000.0
    },
    {
        'name': 'Ветровка',
        'price': 999999.0
    },
    {
        'name': 'Пуловер',
        'price': 9999999.0
    },
    {
        'name': 'Свитер',
        'price': 1000000.0
    },
    {
        'name': 'Худи',
        'price': 9999.0
    },
    {
        'name': 'Блейзер',
        'price': 50.0
    }
]
for piece in _pseudoBD:
    print(piece)

_average = 0
for piece in _pseudoBD:
    _average += piece.get('price')
_average = _average / len(_pseudoBD)
print('Средняя цена: ', _average)

print('Цены ниже средней:')
for piece in _pseudoBD:
    if (piece.get('price') < _average):
        print(piece)

for i in range(0, 3):
    _pseudoBD.append({
        'name': input('Введите имя товара: '),
        'price': float(input('Введите цену товара: '))
    })
for piece in _pseudoBD:
    print(piece)
