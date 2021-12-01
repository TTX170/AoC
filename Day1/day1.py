import more_itertools
with open (r"C:\Users\tom\Downloads\input.txt") as file:
    inputs = file.read().splitlines()
file.close()
inputs = list(map(int, inputs))
increase = 0
last=0 
for i in inputs:
    if (last !=0) and (i > last):
        increase+=1
    last = i 
print(increase)

#part 2
tests = [1,2,3,4,5,6,7,8] 
sums = []
losums = list(more_itertools.windowed(inputs,n=3,step=1))
for i in losums:
    sums.append(sum(i))
increase = 0
last=0 
for i in sums:
    if (last !=0) and (i > last):
        increase+=1
    last = i 
print(increase)