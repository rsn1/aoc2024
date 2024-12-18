with open("input.txt") as f:
    data = f.read().splitlines()

data = [list(map(int,x.split(','))) for x in data]

n_cols = 71#7 #0...70
n_rows = 71#7

grid = []
for i in range(n_rows): #< 71 -> 0...70
    row = []
    for j in range(n_cols):
        row.append('.')
    grid.append(row)

def print_grid():
    for row in grid:
        for c in row:
            print(c,end='')
        print()

#i = row
#j = col
def adj4(i,j):
    adj = []
    for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
        adji, adjj = i+di, j+dj
        if adji in range(n_rows) and adjj in range(n_cols) and grid[i][j] != '#':
            adj.append((adji,adjj))
    return adj

starti, startj = 0,0
endi, endj = 70,70

n_bytes = 1024
for x,y in data[:n_bytes]:
    grid[y][x] = '#'
    #x is from left to right
    #y from top to bottom

stop = False
n_iterations = 0
while not stop:
    new_x, new_y = data[n_bytes+n_iterations]
    grid[new_y][new_x] = '#'

    Q = [(starti,startj,0)]
    visited = set((starti,startj))
    #do bfs until we cant reach end (no more nodes to visit)
    while True:
        try:
            curi, curj, dist = Q.pop(0)
        except:
            print(new_x,new_y)
            stop = True
            break
        if curi == endi and curj == endj:
            #print(curi,curj)
            break
        for adjacent in adj4(curi,curj):
            if adjacent not in visited:
                visited.add(adjacent)
                Q.append((adjacent[0],adjacent[1],dist+1))
    n_iterations += 1
