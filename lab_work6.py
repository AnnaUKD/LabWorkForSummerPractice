import math
import random

print("Задача 1")
matrix = []

for i in range(15):
    row = []
    for j in range(10):
        row.append(random.randint(10, 99))
    row.sort()
    matrix.append(row)


print("Відсортована матриця")
for row in matrix:
    for item in row:
        print(item, end="\t")
    print()  