crates=[[],[],[],[],[],[],[],[],[]]
with open('Day5/input.txt') as f:ls=f.read().splitlines()
for j in range (1,10):
    for i in range (8):
        if (ls[7-i][j*4-3])!=' ':crates[j-1].append(ls[7-i][j*4-3])
instructions = ls[10:]
for instruction in instructions:
    b,v,b,f,b,t = instruction.split((' '))
    crates[int(t)-1] = crates[int(t)-1] + crates[int(f)-1][-int(v):]
    crates[int(f)-1]=crates[int(f)-1][:-int(v)]
for i in range(9):
    try:
        print(crates[i].pop(), end='')
    except:
        print(' ', end='')