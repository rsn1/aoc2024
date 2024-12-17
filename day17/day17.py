import re

with open('input2.txt') as f:
    data = f.read().splitlines()

def nums(x):
    return list(map(int,re.findall(r'-?\d+',x)))


reg = {}

#register A
reg[4] = nums(data[0])[0]
#register B
reg[5] = nums(data[1])[0]
#register C
reg[6] = nums(data[2])[0]

program = nums(data[-1])


def evaluate_combo(op):
    if op <= 3:
        return op
    else:
        return reg[op]

print(reg)
print(program)

prog_len = len(program)

ans = []

pc = 0
while pc < prog_len:
    op = program[pc]
    if op == 0:
        #adv combo
        numerator = reg[4]
        combo_op = 2**evaluate_combo(program[pc+1])
        res = numerator // combo_op
        reg[4] = res

    elif op == 1:
        #bxl literal
        reg[5] = reg[5] ^ program[pc+1]

    elif op == 2:
        #bst combo
        combo_op = evaluate_combo(program[pc+1])
        reg[5] = combo_op % 8
        
    elif op == 3:
        #jnz
        if reg[4] == 0:
            #do nothing
            pc += 2
            continue
        pc = program[pc+1]

    elif op == 4:
        #bitwise or
        reg[5] = reg[5] ^ reg[6]

    elif op == 5:
        #out combo
        combo_op = evaluate_combo(program[pc+1])
        #ans += str(combo_op%8) + ','
        ans.append(combo_op%8)
        #print(combo_op % 8, end='')

    elif op == 6:
        #bdv combo
        numerator = reg[4]
        combo_op = 2**evaluate_combo(program[pc+1])
        res = numerator // combo_op
        reg[5] = res

    elif op == 7:
        #cdv combo
        numerator = reg[4]
        combo_op = 2**evaluate_combo(program[pc+1])
        res = numerator // combo_op
        reg[6] = res

    #update pc
    if op != 3:
        pc += 2

print(ans)