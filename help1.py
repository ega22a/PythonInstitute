string = input('Введите ваше предложение (без знаков препинания): ')
thumb = ''
for value in string.split(' '):
    if (thumb.find(value) == -1):
        print('Слово ' + value + ' встречается ' + str(string.count(value)) + ' раз(а);')
    thumb += value