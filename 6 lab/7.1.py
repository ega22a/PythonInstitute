def wordListByCondition(_str, _type = 1):
    alphabet = [
        ['а', 'у', 'о', 'е', 'и', 'я', 'ю', 'ё', 'э', 'ы'],
        ['б', 'в', 'г', 'д', 'з', 'ж', 'п', 'ф', 'к', 'т', 'с', 'ш', 'л', 'м', 'н', 'р', 'й', 'х', 'ц', 'ч', 'щ']
    ]
    strToList = _str.split(' ')
    output = ''
    if (_type == 1):
        for value in strToList:
            try:
                if (alphabet[0].index(value[len(value) - 1]) > -1):
                    output += value + ' '
            except ValueError:
                continue
    elif(_type == 2):
        for value in strToList:
            try:
                if (alphabet[1].index(value[len(value) - 1]) > -1):
                    output += value + ' '
            except ValueError:
                continue
    return output

string = input('Введите ваше предложение (без знаков препинания): ')

print('Слова, закачивающиеся на согласную букву: ', wordListByCondition(string, 2))
print('Слова, закачивающиеся на гласную букву: ', wordListByCondition(string))