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
    
N_SECRET_NUMBERS = 2000
tot_sum = 0
for secret in data:
    next = secret
    for i in range(N_SECRET_NUMBERS):
        next = calculate_next(next)
    tot_sum += next 

print(tot_sum)
