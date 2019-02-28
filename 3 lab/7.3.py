import sys, math
x = -2.0

for i in range(0, 21):
    y = (math.cos(math.cos(x))) / x
    sys.stdout.write('x = ' + str(x) + '; y = ' + str(y) + '\r\n')
    x += 0.2