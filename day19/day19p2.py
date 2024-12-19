from collections import defaultdict

with open("input.txt") as f:
    data = [x for x in f.read().splitlines() if x]

patterns = data[0].split(', ')
targets = data[1:]

cache = defaultdict(int)
def possible(design,patterns):
    if cache[design]:
        return cache[design]
    if design == '':
        return 1
    n_pos = 0
    for p in patterns:
        if design.startswith(p):
            n_pos += possible(design[len(p):], patterns)
    cache[design] = n_pos
    return n_pos

tot_poss = 0
for t in targets: #curr target e.g brwrr
    n_poss = possible(t,patterns)
    tot_poss += n_poss

print(tot_poss)
