with open("input.txt") as f:
    data = f.read()#[list(map(int,x.split())) for x in f.read().splitlines() if x]

print(len(data))

for idx,c in enumerate(data):
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
        current_idx += 1
        num += data[current_idx]
    #mul(123
    if data[current_idx] != ',':
        continue
    current_idx += 1
    #mul(123,
    num2 = ''
    while(data[current_idx].isdigit()):
        current_idx += 1
    #mul(123,54
    if data[current_idx] != ')':
        continue
    

