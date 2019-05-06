def fileToList(_path):
    _file = open(_path, 'r')
    _returned = []
    for line in _file:
        _returned.append(line)
    _file.close()
    return _returned
_list = fileToList(input('Введите путь до файла: '))
for piece in _list:
    print(piece)