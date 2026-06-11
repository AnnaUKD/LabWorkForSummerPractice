print("Завдання 1")

class Student:

    def __init__(self, surname, group, grades):
        self.surname = surname
        self.group = group
        self.grades = grades


# Створюємо звичайну функцію для сортування
def way_to_sort(student):
    return (student.group, student.surname)


# База даних
db = [
    Student("Бондар", "ІПЗ-24-2", [95, 88, 92]),
    Student("Абакумова", "ІПЗ-24-2", [80, 85, 88]),
    Student("Мельник", "ІПЗ-24-1", [100, 98, 95]),
    Student("Юлько", "ІПЗ-24-2", [75, 82, 90]),
]

db.sort(key=way_to_sort)

print("Відсортований список студентів:")
for student in db:
    print(f"Студент: {student.surname}   Група: {student.group}   Оцінки: {student.grades}")

