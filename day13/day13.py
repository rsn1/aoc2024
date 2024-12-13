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
cost_to_win = []
for i in range(n_rounds):
    a_button_x, a_button_y = buttona[i][0], buttona[i][1]
    b_button_x, b_button_y = buttonb[i][0], buttonb[i][1]
    prize_x, prize_y = prizes[i][0], prizes[i][1]

    found = False
    for A in range(1,101):
        for B in range(1,101):
            x_pos = a_button_x * A + b_button_x * B
            y_pos = a_button_y * A + b_button_y * B
            if x_pos == prize_x and y_pos == prize_y:
                cost_to_win.append(A*3+B)
                found = True
                break

        if found:
            break

print(sum(cost_to_win))
