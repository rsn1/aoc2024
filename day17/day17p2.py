import re

with open('input.txt') as f:
    data = f.read().splitlines()

def nums(x):
    return list(map(int,re.findall(r'-?\d+',x)))

input_reg = {}

#register A
input_reg[4] = nums(data[0])[0]
#register B
input_reg[5] = nums(data[1])[0]
#register C
input_reg[6] = nums(data[2])[0]

program = nums(data[-1])

def evaluate_combo(op):
    if op <= 3:
        return op
    else:
        return reg[op]

print(input_reg)
print(program)

desired_ans = program[:]

prog_len = len(program)
ans = []

stop = False
#observation: final digits change very slow compared to first couple digits

n_iterations = 136904901132300 # 136904230044000 #136897787600000#136889197700000-100000-1000000#1136889197700000-100000
#at 300000000000000 the answer has 17 digits, not 16. has to be smaller
#ans should be between 100000000000000 and 280000000000000
#at 28000000000000 ans gets 17 len
#at 140000000000000  final 2 digits correspond
#final 4 digits correspond at 136889197700000
change_since = [0] * 20
while ans != desired_ans:
    #setup for new iteration of program with different reg[4] value
    if stop == True:
        break
    n_iterations += 1
    reg = dict(input_reg)
    reg[4] = n_iterations
    prev_ans = list(ans)
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

    #if len(ans) == len(desired_ans) and ans[-7:] == desired_ans[-7:]:#ans[-1] == desired_ans[0] and ans[1] == desired_ans[1]:
    #    stop = True
    #    print(f"a register: {n_iterations}")
    #    print(f"answer: {ans}")
    #    print(f"desired answer: {desired_ans}")
    #    break
    if n_iterations % 100000 == 0:
        print(f"a register: {n_iterations}")
        print(f"answer: {ans}, length : {len(ans)}")
        print(f"desired answer: {desired_ans}, length : {len(desired_ans)}")
        print(f"n iterations since last change: {change_since}")
    if len(prev_ans) != len(ans):
        print(f"answer length changed: from {len(prev_ans)} to {len(ans)}")
    elif len(prev_ans) == len(ans):
        for i in range(len(prev_ans)):
            if prev_ans[i] != ans[i]:
                #if i == 15:
                #    print(f"It took {n_iterations} for last digit to change")
                #    stop = True
                #    break
                change_since[i] = 0
            else:
                change_since[i] += 1

#ans = ans[:-1]
print(f"found! final A reg value: {n_iterations}")
print(ans)
print(desired_ans)

#final 4 locked in
#answer: [6, 5, 4, 7, 1, 2, 3, 3, 3, 3, 3, 1, 5, 5, 3, 0]
#desired answer: [2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0]
#found! final A reg value: 136889197700000
#[6, 5, 4, 7, 1, 2, 3, 3, 3, 3, 3, 1, 5, 5, 3, 0]
#[2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0]
#

#final 5 locked in
#answer: [7, 7, 1, 4, 2, 3, 3, 3, 3, 1, 3, 6, 5, 5, 3, 0]
#desired answer: [2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0]
#found! final A reg value: 136897787600000
#[7, 7, 1, 4, 2, 3, 3, 3, 3, 1, 3, 6, 5, 5, 3, 0]
#[2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0]

#final 6 locked in
#answer: [0, 1, 3, 3, 3, 3, 3, 3, 7, 0, 4, 6, 5, 5, 3, 0]
#desired answer: [2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0]
#found! final A reg value: 136904230044000
#[0, 1, 3, 3, 3, 3, 3, 3, 7, 0, 4, 6, 5, 5, 3, 0]
#[2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0]


#final 7 locked in
#answer: [1, 2, 3, 3, 3, 3, 3, 1, 6, 3, 4, 6, 5, 5, 3, 0]
#desired answer: [2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0]
#found! final A reg value: 136904901132300
#[1, 2, 3, 3, 3, 3, 3, 1, 6, 3, 4, 6, 5, 5, 3, 0]
#[2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0]


#all locked in
#found! final A reg value: 136904920099226
#[2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0]
#[2, 4, 1, 5, 7, 5, 1, 6, 0, 3, 4, 6, 5, 5, 3, 0]