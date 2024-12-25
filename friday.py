
"""
ID: eushaza1
LANG: PYTHON3
TASK: friday
"""

"""
file opened in this is provided by the website.
"""

fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')
N = fin.readlines()
N = (int(N[0]))
cent = 1900

if (N > 400) :
    N = 400

years = cent + N

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(months)


weeks = [ 0, 0, 0, 0, 0, 0, 0] 
print(weeks)

days  = 13
i = 0

while i < N :
    x = 0    
    while x < len(months) :
        count = (days % 7)
        weeks[count] = weeks[count] + 1
        days += months[x]
        print(days)
        if (x ==  1)  and (i % 4  == 0) and (i % 100 != 0):
            days += 1
        elif (x ==  1)  and (i % 4  == 0) and (i % 100 == 0) and (i == 100):
            days += 1
        x += 1
    i += 1

fout.write(str(weeks[6]) + " " + str(weeks[0]) + " " + str(weeks[1]) + " " + str(weeks[2]) + " " + str(weeks[3]) + " " + str(weeks[4]) + " " + str(weeks[5]) + "\n")
    
    





fout.close()
