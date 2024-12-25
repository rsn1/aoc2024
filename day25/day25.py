with open("input.txt") as f:
    data = [x.splitlines() for x in f.read().split('\n\n')]

n_rows = len(data[0])
n_cols = len(data[0][0])

keys = []
locks = []

for x in data:
    if x[-1] == '#####':
        keys.append(x)
    elif x[0] == '#####':
        locks.append(x)

keycolumns = []
lockcolumns = []

for key in keys:
    keycols = []
    for i in range(n_cols):
        colsum = n_rows
        for j in range(n_rows): 
            if (key[j][i] != '#'):
                colsum -= 1
                
        keycols.append(colsum)
    keycolumns.append(keycols)

for lock in locks:
    lockcols = []
    for i in range(n_cols):
        colsum = 0
        for j in range(n_rows):
            if (lock[j][i] == '#'):
                colsum += 1
        lockcols.append(colsum)
    lockcolumns.append(lockcols)

tot_sum = 0
for key in keycolumns:
    for lock in lockcolumns:
        fit = True
        for x,y in zip(key,lock):
            if x+y > n_rows:
                fit = False
                break
        if fit:
            tot_sum += 1

print(tot_sum)
