def countLettersA(path = ''):
    if (path != ''):
        _file = open(path, 'r')
        _returned = 0
        for line in _file:
            for word in line.split(' '):
                if (word[0].lower() == 'а'):
                    _returned += 1
        _file.close()
        return _returned
    else:
        return 'Путь до файла пустой!'

print(countLettersA(input('Введите путь до файла: ')))