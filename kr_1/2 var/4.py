string = input('Введите вашу строку: ')
counter = 0
secSring = ''

for char in string:
    if (char.upper() == 'И'):
        secSring += char + '-'
        counter += 1
    else:
        secSring += char

print('Измененная строка: ', secSring)
print('Количество изменений: ', counter)