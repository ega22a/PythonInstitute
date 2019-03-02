sumOfItems = 0
arr = []
arr.append(['Клей', 50, 10])
arr.append(['Тетрадь', 20, 100])
arr.append(['Ручка', 50, 10])

for i in range(0, 3):
    sumOfItems += (arr[i][1] * arr[i][2])

print('Стоимость товаров: ', sumOfItems)