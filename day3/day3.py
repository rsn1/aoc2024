with open("input.txt") as f:
    data = f.read()

sum = 0
do = True
for idx,c in enumerate(data):
    dowindow = data[idx:idx+4]
    dontwindow = data[idx:idx+7]
    
    if dowindow == "do()":
        do = True
    if dontwindow == "don't()":
        do = False
    if not do:
        continue

    #mulwindow
    wdw = data[idx:idx+3]
    if wdw != "mul":
        continue
    #mul
    current_idx = idx+3
    if data[current_idx] != '(':
        continue
    current_idx += 1
    #mul(
    num1 = ''
    while(data[current_idx].isdigit()):
        num1 += data[current_idx]
        current_idx += 1
    #mul(123
    if data[current_idx] != ',':
        continue
    current_idx += 1
    #mul(123,
    num2 = ''
    while(data[current_idx].isdigit()):
        num2 += data[current_idx]
        current_idx += 1
    #mul(123,54
    if data[current_idx] != ')':
        continue
    
    sum += int(num1) * int(num2)

print(sum)

