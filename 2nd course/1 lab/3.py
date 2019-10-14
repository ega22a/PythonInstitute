import math
sine = {
    0: "Крыса или мышь",
    1: "Бык",
    2: "Тигр",
    3: "Кролик или кот",
    4: "Дракон",
    5: "Змея",
    6: "Лошадь",
    7: "Овца или коза",
    8: "Обезьяна",
    9: "Петух",
    10: "Собака",
    11: "Кабан или свинья"
}

trigger = True
while trigger:
    try:
        year = int(input("Введите ваш год рождения: "))
        trigger = False
    except ValueError:
        print("Вы должны ввести число!")
        trigger = True
print("Ваш знак по восточному календарю: " + sine.get(math.fabs((year - 1900) % 12)))