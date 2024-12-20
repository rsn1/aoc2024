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

def adj4(grid, i,j):
    adj = []
    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
        if i+di in range(n_rows) and j+dj in range(n_cols) and grid[i+di][j+dj] != '#':
            adj.append((i+di,j+dj))
    return adj

starti, startj = find_tile('S')
endi, endj = find_tile('E')

prev = {}
prev[(starti,startj)] = None
dists = {}
dists[(starti,startj)] = 0
def bfs(starti,startj,endi,endj,grid):
    Q = deque([(starti,startj,0)])
    visited = set()
    visited.add((starti,startj))
    while len(Q) != 0:
        curi, curj, dist = Q.popleft()
        if curi == endi and curj == endj:
            return dist
        for adjacent in adj4(grid, curi, curj):
            if adjacent not in visited:
                visited.add(adjacent)
                prev[adjacent] = (curi, curj)
                dists[adjacent] = dist+1
                Q.append((adjacent[0],adjacent[1],dist+1))

normal_time = bfs(starti,startj,endi,endj,grid)
cheat_times = []

shortest_path = []
bstart = (endi,endj)
while bstart != None:
    shortest_path.append(bstart)
    bstart = prev[bstart]

#now we have shortest_path
shortest_path = shortest_path[::-1]

#9453x9453
def manhattan(p1,p2):
    return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])

allowed_cheat_dist = 20

#check every pair of points on shortest path
#if manhattan distance between them is shorter, the shortcut is faster
tot = 0
for start in shortest_path:
    for end in shortest_path:
        cheat_dist = manhattan(start,end)
        if cheat_dist > allowed_cheat_dist:
            continue
        time_saved = dists[end] - cheat_dist - dists[start]
        if time_saved >= 100:
            tot += 1

print(tot)
