t=0
with open('Day3/input.txt') as f:ls=f.read().splitlines()
for i in range (int(len(ls)/3)):
    o=set(ls[i*3]).intersection(ls[i*3+1],ls[i*3+2])
    if ord(str(o)[2])>96:t+=ord(str(o)[2])-96
    else:t+=ord(str(o)[2])-38
print(t)