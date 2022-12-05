s=0
with open('Day2/input.txt')as f:ls=f.read().splitlines()
for l in ls:
    for r in(("X","0"),("Y","3"),("Z","6"),("A","1"),("B","2"),("C","3")):l=l.replace(*r)
    s+=int(l[2])
    if l[2]=='0'and l[0]=='1':s+=3
    elif l[2]=='0':s+=int(l[0])-1
    if l[2]=='3':s+=int(l[0])
    if l[2]=='6'and l[0]=='3':s+=1
    elif l[2]=='6':s+=int(l[0])+1
print(s)