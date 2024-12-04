with open("input.txt") as f:
    data = f.read().splitlines()

print(data)

n_rows = len(data)
n_cols = len(data[0])

total = 0

for i in range(n_rows):
    for j in range(n_cols):
        current_char = data[i][j]
        if (current_char != 'A'):
            continue
        number_of_mas = 0
        #diagonal, left to right
        if (i-1 >= 0 and j-1 >= 0 and i+1 < n_rows and j+1 < n_cols):
            if (data[i-1][j-1] == 'M' and data[i+1][j+1] == 'S'):
                number_of_mas += 1
            if (data[i-1][j-1] == 'S' and data[i+1][j+1] == 'M'):
                number_of_mas += 1

        #diagonal right to left
        if (i-1 >= 0 and j+1 < n_cols and i+1 < n_rows and j-1 >= 0):
            if (data[i-1][j+1] == 'M' and data[i+1][j-1] == 'S'):
                number_of_mas += 1
            if (data[i-1][j+1] == 'S' and data[i+1][j-1] == 'M'):
                number_of_mas += 1

        if number_of_mas > 1:
            total += 1
            print(i,j)


print(total)
