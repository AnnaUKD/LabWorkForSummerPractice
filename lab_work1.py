print("Завдання 1")

print("Хрещення Русі відбулося в 988р.")
current_year = int(input("Який зараз рік?: "))
print(f"З того часу пройшло {current_year} років.")


print("Завдання 2")

first_number = int(input("Введіть перше ціле число: "))
second_number = int(input("Введіть друге ціле число: "))


def calculate_sum(first_number, second_number):
    return first_number + second_number


def calculate_floor_division(first_number, second_number):
    return first_number // second_number


print(f"Сума введених чисел дорівнює {calculate_sum(first_number, second_number)}, "
      f"а результатом ділення націло {calculate_floor_division(first_number, second_number)}")


print("Завдання 3")

no = int(input("Введіть № п/п: "))
culture = str(input("Введіть назву с/г культури: "))
plan = float(input("Введіть план: "))
fact = float(input("Введіть факт: "))

if plan > 0:
    percentage = (fact / plan) * 100
else:
    percentage = 0

percentage = round(percentage, 2)

print("--------------------------------------------------")
print("№ п/п | С/г культура | План | Факт | %")
print("--------------------------------------------------")
print(f"{no} | {culture} | {plan} | {fact} | {percentage}")
print("--------------------------------------------------")