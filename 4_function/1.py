def listToDictionary(_list):
    _dict = {}
    for key in range(0, len(_list)):
        _dict.update({key: _list[key]})
    return _dict

print(listToDictionary([1,2,3]))