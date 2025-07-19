class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def introduce(self):
        print(f"I'm {self.first_name} {self.last_name}, age {self.age}.")


class Student(Person):
    def __init__(self, first_name, last_name, age, gpa):
        super().__init__(first_name, last_name, age)
        self.gpa = gpa

    def introduce(self):
        print(
            f"Iam Student {self.first_name} {self.last_name}, age {self.age}, GPA: {self.gpa}")


class Teacher(Person):
    def __init__(self, first_name, last_name, age, subject):
        super().__init__(first_name, last_name, age)
        self.subject = subject

    def introduce(self):
        print(
            f"I'm Teacher {self.first_name} {self.last_name}, age {self.age}, teaches {self.subject}")


people = [
    Student("Mike", "Smith", 31, 3.9),
    Teacher("John", "Dice", 40, "Math"),
    Person("Zaid", "Jaan", 29)
]

print("\n=== Introductions ===")
for p in people:
    p.introduce()
