def count_A(path):
    fname = open(path,"r")
    s = fname.read()
    
    n = 0
    
    while s:
        offsetN = s.find('a')
        if offsetN == -1:
            break
        elif offsetN == (len(s) - 1):
            n += 1
            break
        elif s[offsetN+1] == ' ':
            n += 1
            s = s[offsetN+1:]
        else:
            s = s[offsetN+1:]
    if n == 0:
        print('Слов заканчивающихся на "а" не найдено')
    else:
        print('На "а" заканчивается %s слов(а)' % n)
    fname.close()


def lenMaxWord(path):
    fname = open(path, "r")
    count = int(0)
    maxLen = int(0)
                
    for line in (fname):       
        for letter in line:
            if (letter != ' ' or letter != '\n'): 
                count += 1
                
                
            if (letter == ' ' or letter == '\n'):
                if (maxLen < count):
                    maxLen = count
                count = 0
    fname.close()                                 
    return count
                

def readText(path):
    f = open(path, "r")
    for line in f:
        print(line)
    f.close()

count_A("hello.txt")
print("======================")
readText("hello.txt")
print("======================")
print("Max lenght is: ",lenMaxWord("hello.txt"))
    









