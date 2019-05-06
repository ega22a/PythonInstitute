def fileComparsion(_first, _second):
    _f1 = open(_first, 'r')
    _f2 = open(_second, 'r')
    if (_f1.read() == _f2.read()):
        return True
    else:
        return False
    _f1.close()
    _f2.close()

isEqual = fileComparsion(input('Введите путь до первого файла: '), input('Введите путь до второго файла: '))
if (isEqual):
    print('Файлы равны')
else:
    print('Файлы не равны')