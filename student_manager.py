students = []

stu1 = input("Enter student 1: ")
students.append(stu1)

stu2 = input("Enter student 2: ")
students.append(stu2)

stu3 = input("Enter student 3: ")
students.append(stu3)

print("Students:", students)

print("Total students:", len(students))

rem = input("Enter a name to remove: ")

if rem in students:
    students.remove(rem)
    print("Student removed successfully.")
else:
    print("Student not found.")

print("Updated students:", students)