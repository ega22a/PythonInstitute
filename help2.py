string = input('Введите ваше предложение (без знаков препинания): ')
thumbString = ''

for value in string.split(' '):
    thumbString += value[::-1] + ' '

print('Перевернутые слова: ', thumbString)