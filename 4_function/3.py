def split(_string, _delimiter):
    _return = []
    _subString = ''
    for char in _string:
        if (char != _delimiter):
            _subString += char
        else:
            print(_subString)
            _return.append(_subString)
            _subString = ''
    _return.append(_subString)
    return _return

s = split(input('Введите строку: '), input('Введите разделитель: '))
print('Полученный список:', s)