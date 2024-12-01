with open("input.txt") as f:
    data = [x.split(" ") for x in f.read().splitlines()]

list1 = []
list2 = []
for x in data:
    list1.append(int(x[0]))
    list2.append(int(x[-1]))

list1.sort()
list2.sort()

sum = 0
for x,y in zip(list1,list2):
    sum += abs(x-y)

print(sum)

sim_score = 0
for x in list1:
    n_count = list2.count(x)
    sim_score += n_count * x

print(sim_score)


