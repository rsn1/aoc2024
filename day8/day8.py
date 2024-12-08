from collections import defaultdict
from itertools import combinations

with open("input.txt") as f:
    data = f.read().splitlines()

location_dict = defaultdict(list)
n_rows = len(data)
n_cols = len(data)
print(data)
print(n_rows)
print(n_cols)

antinode_map = [['.']*n_cols for _ in range(n_rows)]

def set_antinode(i,j):
    if i >= 0 and i < n_rows and j >= 0 and j < n_cols:
        antinode_map[i][j] = '#'
        return True
    return False

#create dict with all antennas and their indices
for row,line in enumerate(data):
    for col,c in enumerate(line):
        if c != '.':
            location_dict[c].append((row,col))

print(location_dict)

for antenna in location_dict:
    indices = location_dict[antenna]
    comb = list(combinations(indices,2))
    print(comb)
    for pair in comb:
        antenna1 = pair[0]
        antenna1_x, antenna1_y = antenna1[0], antenna1[1]
        antenna2 = pair[1]
        antenna2_x, antenna2_y = antenna2[0], antenna2[1]
        row_diff = antenna1_x - antenna2_x
        col_diff = antenna1_y -antenna2_y

        #part1
        #set_antinode(antenna1_x+row_diff,antenna1_y+col_diff) 
        #set_antinode(antenna2_x-row_diff,antenna2_y-col_diff) 

        #part2
        #start at antenna1, go in a line down then go in a line up
        print(f"antennas: {antenna1}, {antenna2}")
        k = 0
        while set_antinode(antenna1_x+row_diff*k,antenna1_y+col_diff*k):
            k += 1
        k = 0
        while set_antinode(antenna1_x-row_diff*k,antenna1_y-col_diff*k):
            k += 1

tot_sum = 0
for line in antinode_map:
    tot_sum += line.count('#')
    print(line)


print(tot_sum)
