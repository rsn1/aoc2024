from collections import deque

with open("input.txt") as f:
    grid = [list(x) for x in f.read().splitlines()]

n_rows = len(grid)
n_cols = len(grid[0])

num_hash = 0
hashes = []
for i in range(n_rows):
    for j in range(n_cols):
        if grid[i][j] == '#':
            hashes.append((i,j))
            num_hash += 1

def find_tile(c):
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == c:
                return i,j

def adj4(grid2, i,j):
    adj = []
    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
        if i+di in range(n_rows) and j+dj in range(n_cols) and grid2[i+di][j+dj] != '#':
            adj.append((i+di,j+dj))
    return adj

starti, startj = find_tile('S')
endi, endj = find_tile('E')

def bfs(grid2):
    Q = deque([(starti,startj,0)])
    visited = set((starti,startj))
    while len(Q) != 0:
        curi, curj, dist = Q.popleft()
        if curi == endi and curj == endj:
            return dist
        for adjacent in adj4(grid2, curi, curj):
            if adjacent not in visited:
                visited.add(adjacent)
                Q.append((adjacent[0],adjacent[1],dist + 1))

normal_time = bfs(grid)
cheat_times = []

while len(hashes) > 0:
    hi, hj = hashes.pop(-1)
    grid_copy = [x[:] for x in grid]
    grid_copy[hi][hj] = '.'
    cheat_time = bfs(grid_copy)
    if cheat_time < normal_time:
        cheat_times.append(normal_time-cheat_time)

atleast_hundred = [x for x in cheat_times if x >= 100]
print(len(atleast_hundred))