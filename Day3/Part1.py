t=0
with open('Day3/input.txt') as f:ls=f.read().splitlines()
for l in ls:
    o=set(l[:len(l) // 2]).intersection(set(l[len(l) // 2:]))
    if ord(str(o)[2])>96:t+=ord(str(o)[2])-96
    else:t+=ord(str(o)[2])-38
print(t)