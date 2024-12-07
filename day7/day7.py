with open("input.txt") as f:
    data = [(int((x.split(':')[0])),list(map(int,x.split(':')[1].split()))) for x in f.read().splitlines()]

total = 0
for eq in data:
    target = eq[0]
    numbers = eq[1]
    results = set()
    results.add(numbers[0])
    to_check = numbers[1:]
    for x in to_check:
        #first iteration
        new_results = set()
        for y in results:
            new_results.add(y*x)
            new_results.add(y+x)
            new_results.add(int(str(y)+str(x))) #remove this for part1
        results = new_results
    if target in results:
        total += target

print(total)


