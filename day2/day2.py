import numpy as np

with open("input.txt") as f:
    data = [list(map(int,x.split())) for x in f.read().splitlines() if x]

def is_valid(nparr):
    diff = np.diff(nparr)
    print(f"diff :  {diff}")
    #decreasing
    c = ((diff < 0) & (np.absolute(diff) < 4))
    #increasing
    d = ((diff > 0) & (np.absolute(diff) < 4))

    if np.all(c) or np.all(d):
        return True
    return False

n_safe = 0
for idx, line in enumerate(data):
    nparr = np.array(line)
    if is_valid(nparr):
        n_safe += 1
        continue
    #conditions not all true, see if removing element can make it true
    for idx,val in enumerate(nparr):
        new_arr = np.delete(nparr,idx)
        if is_valid(new_arr):
            n_safe += 1
            break
print(n_safe)
