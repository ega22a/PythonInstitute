string = input('Введите ваше предложение (без знаков препинания): ')

for value in string.split(' '):
    print('Слово: ' + value + ':')
    first = ''
    second = ''
    for char in range(0, len(value)):
        if ('аоиеёэыуюя'.find(value[char]) != -1):
            first += value[char] + ', '
        elif ('бвгджзйклмнпрстфхцчшщ'.find(value[char]) != -1):
            second += value[char] + ', '
    print('    Гласные буквы: ' + first[:-2])
    print('    Согласные буквы: ' + second[:-2])