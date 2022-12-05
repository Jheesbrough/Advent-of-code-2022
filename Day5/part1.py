crates=[[],[],[],[],[],[],[],[],[]]
with open('Day5/input.txt') as f:ls=f.read().splitlines()
for (i,j) in [(i,j) for i in range(8) for j in range(1,10)]:
    if (ls[7-i][j*4-3])!=' ':crates[j-1].append(ls[7-i][j*4-3])
for instruction in ls[10:]:
    for i in range(int(instruction.split((' '))[1])):crates[int(instruction.split((' '))[5])-1].append(crates[int(instruction.split((' '))[3])-1].pop())
for i in range(9):print(crates[i].pop(), end='')