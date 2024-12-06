with open("input.txt") as f:
    data = f.read().splitlines()

print(data)
n_cols = len(data[0])
n_rows = len(data)

def get_guard_dir(symbol):
    if symbol == '^':
        return (-1,0)
    elif symbol == '>':
        return (0,1)
    elif symbol == '<':
        return (0,-1)
    elif symbol == 'v':
        return (1,0)


def is_in_bounds(idx):
    row,col = idx[0], idx[1]
    return row < n_rows and row >= 0 and col < n_cols and col >= 0

def add_tuples(tup1,tup2):
    return (tup1[0]+tup2[0],tup1[1]+tup2[1])

#find start pos
for idx,row in enumerate(data):
    if '^' in row:
        guard_symbol = '^'
        guard_idx = (idx,row.index(guard_symbol))
        guard_dir = get_guard_dir(guard_symbol)
    elif '>' in row:
        guard_symbol = '>'
        guard_idx = (idx,row.index(guard_symbol))
        guard_dir =  get_guard_dir(guard_symbol)
    elif '<' in row:
        guard_symbol = '<'
        guard_idx = (idx,row.index(guard_symbol))
        guard_dir =  get_guard_dir(guard_symbol)
    elif 'v' in row:
        guard_symbol = 'v'
        guard_idx = (idx,row.index(guard_symbol))
        guard_dir = get_guard_dir(guard_symbol)

start_pos = guard_idx
start_dir = guard_dir
start_symbol = guard_symbol

print(guard_idx)
print(guard_dir)
print(guard_symbol)

visited = set()
visited.add(guard_idx)
right_turn_map = {'^':'>', '>':'v', '<':'^', 'v':'<'}

while True:
    next_pos = add_tuples(guard_idx,guard_dir)
    if not is_in_bounds(next_pos):
        break
    next_symbol = data[next_pos[0]][next_pos[1]]

    if (next_symbol == '#'):
        #change dir
        guard_symbol = right_turn_map[guard_symbol]
        guard_dir = get_guard_dir(guard_symbol)
        #guard_symbol = next_symbol
    else:
        #no blocking, take a step
        guard_idx = next_pos
        visited.add(guard_idx)

print(len(visited))

#part 2
#valid locations for placement have to be in the visited set, since the guard has to pass through it.
#if ending up at same pose again -> in a loop
tot_sum = 0
visited.remove(start_pos)
print("part 2")
for pos in visited:
    guard_symbol = start_symbol
    guard_dir = start_dir
    guard_idx = start_pos
    new_data = [list(line) for line in data]
    new_data[pos[0]][pos[1]] = '#'
    cycle = set()
    cycle.add((start_pos[0],start_pos[1],guard_dir))
    while True:
        next_pos = add_tuples(guard_idx,guard_dir)
        if not is_in_bounds(next_pos):
            break
        next_symbol = new_data[next_pos[0]][next_pos[1]]

        if (next_symbol == '#'):
            #change dir
            guard_symbol = right_turn_map[guard_symbol]
            guard_dir = get_guard_dir(guard_symbol)
        else:
            #no blocking, take a step
            guard_idx = next_pos
            guard_pose = (guard_idx[0],guard_idx[1],guard_dir) 
            if guard_pose in cycle:
                tot_sum += 1
                break
            cycle.add(guard_pose)

print(tot_sum)
