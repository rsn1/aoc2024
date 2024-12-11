from collections import defaultdict

with open("input.txt") as f:
    data = [int(x) for x in f.read().strip().split()]

n_blinks = 75

count_map = defaultdict(int)
for x in data:
    count_map[x] += 1

for i in range(n_blinks):
    new_count = defaultdict(int)
    keys = [x for x in count_map if count_map[x] != 0]
    for stone in keys:
        if stone == 0:
            new_count[1] += count_map[0]
            continue
        
        strstone = str(stone)
        strstonelen = len(strstone)
        if strstonelen % 2 == 0:
            mid = int(strstonelen / 2)
            left = strstone[:mid]
            right = strstone[mid:]
            new_count[int(left)] += count_map[stone]
            new_count[int(right)] += count_map[stone]
            continue

        #no other rules apply
        new_count[stone*2024] += count_map[stone]

    count_map = new_count

sum = 0
for x in count_map:
    sum += count_map[x]
    
print(sum)
