students = []

for i in range(3):
    name = input(f"\nEnter student {i+1}'s name: ")
    courses = input("Enter courses enrolled (comma-separated): ")
    course_set = set(course.strip().title() for course in courses.split(","))
    student = (name, course_set)
    students.append(student)

# Students enrolled in Math
print("\n📘 Students enrolled in Math:")
for student in students:
    if "Math" in student[1]:
        print(f"- {student[0]}")

# Courses all students are taking
shared_courses = students[0][1]
for student in students[1:]:
    shared_courses = shared_courses & student[1]

print("\n👥 Common Courses:", shared_courses)

# Total unique courses
all_courses = set()
for student in students:
    all_courses.update(student[1])

print("📚 Total Unique Courses:", all_courses)
