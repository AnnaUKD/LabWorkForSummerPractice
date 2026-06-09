import random

matrix = []
for i in range(4):
    row = []
    for j in range(3):
        row.append(random.randint(-20, 20))
    matrix.append(row)

print("Матриця:")
for row in matrix:
    print(row)

max_sum = -1
needed_row = 0

for i in range(4):
    if abs(sum(matrix[i])) > max_sum:
        max_sum = abs(sum(matrix[i]))
        needed_row = i

print("Індекс потрібного рядка:", needed_row)