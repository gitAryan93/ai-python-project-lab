students = []

for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    age = int(input(f"Enter age of student {i+1}: "))
    gpa = float(input(f"Enter GPA of student {i+1}: "))
    student = (name, age, gpa)
    students.append(student)

print("\n🎓 Student Info Summary:")
for student in students:
    print(f"Name: {student[0]} | GPA: {student[2]}")
