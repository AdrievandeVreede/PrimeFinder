import math

priem = []
try:
    open("priem.txt","r")
except IOError:
    f = open("priem.txt","x")
    f.close()
    f = open("priem.txt","a")
    f.write('2\n')
    x = 3
    while x < 100000:
        s = 0 
        for i in range (2, math.ceil(x / 2)):
            if x%i == 0: 
                s = 1
                break
        if s == 0: 
            f.write(str(x) + "\n")
        x = x + 2
    f.close()
finally:
    file = open("priem.txt","r")
    for line in file:
        priem.append(int(line))
    x = priem[-1]
    file.close()
file = open("priem.txt", "a")
while True:
    s = 0 
    for i in priem:
        if x%i == 0: 
            s = 1
            break
    if s == 0:
        priem.append(x)
        file.write(str(x) + "\n")
        print(x)
    x = x + 2
