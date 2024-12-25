"""
ID: eushaza1
LANG: PYTHON3
TASK: gift1
"""

"""
file opened in this is provided by the website.
"""

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

e = fin.readlines()

np = e[0]
np = int(np)

i = 0
people = [ ]
while i < np :
    people.append( e[i+1])
    i += 1
x = 0

ppl = {}
part = ""
while x < len(people) :
    part = people[x]
    ppl[str(part)]= 0
    x += 1

    
np = np + 2 #7    
i = 0
lol = 0
olo = 0
while np < len(e) :
    dist = e[np]
    dist = (dist.split( ))
    if int(dist[1]) == 0 :
        dist[1] = 0
    else :
        olo = int(dist[0]) // int(dist[1])
        der = int(dist[0]) % int(dist[1])
        ppl[e[np-1]] -= int(dist[0])
        ppl[e[np-1]] += der
        j = 0
        while j < int(dist[1]) :
            ppl[e[np+j+1]] += int(olo)
            j += 1
    np += int(dist[1]) + 2

pplkey = list(ppl)
values = ppl.values()
pplvalue = list(values)


while i < len(ppl) :
    x = pplkey[i].strip("\n")
    fout.write(x + " " + str(pplvalue[i]) + "\n")
    i += 1

fout.close()




   
    






 

