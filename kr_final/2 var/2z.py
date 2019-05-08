'''
3адан массив из 25 случайных элементов в диапазоне от -10 до 10.
Выберите заканчивающиеся на 3 из них и распечатайте в порядке убывания.
'''
import random
mas = []
natri = []
for i in range(25):
    mas.append(random.randint(-10,10))
print(mas)
for j in range(25):
    if str(mas[j]).endswith('3') == True:
        natri.append(mas[j])
print(natri)
