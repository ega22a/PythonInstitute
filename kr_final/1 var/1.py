class fileProcessing():
    def __init__(self, filePath = ''):
        if (len(filePath) != 0):
            self.file = open(filePath, 'r')
        else:
            raise ValueError
    def getAllLine(self):
        _returned = []
        for line in self.file:
            _returned.append(line)
        return _returned
    def numberOfWords(self):
        _sum = 0
        for line in self.file:
            _sum += len(line.split(' '))
        return(_sum)
    def allWordsCapitalize(self):
        _returned = []
        for line in self.file:
            _string = ''
            for word in line.split(' '):
                _string += word.capitalize() + ' '
            _returned.append(_string[:-1])
        return _returned
    def close(self):
        self.file.close()

fp = fileProcessing(input('Введите путь до файла: '))
print(fp.getAllLine())
print(fp.numberOfWords())
print(fp.allWordsCapitalize())
fp.close()