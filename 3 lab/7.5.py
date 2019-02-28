import random

secret = random.randrange(5, 80)

guess = int(input('Какое число загадал компьютер: '))

while (secret != guess):
    if (guess > secret):
        print('Было загадано поменьше!')
    else:
        print('Было загадано побольше!')
    guess = int(input('Какое число загадал компьютер: '))

print('Вы отгадали число!')