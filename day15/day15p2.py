with open("input.txt") as f:
    data = f.read().split('\n\n')

grid = [list(x) for x in data[0].split('\n')]
instructions = data[-1].strip()
instructions = instructions.replace('\n','')

n_rows = len(grid)
n_cols = len(grid[0])

new_grid = [[] for i in range(n_rows)]

#create new "wide" grid
for i in range(n_rows):
    for j in range(n_cols):
        val = grid[i][j]
        if val == '.' or val == '#':
            new_grid[i].append(val)
            new_grid[i].append(val)
        elif val == '@':
            new_grid[i].append(val)
            new_grid[i].append('.')
        elif val == 'O':
            new_grid[i].append('[')
            new_grid[i].append(']')

def get_robot_pos():
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i][j] == '@':
                roboti, robotj = i,j
    return roboti, robotj


def visualize_grid(grid):
    for row in grid:
        print(row)

grid = new_grid

def make_move(to_move, di, dj):
    new_positions = {(i+di,j+dj) for i, j in to_move}
    grid_copy = [row[:] for row in grid]
    for i,j in to_move:
       grid[i+di][j+dj] = grid_copy[i][j]
       if (i,j) not in new_positions:
           grid[i][j] = '.'

roboti, robotj = get_robot_pos()

move_dict = {'<': (0,-1), '^': (-1,0), '>': (0,1), 'v': (1,0)}

for move in instructions:
    #print(f"move {move}")
    #visualize_grid(grid)
    #print('-------------')
    di, dj = move_dict[move]
    nexti, nextj = roboti+di, robotj+dj
    next_val = grid[nexti][nextj]
    if next_val == '#':
        #wall, skip move
        continue
    elif next_val == '.':
        #move
        grid[nexti][nextj] = '@'
        grid[roboti][robotj] = '.'
        roboti, robotj = nexti, nextj
    #this part has changed for p2
    elif di != 0: #moving up or down
        #find all blocks that need to move, move them all at once
        do_move = True
        to_move = [(roboti,robotj)]
        sfr = 0
        ni, nj = roboti, robotj
        while sfr < len(to_move):
            #move one up
            ci, cj = to_move[sfr][0], to_move[sfr][1]
            ni, nj = ci + di, cj + dj
            old_val = grid[ci][cj]
            new_val = grid[ni][nj]
            if new_val == '[':
                to_move.append((ni,nj))
                if old_val != '[':  
                    to_move.append((ni,nj+1))
            elif new_val == ']':
                to_move.append((ni,nj))
                if old_val != ']':
                    to_move.append((ni,nj-1))
            elif new_val == '#':
                #cannot move if wall above
                do_move = False
                break
            sfr += 1
        if do_move:
            make_move(to_move,di,dj) #check if rock above
            roboti, robotj = roboti+di, robotj+dj
    else: #moving horizontally 
        ni, nj = roboti+di, robotj+dj
        while grid[ni][nj] != '#' and grid[ni][nj] != '.':
            ni, nj = ni + di, nj + dj
        if grid[ni][nj] == '#':
            #wall, skip move
            continue
        #empty space, move
        # if dj is negative, moving left -> '[' at end of box
        if dj < 0:
            boxes = ['[',']']
        else:
            boxes = [']','[']
        i = 0
        while grid[ni][nj] != '@':
            grid[ni][nj] = boxes[i%2]
            ni, nj = ni - di, nj - dj
            i += 1
        #move robot
        grid[ni+di][nj+dj] = '@'
        grid[ni][nj] = '.'
        roboti, robotj = ni+di, nj+dj

tot_sum = 0
seen = set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '[' and (i,j) not in seen:
            tot_sum += min(j,j+1)+100*i
            seen.add((i,j))
        
print(tot_sum)
