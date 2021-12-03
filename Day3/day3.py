with open (r"C:\Users\tom\Downloads\input3.txt") as file:
    inputs = file.read().splitlines()
zeros=[0] * len(inputs[0])
ones=[0] * len(inputs[0])
gamma=''
epsilon=''
for i in inputs:
    for x in range(12):
        if i[x] == '1':
            ones[x]+=1
        else:
            zeros[x]+=1
for i in range(12):
    if zeros[i] > ones[i]:
        gamma+=('0')
        epsilon+=('1')
    else:
        gamma+=('1')
        epsilon+=('0')

gammaint = int(gamma,2)
epsilonint = int(epsilon,2)
total = gammaint*epsilonint
print(ones)
print(zeros)
print(gammaint)
print(epsilonint)
print(total)

#part2
o2list=[[] for i in range(len(inputs[0])+1)]
co2list=[[] for i in range(len(inputs[0])+1)]
o2list[0]=inputs
co2list[0]=inputs
for x in range(12):
    o2one=0
    o2zero=0
    co2zero=0
    co2one=0
    for i in o2list[x]:
        if i[x] == '1':
            o2one+=1
        else:
            o2zero+=1
    if o2one >= o2zero: keep = '1' 
    else: keep='0'
    for i in o2list[x]:
        if len(o2list[x]) == 1: o2list[x+1].append(i) 
        elif keep == i[x]:
            o2list[x+1].append(i)   
    for i in co2list[x]:
        if i[x] == '1':
            co2one+=1
        else:
            co2zero+=1
    if co2zero <= co2one: keep = '0' 
    else: keep='1'
    for i in co2list[x]:
        if len(co2list[x]) == 1: co2list[x+1].append(i) 
        elif keep == i[x]:
            co2list[x+1].append(i)
o2int = int(o2list[12][0],2)
co2int = int(co2list[12][0],2)
print(co2int)
print(o2int)
p2total = co2int*o2int
print (p2total)
