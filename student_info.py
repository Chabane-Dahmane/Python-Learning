student = {
    "name" : "Ahmed",
    "age" : "18",
    "major" : "computer science"
}

email = input("Enter your Email : ")
student["email"] = email

print("student info : ")
for key,value in student.items():
    print(key, ":" , value)

age = int(input("Enter new age: "))
student["age"]= age

print(" Updated student : ")
for key,value in student.items():
    print(key, ":" , value)

