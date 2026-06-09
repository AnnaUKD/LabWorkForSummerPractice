print("Завдання 1")

full_name = input("Введіть Прізвище, Ім'я та По-батькові: ")

words = full_name.split()

last_name = words[0]

print("Результат:")
for letter in last_name:
    print(letter)

print("Завдання 2")

given_string = input("Введіть рядок: ")

count = 0
positions = []

for i in range(len(given_string)):
    if "a" <= given_string[i] <= "z":
        count += 1
        positions.append(i + 1)

if count > 0:
    print("Кількість малих латинських літер в наданому рядку:", count)
    print("Номери їх позицій:", positions)
else:
    print("Малих латинських літер немає у даному рядку.")