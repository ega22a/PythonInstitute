sick = []

sick.append(['Репьев', 20, 'Мужской', 110])
sick.append(['Калягина', 38, 'Женский', 150])
sick.append(['Евсина', 64, 'Женский', 180])
sick.append(['Тюрина', 4, 'Женский', 100])
sick.append(['Иванов', 25, 'Мужской', 110])

for value in sick:
    if (value[3] > 140):
        print('Данные о больном:', value)