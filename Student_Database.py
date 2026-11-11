import json
students = {"name" : "ali" , 
           "age" : 18 ,
           "grade": 12,
           "skils" : ["python","HTML","CSS"]
           }

with open("student.json","w")as file:
     json.dump(students,file,indent=4)
#Read the JSON file
with open("student.json","r")as file:
      student = json.load(file)
#Change Ali's grade to 16.
student["grade"] = 16
  #change his age to 19.
student["age"] = 19
#Add a new skill: "JavaScript".
student["skils"].append("JavaScript")
#Add a new key called "university" with value "USTHB".
student["university"] = "USTHB"
#Delete the "age" key.
student.pop("age",None)

try :
      with open("json.file","w") as file:
        json.dump(student,file,indent=4)

      print(student)

      print("Name:", student["name"])
      print("Grade:", student["grade"])
except FileNotFoundError :
      print("The file does not exist!")
except json.JSONDecodeError :
     print("The JSON file is invalid!")
except KeyError :
       print("Missing information:")
    