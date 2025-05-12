class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def introduce(self):
        print(f"Hi, I'm {self.full_name()}, age {self.age}")


class Student(Person):  # Inheriting from Person
    def __init__(self, first_name, last_name, age, gpa):
        super().__init__(first_name, last_name, age)  # Call parent constructor
        self.gpa = gpa

    def is_honor_student(self):
        return self.gpa >= 3.5

    def introduce(self):
        super().introduce()  # Use parent introduce
        print(f"GPA: {self.gpa}")
        print("Honor Student? ✅" if self.is_honor_student()
              else "Honor Student? ❌")


# Loop to handle multiple students
students = []

while True:
    print("\nEnter student info: ")
    fname = input("First name: ")
    lname = input("Last name: ")
    age = int(input("Age: "))
    gpa = float(input("GPA: "))

    student = Student(fname, lname, age, gpa)
    students.append(student)

    more = input("Add another student? (yes/no): ").strip().lower()
    if more != "yes":
        break

# Display all student info
print("\n==== STUDENT PROFILES ====")
for s in students:
    s.introduce()
    print("----------------------")
