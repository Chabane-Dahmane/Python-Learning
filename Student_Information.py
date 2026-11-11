import json

student = {"name" : "ali" , 
           "age" : 18 ,
           "university" : "USTHB" ,
           "skils" : ["python","HTML","CSS"]
           }
# Convert Python dictionary to JSON string
data = json.dumps(student)
print(data)

# Convert JSON string back to Python dictionary
data2 = json.loads(data)
# Display information
print("name : " ,data2["name"])
print("university : " ,data2["university"] )