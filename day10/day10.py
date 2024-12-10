with open("input.txt") as f:
    data = [list(map(int,x)) for x in f.read().splitlines()]

n_rows = len(data)
n_cols = len(data[0])

zeros = []
for i, line in enumerate(data):
    for j, c in enumerate(line):
        if c == 0:
            zeros.append((i,j))
    
def in_bounds(i,j):
    return i >= 0 and i < n_rows and j >= 0 and j < n_cols

#node of form (i,j), prev is data[i][j]
def dfs(node, prev, visited):
    i,j = node[0], node[1]
    if not in_bounds(i,j) or (i,j) in visited:
        return 0

    val = data[i][j]
    if val != prev + 1:
        return 0

    if val == 9:
        #visited.add((i,j)) #add this line for part 1
        return 1

    return dfs((i+1,j), val, visited) + dfs((i-1,j), val, visited) + dfs((i,j+1), val, visited) + dfs((i,j-1), val, visited)

tot_sum = 0
for zero in zeros:
    visited = set()
    score = dfs(zero,-1,visited)
    tot_sum += score

print(tot_sum)
