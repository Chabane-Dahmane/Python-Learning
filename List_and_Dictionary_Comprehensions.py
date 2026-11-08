#Create a list containing all even numbers from 1 to 30 using list comprehension
Even_numbers = [i for i in range(1,31) if i%2==0]
print(Even_numbers)

#Create a list containing the squares of numbers from 1 to 10.
Squares = [i*i for i in range(1,11)]
print(Squares)

students = {
    "Ahmed": 15,
    "Ali": 8,
    "Omar": 17,
    "Yacine": 9,
    "Amine": 12
}
#Create a new dictionary containing only students with scores of 10 or higher.
passed_students = {
     name : result
     for name,result in students.items() 
     if result>=10}
print(passed_students)

numbers = [3, 8, 12, 5, 20, 7, 14, 9]
#Create a new list containing the squares of numbers greater than 10.
numbers = [i*i for i in numbers if i>=10 ]
print(numbers)