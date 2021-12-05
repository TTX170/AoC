inputs=[[]]
x=0
winningboard=0
isfirst=1

with open (r"C:\Users\tom\OneDrive\Desktop\AoC\Day4\input.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        if isfirst == 1:
            inputs[0].extend(line.split(','))
            isfirst=0
            continue
        if line == '': 
            x+=1
            inputs.append([])
            continue
        inputs[x].append(line.split())

for i in inputs[0]:
    for x in range(1,101):
        
        #currentboard = inputs[x]
        for y in range(5):
            
            pos = 0
            for z in range(5):
                winnerhori=0
                winnervert=0
                if inputs[x][y][z] == i:
                    inputs[x][y][z] = 'x'
                if inputs[x][y][z] == 'x': winnerhori+=1
                for vert in range(5):
                    if inputs[x][vert][z]=='x': 
                        winnervert+=1
            if winnerhori == 5:
                winningboard=inputs[x]
                finalvalue = int(i)
                break
            elif winnervert == 5:
                winningboard=inputs[x]
                finalvalue = int(i)
                break
        if winningboard !=0:
            break
#print(winningboard)
totlist=[]
total = 0
for i in winningboard:
    for x in i:
        if x != 'x':
            totlist.append(int(x))
for i in totlist:
    total+=i
print(winningboard)
print(total)
print(finalvalue)
totaltotal=total*finalvalue
print(totaltotal)