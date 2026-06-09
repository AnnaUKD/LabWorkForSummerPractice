import random

n = int(input("Введіть кількість чисел в масиві: "))
arr = []

for i in range(n):
    arr.append(random.randint(-10, 10))

print("Згенерований масив:", arr)

C = float(input("Введіть число С: "))

count = 0
for x in arr:
    if x > C:
        count += 1

max_idx = 0
for i in range(n):
    if abs(arr[i]) > abs(arr[max_idx]):
        max_idx = i

print("Максимум за модулем:", arr[max_idx], "(стоїть на позиції:", max_idx, ")")

result_of_multiplication = 1

if max_idx == n - 1:
    result_of_multiplication = 0
else:
    for i in range(max_idx + 1, n):
        result_of_multiplication *= arr[i]

print("Кількість чисел більших за C:", count)
print("Добуток елементів після максимуму за модулем:", result_of_multiplication)