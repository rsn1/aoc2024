from collections import defaultdict

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

with open("input.txt") as f:
    data = f.read().splitlines()

print(data)
orddict = defaultdict(list)
updates = []
for idx,x in enumerate(data):
    if x == '':
        updates = data[idx+1:]
        break
    d = x.split('|')
    orddict[int(d[0])].append(int(d[-1]))

updates = [list(map(int,x.split(','))) for x in updates]

print(f"updates: {updates}")
print(orddict)

#parsing done
#orddict[num] contains list of numbers that have to be AFTER num

#keep stack, pop whenever element is encountered

total = 0
total_wrong = 0
for round in updates:
    bigstack= set()
    for number in round:
        
        if number in bigstack:
            bigstack.remove(number)

        following = orddict[number]
        if not following:
            #no numbers have to follow
            continue
        #add all numbers that have to be after current num
        for numb in following:
            bigstack.add(numb)
    #numbers might not be part of round, only keep ones that are.
    condition = intersection(list(bigstack),round)
    if not condition:
        mid = int((len(round)-1)/2)
        total += int(round[mid])
    else:
        #part 2
        print(f"round {round}")
        print(f"condition {condition}")
        #not correctly ordered
        #get key from value
        for wrongly_placed in condition:
            correct_list = []
            all_found = False
            to_place_after = []
            for key in orddict:
                if wrongly_placed in orddict[key]:
                    to_place_after.append(key)
            to_place_after = intersection(to_place_after,round)
            print(f"to_place_after  {to_place_after}")            

            for idx,x in enumerate(round):
                if x != wrongly_placed:
                    correct_list.append(x)
                if x in to_place_after:
                    to_place_after.remove(x)

                if not to_place_after and not all_found:
                    correct_list.append(wrongly_placed)
                    all_found = True

                    continue
            round = correct_list
        print(f"round after swap: {correct_list}")
        mid = int((len(round)-1)/2)
        total_wrong += int(round[mid])

print(total)
print(total_wrong)
