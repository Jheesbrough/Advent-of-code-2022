s=0
with open('Day2/input.txt')as f:ls=f.read().splitlines()
for l in ls:
    for r in(("X","1"),("Y","2"),("Z","3"),("A","1"),("B","2"),("C","3")):l=l.replace(*r)
    s+=int(l[2])
    if l[0]==l[2]:s+=3
    if l[0]=='1'and l[2]=='2'or l[0]=='2'and l[2]=='3'or l[0]=='3'and l[2]=='1':s+=6
print(s)