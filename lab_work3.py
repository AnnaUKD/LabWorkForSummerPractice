import math

print("Завдання 1")

A = 0
B = math.pi / 4
M = 20

H = (B - A) / M

for i in range(21):
    x_i = A + i * H
    f_x = math.sin(x_i) + math.tan(x_i)

    print(f"Крок {i}: X = {round(x_i, 3)} | Результат = {round(f_x, 3)}")

print("Завдання 2")

import math


a = 2.5
b = 0.4
t = -1.0

while t <= 1.0:

    if t < 0.1:
        w = math.sqrt(a * (t**2) + b * math.sin(t) + 1)
    elif t == 0.1:
        w = a * t + b
    else:
        w = math.sqrt(a * (t**2) + b * math.cos(t) + 1)


    print(f"t = {round(t, 1)}  ->  w = {round(w, 3)}")
    t = round(t + 0.2, 1)


