e=[0]
with open('Day1/input.txt')as f:ls=f.read().splitlines()
for l in ls:
    if l == "":e.append(0)
    else:e[-1]+=int(l)
print(sorted(e)[-1]+sorted(e)[-2]+sorted(e)[-3])