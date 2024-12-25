"""
ID: eushaza1
LANG: PYTHON3
TASK: ride
"""

fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
print(fin)
#fin.readlines()

e = fin.readlines()
c = e[0]
s = e[1]

print("c is " + str(c))
print("s is " + s)
ansl = []
ansl2 = []
multi = (1)
multi2 = (1)
for i in c :
    for j in i :
        j = (ord(j) - 64)
        ansl.append(j)
for i in ansl :
        multi = (multi * i)
for i in s :
    for j in i :
        j = (ord(j) - 64)
        ansl2.append(j)

for i in ansl2 :
        multi2 = (multi2 * i)
multi3 = (0)
if (multi %47 == multi2 %47) :
    x = "GO"
else :
    x = "STAY"
            




 
fout.write (x + "\n")
fout.close()


