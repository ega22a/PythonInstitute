import math

trigger = True
while trigger:
    try:
        allSum = float(input("Введите желаемую сумму потребительского кредита: "))
        period = int(input("На какое количество лет вы желаете взять кредит: "))
        percent = float(input("Введите желаемую годовую процентную ставку: "))
        trigger = False
    except ValueError:
        print("Внимание! Введите только числа!")
        trigger = True
withOverprice = round(allSum * (1 + period * (percent / 100)), 2)
month = round(withOverprice / (12 * period), 2)
print("Общая сумма выплат с учетом надбавок: " + str(withOverprice) + ".")
print("Ежемесячный платеж составит: " + str(month) + ".")
print("Спасибо, что пользуетесь Python Bank.")