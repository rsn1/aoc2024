from collections import defaultdict

with open("input.txt") as f:
    data = list(map(int,f.read().splitlines()))

#given secret_i calculates secret i+1
def calculate_next(secret):
    secret ^= secret*64
    secret %= 16777216

    secret ^= secret // 32
    secret %= 16777216

    secret ^= secret * 2048
    secret %= 16777216

    return secret
    
pricedict = defaultdict(int)

N_SECRET_NUMBERS = 2000
#data = [123]
for secret in data:
    seen = set()
    last_digits = []
    next = secret
    for i in range(N_SECRET_NUMBERS):
        last_digits.append(int(str(next)[-1]))
        next = calculate_next(next)
    #we have all last digits (prices) for given secret word
    #calculate the sequences
    differences = [x[1]-x[0] for x in zip(last_digits,last_digits[1:])]
    for i in range(len(differences)-3):
        dictentry = tuple(differences[i:i+4]) 
        #only add sequence if it's the first time we see it
        if dictentry not in seen:
            pricedict[dictentry] += last_digits[i+4]
            seen.add(dictentry)

#find max value
print(max(pricedict.values()))
