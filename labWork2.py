print("Завдання 1")

first_number = int(input("Введіть перше ціле число: "))
second_number = int(input("Введіть друге ціле число: "))
third_number = int(input("Введіть третє ціле число: "))

numbers_to_sort = [first_number, second_number, third_number]

def sort_numbers_by_modules(numbers_to_sort):
    return sorted(numbers_to_sort, key=abs)
print(f"Відсортовані числа в порядку зростання модулів {sort_numbers_by_modules(numbers_to_sort)}")