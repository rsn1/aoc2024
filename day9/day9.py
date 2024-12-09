with open("input.txt") as f:
    data = f.read().strip()

#check if all elements left of idx are digits
def all_digits_left(list,index):
    for i in range(index):
        if not list[i].isdigit():
            return False
    return True

new_list = []
current_id = 0
for idx, c in enumerate(data):
    is_file = idx % 2 == 0
    n_repetitions = int(c)
    if is_file:
        for i in range(n_repetitions):
            new_list.append(str(current_id))
        current_id += 1
    else:
        for i in range(n_repetitions):
            new_list.append('.')


list_len = len(new_list)

#assumes first element is not '.'
for i in range(1,list_len):
    backwards = new_list[-i] 
    if backwards.isdigit() and not all_digits_left(new_list,list_len-i):
        next_dot = new_list.index('.')
        new_list[next_dot] = backwards
        new_list[-i] = '.'

sum = 0
for idx, c in enumerate(new_list):
    if c.isdigit():
        sum += idx * int(c)

print(sum)
