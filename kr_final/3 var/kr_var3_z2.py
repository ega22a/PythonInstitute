import random
import math

arr = []
mass = []

for i in range(0,24):
    arr.append(random.randint(-10,10))
    
mod = int(0)

for i in range(0,24):
    if arr[i] == -7:
        continue
    mod = arr[i] % 10
    if (mod == 3):
        mass.append(arr[i])

for i in range (0, len(mass) - 1):
    if (mass[i] == -7):
        del mass[i] 

for i in range(len(mass)-1):
    for j in range(len(mass)-i-1):
        if mass[j] < mass[j+1]:
            mass[j], mass[j+1] = mass[j+1], mass[j]

f = open("text.txt", "w")
for index in mass:
    f.write(str(index) + '\n')
f.close()
