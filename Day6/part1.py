with open('Day6/input.txt') as f:inp=f.read()
for i in range (len(inp)):
    if len(set(list(inp[i:i+4])))==4:
        print(i+4)
        break