def SumOfLastA(_path = ''):
    if (len(_path) != 0):
        _file = open(_path, 'r')
        _sumOfWords = 0
        _longWord = ''
        for line in _file:
            for word in line.split(' '):
                if (word[-1].lower() == 'а'):
                    _sumOfWords += 1
                if (len(_longWord) < len(word)):
                    _longWord = word
        _file.close()
        return {'count': _sumOfWords, 'longWord': _longWord}
    else:
        return 'Передан пустой путь до файла'

print(SumOfLastA('text/text.txt'))