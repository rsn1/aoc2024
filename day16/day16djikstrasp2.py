with open("input2.txt") as f:
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
#print(endi,endj)

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
            

#k = dist.keys()
p = prev.keys()
for pr in p:
    i,j,dir = pr
    #print(i,j)
    if i == endi and j == endj:
        print("prev:", prev[pr])
        print("dist:",dist[pr])


#seen = set()
#back = prev[]
#while back != None:

#print(k)
#for x in k:
#    if x[0] == endi and x[1] == endj:
#        print(dist[x])