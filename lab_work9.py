print("Задача 1")

a = 2.0
product = 1.0

for _ in range(5):
    product *= a
    a = a - 1 / (a**2) - 1 / (a**3)

print("Добуток обчислювань:", product)

print("Задача 2")

def entering_numbers():
    return float(input("x: ")), float(input("y: ")), float(input("z: "))


def find_max(a, b, c):
    res = a
    if b > res: res = b
    if c > res: res = c
    return res

def find_min(a, b, c):
    res = a
    if b < res: res = b
    if c < res: res = c
    return res

def result(res):
    print("Результат:", res)

x, y, z = entering_numbers()

denominator  = find_min(x, y, z)

if denominator  != 0:
    numerator  = find_max(x, y, z) * find_min(y, z, z) * find_min(x, y, y)
    result(numerator / denominator )
else:
    print("Помилка: ділення на нуль!")


print("Задача 3")

def is_palindrome(number):
    s = str(number)
    return s == s[::-1]

num = int(input("Введіть натуральне число: "))

if is_palindrome(num):
    print(f"Число {num} є паліндромом.")
else:
    print(f"Число {num} не є паліндромом.")