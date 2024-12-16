with open("input.txt") as f:
    grid = [list(x) for x in f.read().splitlines()]

n_rows = len(grid)
n_cols = len(grid[0])

def find_tile(c):
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == c:
                return i,j

def adj4(i,j):
    adj = []
    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
        if i+di in range(n_rows) and j+dj in range(n_cols) and grid[i+di][j+dj] != '#': # and (di,dj) not in pathset:
            adj.append((i+di,j+dj,(di,dj)))
    return adj

starti, startj = find_tile('S')
endi, endj = find_tile('E')

def pop_min(Q):
    minimum = min(Q,key=lambda x: x[0])
    Q.remove(minimum)
    return minimum

start_dir = (0,1)
Q = [(0,(starti,startj,start_dir))]
dist = {}
dist[(starti,startj,start_dir)] = 0
prev = {}
prev[(starti,startj,start_dir)] = None
#diri, dirj = (0,1)
while len(Q) != 0:
    score, (ci, cj, dir) = pop_min(Q) #min(grid)

    for ni, nj, (di,dj) in adj4(ci,cj):
        alt = score + 1
        if dir != (di, dj):
            alt += 1000
        new_node = (ni,nj,(di,dj)) 
        if new_node not in dist or alt < dist[new_node]:
            dist[new_node] = alt
            prev[new_node] = [(ci,cj,dir)]
            Q.append((alt,new_node))
        elif alt == dist[new_node]:
            prev[new_node].append((ci,cj,dir))

#find path to start from
minimum = None
mindi,mindj = None, None
for (di,dj) in [(1,0),(-1,0),(0,1),(0,-1)]:
    if (endi, endj, (di,dj)) in dist.keys():
        distance = dist[(endi,endj,(di,dj))]
        if minimum is None or distance < minimum:
            minimum = distance
            mindi, mindj = di, dj

revQ = [(endi,endj,(mindi,mindj))]
s = set(revQ)
while len(revQ) > 0:
    node = revQ.pop(-1)
    prev_nodes = prev[node]
    if prev_nodes == None:
        #at start
        continue
    for prev_node in prev_nodes:
        if prev_node not in s:
            s.add(prev_node)
            revQ.append(prev_node)

#print(s)
s = {(x[0],x[1]) for x in s}
print(len(s))
