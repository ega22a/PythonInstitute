import os
f = open(os.path.join(os.path.dirname(__file__), '1.txt'), 'r')
_lines = []
_o = []
for line in f:
    _lines.append(int(line.split("\n")[0]))
f.close()
for line in _lines:
    if (line % 2 == 0):
        _o.append(line)
print("Обычный файл", _lines)
print("Четные числа", _o)