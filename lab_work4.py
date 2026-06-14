print("Завдання 1")

arr = []
print("Вводьте числа. Щоб зупинитись, напишіть слово stop")
print("В масиві може бути 10 елементів.")

while len(arr) < 10:
    user_input = input("Введіть число: ")
    if user_input == "stop":
        break

    num = int(user_input)

    if num % 5 == 0:
        arr.append(num)
    else:
        print("Не ділиться на 5, пропуск!")

print("Ваш масив:", arr)

n = len(arr)
for i in range(n):
    for j in range(0, n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Відсортований масив:", arr)

pos_sum = 0
pos_count = 0

neg_product = 1
neg_count = 0

total_sum = 0

for x in arr:
    total_sum += x

    if x > 0:
        pos_sum += x
        pos_count += 1
    elif x < 0:
        neg_product *= x
        neg_count += 1

if neg_count == 0:
    neg_product = 0

avg = total_sum / n

print("РЕЗУЛЬТАТИ ОБЧИСЛЕНЬ")
print("Додатні: сума =", pos_sum, ", кількість =", pos_count)
print("Від'ємні: добуток =", neg_product, ", кількість =", neg_count)
print("Середнє арифметичне всього масиву =", round(avg, 2))