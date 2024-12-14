import re

def nums(x):
    return list(map(int,re.findall(r'-?\d+',x)))

with open("input.txt") as f:
    data = [nums(x) for x in f.read().splitlines()]

grid_width = 101
grid_height = 103
total_time = 100
grid = []

for i in range(grid_height):
    row = list()
    for j in range (grid_width):
        row.append(list())
    grid.append(row)

#data[0] = [x,y,vx,vy]
#x = column (distance from left wall)
#y = row (distance from top wall)
#grid[roboty][robotx] containst list of velocities and id 
for idx, (robotx,roboty,robotvx,robotvy) in enumerate(data):
    robotlist = grid[roboty][robotx]
    robotlist.append((robotvx,robotvy,idx))

def visualize_grid():
    print("---------------")
    for row in grid:
        for robot in row:
            if not robot:
                print(".", end='')
            else:
                print(len(robot), end='')
        print('')
    print("---------------")

def calculate_new_position(i,j,dx,dy):
    return (i + dy) % grid_height, (j + dx) % grid_width

#visualize_grid()
visualize = False
for second in range(total_time):
    has_moved = set()
    for i in range(grid_height):
        for j in range(grid_width):
            current_robots = grid[i][j]
            for robot in current_robots[:]:
                (robotvx, robotvy, id) = robot
                if id in has_moved:
                    continue
                has_moved.add(id)
                #remove from old position
                current_robots.remove(robot)
                newi,newj = calculate_new_position(i,j,robotvx,robotvy)
                grid[newi][newj].append(robot)
#                visualize = True
#            if visualize:
#                print(f"robot with ID {id} at pos (x={j},y={i}) has moved to pos (x={newj}, y={newi})")
#                visualize = False
#                visualize_grid()

mid_height = (grid_height-1)/2
mid_width = (grid_width-1)/2

top_left = 0
top_right = 0
bottom_left = 0
bottom_right = 0
for i in range(grid_height):
    for j in range(grid_width):
        n_robots = len(grid[i][j])
        if i < mid_height and j < mid_width:
            top_left += n_robots
        elif i < mid_height and j > mid_width:
            top_right += n_robots
        elif i > mid_height and j < mid_width:
            bottom_left += n_robots
        elif i > mid_height and j > mid_width:
            bottom_right += n_robots

print(top_left*top_right*bottom_left*bottom_right)