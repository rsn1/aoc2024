with open("input.txt") as f:
    data = f.read().split('\n\n')

grid = [list(x) for x in data[0].split('\n')]
instructions = data[-1].strip()
instructions = instructions.replace('\n','')
n_rows = len(grid)
n_cols = len(grid[0])

def visualize_grid():
    for row in grid:
        print(row)

roboti, robotj= 0,0
#find start position
for i in range(n_rows):
    for j in range(n_cols):
        if grid[i][j] == '@':
            roboti, robotj = i,j


move_dict = {'<': (0,-1), '^': (-1,0), '>': (0,1), 'v': (1,0)}
#exit()
for move in instructions:
    #print(f"move {move}")
    #visualize_grid()
    #print('-------------')
    di, dj = move_dict[move]
    next_val = grid[roboti+di][robotj+dj]
    if next_val == '#':
        #wall, skip move
        continue
    elif next_val == '.':
        #move
        grid[roboti+di][robotj+dj] = '@'
        grid[roboti][robotj] = '.'
        roboti, robotj = roboti+di, robotj+dj
    elif next_val == 'O':
        next_copy = next_val
        steps_from_robot = 1
        while next_copy == 'O':
            #after while loop next_copy will be at block after last rock ('O')
            steps_from_robot += 1
            next_copy = grid[roboti+di*steps_from_robot][robotj+dj*steps_from_robot]
        #check if wall after last rock
        if next_copy == '#':
            #cant move
            continue
        #free space after last rock (next_copy == '.'). Move stone
        grid[roboti+di*steps_from_robot][robotj+dj*steps_from_robot] = 'O'
        #update robot pos
        grid[roboti+di][robotj+dj] = '@'
        grid[roboti][robotj] = '.'
        roboti, robotj = roboti+di, robotj+dj

tot_sum = 0
for i in range(n_rows):
    for j in range(n_cols):
        if grid[i][j] == 'O':
            tot_sum += i*100+j

print(tot_sum)
