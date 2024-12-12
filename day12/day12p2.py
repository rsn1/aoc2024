from collections import defaultdict

with open("input.txt") as f:
    data = f.read().splitlines()

#print(data)
n_rows = len(data)
n_cols = len(data[0])

def in_bounds(i,j):
    return i >= 0 and i < n_rows and j >= 0 and j < n_cols


def get_neighbours(nx,ny):
    neighbours = []
    val = data[nx][ny]

    if in_bounds(nx+1,ny) and data[nx+1][ny] == val:
        neighbours.append((nx+1,ny))
    if in_bounds(nx-1,ny) and data[nx-1][ny] == val:
        neighbours.append((nx-1,ny))
    if in_bounds(nx,ny+1) and data[nx][ny+1] == val:
        neighbours.append((nx,ny+1))
    if in_bounds(nx,ny-1) and data[nx][ny-1] == val:
        neighbours.append((nx,ny-1))
    return neighbours

def get_n_corners(nx,ny):
    val = data[nx][ny]
    neighbours = get_neighbours(nx,ny)
    n_neighbours = len(neighbours)
    if n_neighbours == 0:
        return 4
    elif n_neighbours == 1:
        return 2
    elif n_neighbours == 2:
        #all on a row
        if (nx,ny+1) in neighbours and (nx,ny-1) in neighbours:
            return 0

        #all in a column
        if (nx+1,ny) in neighbours and (nx-1,ny) in neighbours:
            return 0
        
        smallestx = min(neighbours, key=lambda x: x[0])[0]
        smallesty = min(neighbours, key=lambda x: x[1])[1]
        dx = 1
        dy = 1
        if smallestx < nx:
            dx = -1
        if smallesty < ny:
            dy = -1
        if data[nx+dx][ny+dy] == val:
            return 1
        else:
            return 2
    elif n_neighbours == 3:
        unique_neighbour = (0,0)
        n_corners = 0
        for idx, x in enumerate(neighbours):
            except_current = list(neighbours)
            except_current.remove(x)
            is_unique = 0
            for y in except_current:
                if x[0] != y[0] and x[1] != y[1]:
                     is_unique += 1
            if is_unique == 2:
                unique_neighbour = (x[0],x[1])
                break
        if unique_neighbour[0] == nx:
            #same row
            #check nx-1,unique_neighbour[1], nx+1, unique_neighbour[1]
            if data[nx-1][unique_neighbour[1]] != val:
                n_corners += 1
            if data[nx+1][unique_neighbour[1]] != val:
                n_corners += 1
        elif unique_neighbour[1] == ny:
            if data[unique_neighbour[0]][ny+1] != val:
                n_corners += 1
            if data[unique_neighbour[0]][ny-1] != val:
                n_corners += 1
        return n_corners

    elif n_neighbours == 4:
        #could have between 1-4 corners
        non_neighbours = [data[nx+1][ny+1], data[nx+1][ny-1], data[nx-1][ny+1], data[nx-1][ny-1]]
        return 4 - non_neighbours.count(val) 


visited = set()
def dfs(nx, ny):
    if (nx,ny) in visited or not in_bounds(nx,ny):
        return 0, 0

    visited.add((nx,ny))

    val = data[nx][ny]

    area = 0

    #current nodes area and perimeter
    n_sides = get_n_corners(nx,ny)

    if in_bounds(nx+1,ny) and data[nx+1][ny] == val:
            #neighbour with same value
            area_down, sides_down = dfs(nx+1,ny)
            area += area_down
            n_sides += sides_down

    if in_bounds(nx-1,ny) and data[nx-1][ny] == val:
            #neighbour with same value
            area_up, sides_up = dfs(nx-1,ny)
            area += area_up
            n_sides += sides_up

    if in_bounds(nx,ny+1) and data[nx][ny+1] == val:
            #neighbour with same value
            area_right, sides_right = dfs(nx,ny+1)
            area += area_right
            n_sides += sides_right

    if in_bounds(nx,ny-1) and data[nx][ny-1] == val:
            #neighbour with same value
            area_left, sides_left = dfs(nx,ny-1)
            area += area_left
            n_sides += sides_left
   
    #area + 1, counting ourselves
    area +=  1
    return area, n_sides

tot_sum = 0
regions = defaultdict(list)
for i in range(n_rows):
    for j in range(n_cols):
        current = data[i][j]
        area, sides = dfs(i,j)
        if area != 0:
            #print(f"current region {current} sides: {sides}")
            tot_sum += sides*area


print(tot_sum)