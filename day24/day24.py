with open("input.txt") as f:
    data = f.read().split('\n\n')

xyvals = data[0].splitlines()
expr = data[-1].splitlines()

dict = {}

for e in expr:
    s = e.split(" ")
    op1 = s[0]
    instr = s[1]
    op2 = s[2]
    res = s[4]
    dict[res] = (op1,op2,instr)
    print(s)
for x in xyvals:
    v = x.split(": ")
    xvar = v[0]
    xval = v[1]
    dict[xvar] = int(xval)
    print(v)

def dfs(start):
    val = dict[start]
    if val == 0 or val == 1:
        return val
    
    res1 = dfs(val[0])
    #save results
    dict[val[0]] = res1
    res2 = dfs(val[1])
    dict[val[1]] = res2

    funct = val[-1]
    if funct == 'OR':
        dict[start] = res1 or res2
    elif funct == 'XOR':
        dict[start] = res1 ^ res2
    elif funct == 'AND':
        dict[start] = res1 and res2
    return dict[start]
 
#simplify all expressions
for key in dict:
    dfs(key)

number = 0
z = []
while True:
    if number < 10:
        currentz = f'z0{number}'
    else:
        currentz = f'z{number}'
    try:
        zval = dict[currentz]
    except:
        break
    z.append(zval)
    number += 1

#convert binary -> decimal
decimalz = 0
for idx, num in enumerate(z):
    decimalz += num*2**idx

#z = z[::-1]
print(decimalz)
