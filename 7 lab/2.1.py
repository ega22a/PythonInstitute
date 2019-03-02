items = []

print('Заполните базу товарами. Количество необходимых товаров - 100.')
for i in range(0, 100):
    print('Товар №', i + 1)
    nameOfItem = input('Введите наименование: ')
    vendorOfItem = input('Введите наименование производителя: ')
    if (input('Вывести общее количество товаров этого производителя? (y для согласия): ') == 'y'):
        sumOfVendor = []
        for value in items:
            if (value[1] == vendorOfItem):
                print(value)
    priceOfItem = float(input('Введите цену товара (за еденицу): '))
    countOfItem = int(input('Введите количество товаров: '))
    items.append([nameOfItem, vendorOfItem, priceOfItem, countOfItem])