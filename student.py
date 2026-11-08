class students:
    def __init__(self,name,age,grade):
        self.name = name 
        self.age = age
        self.grade = grade

    def show_info(self):
        print("name :",self.name)
        print("age : ",self.age )
        print("grade : ",self.grade)
    def is_passed(self):
        if self.grade>= 10 :
            print("Passed")
        else :
            print("Faild")

stu1 = students("Ali",12,12)
stu2 = students("Dah",18,9)
stu1.show_info()
stu1.is_passed()
stu2.show_info()
stu2.is_passed()

