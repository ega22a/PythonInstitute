def fileToList(_path):
    _file = open(_path, 'r')
    _returned = []
    for line in _file:
        _subList = []
        for word in line.split(' '):
            _subList.append(word)
        _returned.append(_subList)
    _file.close()
    return _returned
_list = fileToList(input('Введите путь до файла: '))
for piece in _list:
    print(piece)