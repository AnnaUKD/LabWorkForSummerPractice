print("Завдання 1")

first_number = int(input("Введіть перше ціле число: "))
second_number = int(input("Введіть друге ціле число: "))
third_number = int(input("Введіть третє ціле число: "))

numbers_to_sort = [first_number, second_number, third_number]

def sort_numbers_by_modules(numbers_to_sort):
    return sorted(numbers_to_sort, key=abs)
print(f"Відсортовані числа в порядку зростання модулів {sort_numbers_by_modules(numbers_to_sort)}")


print("Завдання 2")

def process_numbers(total_sum=0, count=0):
    num = float(input("Введіть число (0 для завершення): "))

    if num == 0:
        return total_sum, count
    if num % 2 == 0 and num > 8:
        return process_numbers(total_sum + num, count + 1)
    else:
        return process_numbers(total_sum, count)

final_sum, final_count = process_numbers()

print(f"Сума чисел, які задовільняють умову: {final_sum}")
print(f"Кількість чисел, які задовільняють умову: {final_count}")


print("Завдання 3")

planets = {
    1: "Меркурій",
    2: "Венера",
    3: "Земля",
    4: "Марс",
    5: "Юпітер",
    6: "Сатурн",
    7: "Уран",
    8: "Нептун"
}

number = int(input("Введіть порядковий номер планети (1-8): "))

if number in planets:
    print(f"Планета №{number} — це {planets[number]}.")
else:
    print("У Сонячній системі лише 8 планет. Введіть число від 1 до 8.")


print("Завдання 4")

total_sum = 0
count = 0

while True:
    num = float(input("Введіть число (0 для завершення): "))
    if num == 0:
        break
    if num % 2 == 0 and num > 8:
        total_sum += num
        count += 1

print(f"Сума чисел, які задовільняють умову: {total_sum}")
print(f"Кількість чисел, які задовільняють умову: {count}")