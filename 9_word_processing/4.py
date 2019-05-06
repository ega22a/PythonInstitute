def getAllLinks(_path = ''):
    if (len(_path) != 0):
        _file = open(_path, 'r')
        _returned = []
        for line in _file:
            _subString = ''
            _a = ''
            _endPoint = 0
            while (_endPoint != -1):
                if (line.find('<a ', _endPoint) != -1):
                    _subList = {}
                    _subString = line[line.find('<a ', _endPoint) + 3 : line.find('</a>', _endPoint)]
                    _endPoint = line.find('</a>', _endPoint) + 1
                    _subList.update({'text': _subString.split('>')[1]})
                    _subSplit = _subString.split('>')[0].split('"')[:-1]
                    for key in range(0, len(_subSplit), 2):
                        if (key == 0):
                            _subList.update({_subSplit[key][:-1]: _subSplit[key + 1]})
                        else:
                            _subList.update({_subSplit[key][1:-1]: _subSplit[key + 1]})
                    _returned.append(_subList)
                else:
                    _endPoint = -1
        _file.close()
        return _returned
    else:
        return 'Given empty path to file.'

for piece in getAllLinks('/home/george/Документы/python/9_word_processing/text/2.html'):
    print(piece)