inputs=[[]]
x=0
isfirst=1
with open (r"C:\Users\tom.oliver\OneDrive - Cinos Limited\AoC\AoC\Day4\input.txt") as file:
    lines = file.read().splitlines()
    for line in lines:
        if isfirst == 1:
            inputs[0].extend(line.split(','))
            isfirst=0
            continue
        if line == '/s': 
            x+=1
            inputs.append([])
            continue
        inputs[x].append(line.split('/\[0-9] /\[0-9]'))
print(inputs)