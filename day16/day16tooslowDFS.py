import sys

with open("input2.txt") as f:
    grid = [list(x) for x in f.read().splitlines()]

n_rows = len(grid)
n_cols = len(grid[0])

def find_tile(c):
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == c:
                return i,j


def visualize_grid(i,j):
    grid_copy = [row[:] for row in grid]
    grid_copy[i][j] = 'O'

    for x in range(i-10,i+10):
        for y in range(j-10, j+10):
            if x in range(n_rows) and y in range(n_cols):   
                print(grid_copy[x][y],end='')
            else:
                print('$',end='')
        print()

def visualize_path(path):
    grid_copy = [row[:] for row in grid]
    for i,j,_ in path:
        grid_copy[i][j] = 'O'
    for i in range(n_rows):
        for j in range(n_cols):
            print(grid_copy[i][j],end='')
        print()

lowest = 1000000000
best_paths = []
dead_ends = set()

starti, startj = find_tile('S')
endi, endj = find_tile('E')

def adj4(i,j):
    adj = []
    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
        if i+di in range(n_rows) and j+dj in range(n_cols) and grid[i+di][j+dj] != '#':
            adj.append((di,dj))
    return adj

def dfs(i, j, dir, path, pathset):
    if i == endi and j == endj:
        global lowest, best_paths
        total_score = sum([x[-1] for x in path])
        lowest = min(total_score,lowest)
        if total_score < lowest:
            best_paths = [path[:]]
        elif total_score == lowest:
            best_paths.append(path[:])
        return

    for di, dj in adj4(i,j):
        newi, newj = i+di, j+dj
        if (newi, newj) in pathset:
            continue

        #calc score
        score = 1
        if dir != (di, dj):
            score += 1000

        pathset.add((i,j))
        path.append((i,j,score))
        dfs(newi, newj, (di,dj), path,pathset)
        pathset.remove((i,j))
        path.remove((i,j,score))

sys.setrecursionlimit(10000)

dfs(starti, startj, (0,1), [], set())

#for b in best_paths:
#    print("============")
#    visualize_path(b)
#    print("============")
#print(endi,endj)
print(lowest)
