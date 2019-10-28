import os
from random import randint
f = open(os.path.join(os.path.dirname(__file__), '1.txt'), 'w')
for i in range(10):
    f.write(str(randint(-10000, 10000)) + "\n")
f.close()
f = open(os.path.join(os.path.dirname(__file__), '1.txt'), 'r')
_lines = []
for line in f:
    _lines.append(int(line.split("\n")[0]))
f.close()
print("Числа, записанные в файл:", _lines)
print("Сумма:", sum(_lines))
print("Среднее:", sum(_lines) / len(_lines))