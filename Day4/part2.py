t=0
with open('Day4/input.txt') as f:ls=f.read().splitlines()
for l in ls:
    if(not(int(l.split(',')[0].split('-')[0])<int(l.split(',')[1].split('-')[0])and int(l.split(',')[0].split('-')[1])<int(l.split(',')[1].split('-')[0])or int(l.split(',')[0].split('-')[0])>int(l.split(',')[1].split('-')[1])and int(l.split(',')[0].split('-')[1])>int(l.split(',')[1].split('-')[1]))):t+=1
print(t)