def paragraphs(_path):
    _file = open(_path, 'r')
    _subStr = ''
    _list = []
    for line in _file:
        if (line[0] == ' '):
            if (len(_subStr) != 0):
                _list.append(_subStr)
            _subStr = line + '\n'
        else:
            _subStr += line + '\n'
    _list.append(_subStr)
    _file.close()
    return _list

par = paragraphs(input('Введите путь до файла: '))
for piece in par:
    print(piece)