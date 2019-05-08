'''
Написать функцию позволяющую из текстового файла считывать
текст и определить количество слов, заканчивающихся буквой "а".
Вывести самое длинное слово.
'''
def kolvo(x):
    kolv = 0
    for i in range(len(x)):
        #print(x[i])
        if (x[i].endswith('а') == True):
            kolv += 1
    return kolv
def dlinna(x):
    dlina = -1
    slovo = ''
    for i in range(len(x)):
        if len(x[i]) > dlina:
            dlina = len(x[i])
            slovo = x[i]
    return slovo
text = open('text.txt', 'r').read().split(' ')
print('Количество слов заканчивающихся на "А": ',kolvo(text))
print('Самое длинное слово: ',dlinna(text))
