employees = {
    'Иванов': 30000,
    'Петров': 20000,
    'Сидоров': 25000,
    'Репьев': 3000,
    'Анатольевич': 150000
}

for key, value in employees.items():
    print(key, value)

for key, value in employees.items():
    if value < 30000:
        print('Сотрудник с окладом меньше 30 000 рублей:', key, value)