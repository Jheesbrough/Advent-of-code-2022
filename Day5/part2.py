crates=[[],[],[],[],[],[],[],[],[]]
with open('Day5/input.txt') as f:ls=f.read().splitlines()
for (i,j) in [(i,j) for i in range(8) for j in range(1,10)]:
    if (ls[7-i][j*4-3])!=' ':crates[j-1].append(ls[7-i][j*4-3])
for i in ls[10:]:
    crates[int(i.split((' '))[5])-1] = crates[int(i.split((' '))[5])-1] + crates[int(i.split((' '))[3])-1][-int(i.split((' '))[1]):]
    crates[int(i.split((' '))[3])-1]=crates[int(i.split((' '))[3])-1][:-int(i.split((' '))[1])]
for i in range(9):print(crates[i].pop(), end='')