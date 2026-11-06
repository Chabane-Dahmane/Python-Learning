student = ("ahmed","ali","youcef")
print("First student : ",student[0])

class_A = {"Ahmed", "Ali", "Sara"}
class_B = {"Ali", "Omar", "Sara"}

print("All Student : " , class_A | class_B)
print("Students in both classes: " , class_A & class_B)
print("Only in class A: " , class_A - class_B)