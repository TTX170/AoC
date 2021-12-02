with open (r"C:\Users\tom\Downloads\input2.txt") as file:
    inputs = file.read().splitlines()
file.close()
splitputs = []
for i in inputs:
    splitputs.append(i.split())
#print(splitputs)
forward=0
depth=0
for i in splitputs:
    if i[0] == 'forward':
        forward+=int(i[1])
    if i[0] == 'down':
        depth+=int(i[1])
    if i[0] == 'up':
        depth-=int(i[1])
total = forward*depth
print("part 1:")
print(forward)
print(depth)
print(total)

#part 2

forward=0
depth=0
aim=0
for i in splitputs:
    if i[0] == 'forward':
        forward+=int(i[1])
        if aim != 0:
            depth+=(int(i[1])*aim)
    if i[0] == 'down':
        aim+=int(i[1])
    if i[0] == 'up':
        aim-=int(i[1])
total = forward*depth
print("part 2:")
print(aim)
print(forward)
print(depth)
print(total)
