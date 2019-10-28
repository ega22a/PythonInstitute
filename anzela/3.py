import os
f = open(os.path.join(os.path.dirname(__file__), '2.txt'), 'r')
_words = 0
for line in f:
    _words += len(line.split(" "))
f.close()
print("Количество слов в файле:", _words)