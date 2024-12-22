import functools
import itertools

with open("input.txt") as f:
    data = f.read().splitlines()

def move_to_front(l1,element):
    n_elements = l1.count(element)
    new_list = [x for x in l1 if x != element]
    return [element]*n_elements+new_list

str_to_pos = {
    '^': (1,0),
    '>': (0,1),
    '<': (0,-1),
    'v': (-1,0)
}

pos_to_str = {v:k for k,v in str_to_pos.items()}

def optimize_movement(l1):
    n_left = l1.count('<')
    n_right = l1.count('>')
    n_down = l1.count('v')
    n_up = l1.count('^')
    return ['<']*n_left + ['v'] * n_down + ['^'] * n_up + ['>'] * n_right

class numeric_robot:
    def __init__(self):
        self.robot_map = {
            'A': (0,2),
            '0': (0,1),
            '1': (1,0),
            '2': (1,1),
            '3': (1,2),
            '4': (2,0),
            '5': (2,1),
            '6': (2,2),
            '7': (3,0),
            '8': (3,1),
            '9': (3,2),
}
        self.robot_state = 'A'

    def get_shortest_paths_to(self, goal):
        desti, destj = self.robot_map[goal]
        curi, curj = self.robot_map[self.robot_state]
        disti, distj = desti-curi, destj-curj #(0,-1)
        #return list of strings with all possible ways of doing the above movement i.e 
        #e.g (2,1) -> '^^>' '>^^' '^>^'
        #(-2,1) -> 'vv>' '>vv' 'v>v'
        movement_list = []
        n_vertical_moves = abs(disti)
        n_horizontal_moves = abs(distj)
        for _ in range(n_vertical_moves):
            movement_list.append(pos_to_str[(disti/n_vertical_moves,0)])
        for _ in range(n_horizontal_moves):
            movement_list.append(pos_to_str[(0,distj/n_horizontal_moves)])
        
        #sort it optimally
        #priority is: < - ^/v - >
        movement_list = optimize_movement(movement_list)
        #handle out of bounds
        if self.robot_state in ['A','0'] and goal in ['1','4','7']:
            #move up before left
            movement_list = move_to_front(movement_list,'^')
        elif self.robot_state in ['1','4','7'] and goal in ['A','0']:
            #move right before down
            movement_list = move_to_front(movement_list,'>')
        return movement_list

    def solve(self,code):
        movement_str = ''
        for c in code: #c = e.g '0', calculate ways to get to 0
            shortest_path_str = "".join(self.get_shortest_paths_to(c))
            shortest_path_str += 'A'
            movement_str += shortest_path_str
            self.robot_state = c #update robot state to x
            #reset robot state
        return movement_str

def get_numeric_part(code):
    str = ''
    i = 0
    #avoid leading 0
    while code[i] == '0':
        i+=1
    while code[i] != 'A':
        str += code[i]
        i+=1
    return int(str)
    
dirtopos = {
            '<': (0,0),
            'v': (0,1),
            '>': (0,2),
            '^': (1,1),
            'A': (1,2),
}

#all possible ways to go from start to end on directional pad
def possible_ways(start,end):
    starti, startj = dirtopos[start] #1,2
    endi, endj = dirtopos[end] # 0,0
    disti = endi-starti
    distj = endj-startj
    movement_str = ''
    n_vertical_moves = abs(disti)
    n_horizontal_moves = abs(distj)
    for _ in range(n_vertical_moves):
        movement_str += pos_to_str[(disti/n_vertical_moves,0)]
    for _ in range(n_horizontal_moves):
        movement_str += pos_to_str[(0,distj/n_horizontal_moves)]
    all_poss = set(itertools.permutations(movement_str))
    #handle out of bounds
    if start == 'A' and end == '<':
        all_poss.remove(('<','<','v'))
    elif start == '<' and end == 'A':
        all_poss.remove(('^','>','>'))
    elif start == '^' and end == '<':
        all_poss.remove(('<','v'))
    elif start == '<' and end == '^':
        all_poss.remove(('^','>'))
    return [list(x) for x in all_poss]

@functools.cache
def solve_rec(start,end,depth):
    start_to_end = possible_ways(start,end)
    for x in start_to_end:
        x.append('A')

    if depth == 1:
        return len(start_to_end[0])
    
    best = float('inf')
    for poss in start_to_end:
        curr = 'A' + "".join(poss)
        total_cost = 0
        for i in range(len(curr)-1):
            total_cost += solve_rec(curr[i],curr[i+1],depth-1)
        best = min(best,total_cost)


    #< -> path (A,<) = v<<A
    #A -> path(<,A) = >>^
    
    return best

overall_sum = 0
for d in data:
    print(f"calculating {d}")
    n1 = numeric_robot()
    first = n1.solve(d)
    tot_sum = 0
    first = 'A' + first
    for i in range(len(first)-1):
        tot_sum += solve_rec(first[i],first[i+1],25)

    numpart = get_numeric_part(d)
    overall_sum += numpart*tot_sum

print(overall_sum)
