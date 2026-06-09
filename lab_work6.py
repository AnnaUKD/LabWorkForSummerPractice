import math
import random

print("Задача 1")
a = 2.5
b = 0.4

print("  t   |    w")
print("----------------")

for i in range(-10, 11, 2):
    t = i / 10
    if t < 0.1:
        w = math.sqrt(a * (t**2) + b * math.sin(t) + 1)
    elif t == 0.1:
        w = a * t + b
    else:
        w = math.sqrt(a * (t**2) + b * math.cos(t) + 1)

    print(f"{t:4.1f} | {round(w, 4)}")


print("Завдання 2")

matrix = []

for i in range(15):
    row = []
    for j in range(10):
        row.append(random.randint(10, 99))
    row.sort()
    matrix.append(row)


print("--- ВІДСОРТОВАНА МАТРИЦЯ ---")
for row in matrix:
    for item in row:
        print(item, end="\t")
    print()  