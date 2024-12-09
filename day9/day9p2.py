from collections import defaultdict

with open("input.txt") as f:
    data = f.read().strip()

def find_first_dotseq(list,n_dots):
    dotseq = []
    for idx, c in enumerate(list):
        if len(dotseq) == n_dots:
            return dotseq[0][0]

        if c == '.':
            dotseq.append((idx,c))
        else:
            dotseq = []
    return -1
        
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
i = 1
current_chunk = []
has_been_moved = defaultdict(bool)
while i < list_len-1:
    backwards = new_list[-i] 
    if backwards == '.' or has_been_moved[backwards]:
        i += 1
        continue

    while new_list[-i] == backwards:
        current_chunk.append((-i,backwards))
        i += 1
        if (i == list_len):
            break
    
    chunk_len = len(current_chunk)
    empty_chunk = '.' * chunk_len
    #first_idx = ''.join(new_list).find(empty_chunk) <--- annoying bug, indices get screwed for multi digit numbers
    #example had no multi digit file IDs :(
    first_idx = find_first_dotseq(new_list,chunk_len)
    if first_idx == -1 or first_idx > list_len-i:
        #no empty chunks
        current_chunk = []
        continue

    for j in range(chunk_len):
        new_list[first_idx+j] = current_chunk[j][1]
        new_list[current_chunk[j][0]] = '.'
    has_been_moved[backwards] = True
    
    current_chunk = []
    
sum = 0
for idx, c in enumerate(new_list):
    if c.isdigit():
        sum += idx * int(c)

print(sum)
