a = ['Pentium 5', 60000, 12]
a.append('Kitai')

print('Цена со скидкой: ', a[a.index(60000)] * 0.9)

a.reverse()
print(a)

print('Количество элементов списка: ', len(a))
a.remove(12)
print('Список, с удаленным количеством комплектующим: ', a)