_pseudoDB = [
    {
        'name': 'Табуретка',
        'price': 2500.0,
        'count': 100
    },
    {
        'name': 'Стол',
        'price': 3500.0,
        'count': 50
    },
    {
        'name': 'Стул',
        'price': 900.0,
        'count': 100
    },
    {
        'name': 'Прихожая',
        'price': 10000.0,
        'count': 10
    },
    {
        'name': 'Столешница',
        'price': 900.0,
        'count': 100
    },
    {
        'name': 'Гардероб',
        'price': 15000.0,
        'count': 100
    },
    {
        'name': 'Шкаф-купе',
        'price': 150000.0,
        'count': 5
    },
    {
        'name': 'Ковер',
        'price': 10000.0,
        'count': 100
    },
    {
        'name': 'Раковина',
        'price': 9999.0,
        'count': 100
    },
    {
        'name': 'Туалет',
        'price': 1488.0,
        'count': 100
    }
]

for piece in _pseudoDB:
    print(piece)

print('Внимание! У товаров нет производителей! Заполните!')
for piece in _pseudoDB:
    piece.update({'manufacturer': input('Введите производителя для товара "' + piece.get('name') + '": ')})
for piece in _pseudoDB:
    print(piece)

_average = 0
_sum = 0
for piece in _pseudoDB:
    _sum += piece.get('price')
_average = _sum / len(_pseudoDB)
print('Средня стоимость всех товаров: ' + str(_average))

_countOfMoreThanAvarage = 0
for piece in _pseudoDB:
    if (piece.get('price') > _average):
        _countOfMoreThanAvarage += 1
print('Товаров с ценой больше, чем средняя стоимость всех товаров: ' + str(_countOfMoreThanAvarage))

_sorted = {}
for i in range(0, len(_pseudoDB)):
    _sorted.update({i: _pseudoDB[i].get('count')})
for key in sorted(_sorted, key = _sorted.get):
    print(_pseudoDB[key])