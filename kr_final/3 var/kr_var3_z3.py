import random

slov = {"Copybook":15, "Book":100, "Pen":20, "Brush":30, "Painter tool":150,
        "A diary":75, "Journal":200, "Pencil":10, "Eraser":30, "Notes":175}

sred = int(0)
count = int(0)

for key, value in slov.items():
    print("Товар: ", key, "Цена: ", value)
    sred += value
    count += 1

print()
sred = sred / count
print("Средняя цена товаров: ", sred)
print()
for key, value in slov.items(): 
    if (value < sred):
        print("Товар: ", key, "Цена: ", value)

print()
print("Обновлённый словарь")

slov.update({"smth":random.randint(0,1000), "smth'":random.randint(0,1000), "smth''":random.randint(0,1000)})

for key, value in slov.items():
    print("Товар: ", key, "Цена: ", value)
