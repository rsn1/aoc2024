from collections import defaultdict

with open("input.txt") as f:
    data = f.read().splitlines()

#print(data)
n_rows = len(data)
n_cols = len(data[0])

def in_bounds(i,j):
    return i >= 0 and i < n_rows and j >= 0 and j < n_cols


def dfs_help(nx,ny, val):
    area = 0
    perimeter = 0
    if in_bounds(nx,ny):
        if (data[nx][ny] == val):
            #neighbour with same value
            area, perimeter = dfs(nx,ny)
        else:
            #neighbour with different value
            perimeter += 1
    else:
        perimeter += 1
    return area, perimeter


visited = set()
def dfs(nx, ny):
    #nx, ny = node
    if (nx,ny) in visited or not in_bounds(nx,ny):
        return 0, 0

    visited.add((nx,ny))

    val = data[nx][ny]

    area = 0
    perimeter = 0

    #base case: node is an outer node
    area_down, perimeter_down = dfs_help(nx+1,ny,val)
    area_up, perimeter_up = dfs_help(nx-1,ny,val)
    area_right, perimeter_right = dfs_help(nx,ny+1,val)
    area_left, perimeter_left = dfs_help(nx,ny-1,val)

    area +=  1 + area_down + area_left + area_up + area_right
    perimeter += perimeter_down + perimeter_left + perimeter_up + perimeter_right
    
    return area, perimeter



tot_sum = 0
regions = defaultdict(list)
for i in range(n_rows):
    for j in range(n_cols):
        current = data[i][j]
        area, perimeter = dfs(i,j)
        tot_sum += area*perimeter
        if area != 0 and perimeter != 0:
            regions[current].append((area,perimeter))

print(tot_sum)




