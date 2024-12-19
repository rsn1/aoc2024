from collections import defaultdict

with open("input.txt") as f:
    data = [x for x in f.read().splitlines() if x]

patterns = data[0].split(', ')
targets = data[1:]

cache = defaultdict(bool)
def possible(design,patterns):
    if cache[design]:
        return True
    if design == '':
        return True
    poss = []
    for p in patterns:
        if design.startswith(p):
            is_possible = possible(design[len(p):], patterns)
            poss.append(is_possible)
            cache[design] = is_possible
    return any(poss)

tot_poss = 0
tot_imposs = 0
for t in targets: #curr target e.g brwrr
    tlen = len(t) 
    if possible(t,patterns):
        tot_poss += 1
    else:
        tot_imposs += 1

print(tot_poss)
print(tot_imposs)
