employees = {
    'Иванов': 30000,
    'Петров': 20000,
    'Сидоров': 25000
}

for key, value in employees.items():
    print(key, value)

for value in employees.values():
    if value == 20000:
        print('Сотрудник с окладом в 20 000 рублей:', key, value)