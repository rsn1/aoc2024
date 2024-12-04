with open("input.txt") as f:
    data = f.read().splitlines()

print(data)


n_rows = len(data)
n_cols = len(data[0])
print(f"rows :{n_rows}")
print(f"cols :{n_cols}")

total = 0
word = "XMAS"
#check left -> right and right -> left
for line in data:
    #left -> right
    total += line.count(word)
    #right -> left
    total += line.count(word[::-1])


print(f"total horizontal: {total}")

#check up -> down, down -> up
total_vertical = 0
for i in range(n_cols):
    for j in range(n_rows-3):
        vertical_word = data[j][i] + data[j+1][i] + data[j+2][i] + data[j+3][i]
        total_vertical += vertical_word.count(word)
        total_vertical += vertical_word.count(word[::-1])


print(f"total vertical: {total_vertical}")
total += total_vertical

#diagonals
diagonal_list_right = []
for i in range(n_rows): #i = 1
    tmp1=""
    tmp2=""
    for j in range(n_rows-i): #j = 0,1,2,3,4,5,6,7,8
        tmp1 += data[i+j][j] #0,1 1,2, 
        tmp2 += data[j][i+j]
        print(f"row: {i+j} col: {j} char: {tmp1}")#0+10-9-1
        print(f"row: {j} col: {i+j} char: {tmp2}")
    print("-----------------------")
    diagonal_list_right.append(tmp1)
    diagonal_list_right.append(tmp2)

middle_element = max(diagonal_list_right, key=len)
diagonal_list_right.remove(middle_element)

total_diagonal_right = 0
for line in diagonal_list_right:
    total_diagonal_right += line.count(word)
    total_diagonal_right += line.count(word[::-1])

print(f"total diagonal right: {total_diagonal_right}")
print(f"diagonal right {diagonal_list_right} n_elements: {len(diagonal_list_right)}")

diagonal_list_left = []
for i in range(n_cols):#0
    tmp1=""
    tmp2=""
    for j in range(n_cols-i):
        col = j
        row = i+j
        print(n_rows,i,j)
        tmp1 += data[row][-col-1]#0
        tmp2 += data[col][-row-1]
        print(f"row: {row} col: {-col-1} char: {tmp1}")#0+10-9-1
        print(f"row: {col} col: {row} char: {tmp2}")
    print("----------------------")

    diagonal_list_left.append(tmp1)
    diagonal_list_left.append(tmp2)

#remove mid element, counted twice
middle_element = max(diagonal_list_left, key=len)
diagonal_list_left.remove(middle_element)

total_diagonal_left = 0
for line in diagonal_list_left:
    total_diagonal_left += line.count(word)
    total_diagonal_left += line.count(word[::-1])

print(f"total diagonal left: {total_diagonal_left}")
print(f"diagonal left {diagonal_list_left} n_elements: {len(diagonal_list_left)}")

total += total_diagonal_right
total += total_diagonal_left
print(f"total: {total}")
#1, 0 : 2, 1: 3, 2

