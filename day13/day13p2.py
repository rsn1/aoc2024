import numpy as np
import re

with open("input.txt") as f:
    data = f.read().splitlines()

def nums(x):
    return list(map(int,re.findall(r'\d+',x)))

buttona = []
buttonb = []
prizes = []

i = 0
while i < len(data):
    buttona.append(nums(data[i]))
    buttonb.append(nums(data[i+1]))
    prizes.append(nums(data[i+2]))
    i += 4

n_rounds = len(prizes)
tot_sum = 0
for i in range(n_rounds):
    a_button_x, a_button_y = buttona[i][0], buttona[i][1]
    b_button_x, b_button_y = buttonb[i][0], buttonb[i][1]
    prize_x, prize_y = prizes[i][0]+10000000000000, prizes[i][1]+10000000000000

    eqs = np.array([[a_button_x, b_button_x],[a_button_y, b_button_y]])
    target = np.array([prize_x, prize_y])
    sol = np.linalg.solve(eqs, target)
    roundedA = np.round(sol[0])
    roundedB = np.round(sol[1])
    if roundedA * a_button_x + roundedB * b_button_x == prize_x and roundedA * a_button_y + roundedB * b_button_y == prize_y:
        tot_sum += int(roundedA*3+roundedB)

print(tot_sum) 
