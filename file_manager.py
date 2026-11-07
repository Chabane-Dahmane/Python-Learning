with open("students.txt","w") as file :
    name = input("Enter student name: ")
    age = int(input("Enter student age:"))
    file.write(f"Name: {name}, Age: {age}\n")

print("Student saved successfully!")


while True :
    add = input("add another student?")
    if add.lower() != "yes" :
       break
  
    with open("students.txt","a") as file :
          name = input("Enter student name: ")
          age = int(input("Enter student age:"))
          file.write(f"Name: {name}, Age: {age}\n")

print("Student saved successfully!")  

print("---Student list---")
with open("students.txt","r") as file :
    for line in file :
        print(line)