class Student:
    def __init__(self, first_name, last_name, age, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gpa = gpa

    def introduce(self):
        print(
            f"\nHi, I'm {self.first_name} {self.last_name}, age {self.age}, GPA: {self.gpa}")

    def is_honor_student(self):
        return self.gpa >= 3.5

    def get_letter_grade(self):
        if self.gpa >= 3.7:
            return "A"
        elif self.gpa >= 3.0:
            return "B"
        else:
            return "F"

    def full_name(self):
        return f"{self.first_name} {self.last_name}"


# ===  USER INTERACTION / MAIN PROGRAM ===
students = []

num = int(input("How many students do you want to enter? "))

for i in range(num):
    print(f"\n--- Student {i + 1} ---")
    first_name = input("Enter student's first name: ")
    last_name = input("Enter student's last name: ")
    age = int(input("Enter student's age: "))
    gpa = float(input("Enter student's GPA: "))

    student = Student(first_name, last_name, age, gpa)
    students.append(student)

# === OUTPUT REPORT ===
print("\n==== STUDENT REPORT ====")

for s in students:
    print(f"\nName: {s.full_name()}")
    print(f"Age: {s.age}")
    print(f"GPA: {s.gpa}")
    print("Honor Student? ✅" if s.is_honor_student() else "Honor Student? ❌")
    print(f"Letter Grade: {s.get_letter_grade()}")
