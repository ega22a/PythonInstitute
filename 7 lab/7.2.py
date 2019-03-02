books = []
countOfBooks = int(input('Какое количество книг вы желаете внести: '))

for i in range(0, countOfBooks):
    author = input('Введите имя автора: ')
    name = input('Введите наименование книги: ')
    year = int(input('Введите год издания: '))
    sheets = int(input('Введите количество страниц: '))

    books.append([author, name, year, sheets])

    print()

print('Ваша библиотека:')
for value in books:
    print(value)
print()

searchAuthor = input('Книги какого автора нужно вывести: ')
for value in books:
    if (value[0] == searchAuthor):
        print(value)

lastBooks = books[0]
for value in books:
    if(value[2] < lastBooks[2]):
        lastBooks = value
print('Самая ранняя книга в библиотеке: ', lastBooks)