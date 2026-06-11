from lab_work10_task1 import Student

print("Завдання 2")

class ScholarshipStudent(Student):
    def __init__(self, surname, group, grades, amount, topic):
        super().__init__(surname, group, grades)
        self.amount = amount
        self.topic = topic


def check_student(student):
    print(f"Степидіант: {student.surname}")
    print(f"Група: {student.group}")
    print(f"Оцінки: {student.grades}")
    print(f"Розмір стипендії: {student.amount} грн")
    print(f"Тема дослідження: '{student.topic}'")

if __name__ == "__main__":
    print("Вітайте нашу стипендіантку!")

    scholar = ScholarshipStudent(
        "Терешко",
        "ІПЗс-24-2",
        [100, 98, 95],
        2000,
        "ШІ в медицині",
    )

    check_student(scholar)