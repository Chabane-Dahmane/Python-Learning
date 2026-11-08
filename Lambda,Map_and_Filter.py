#Create a lambda function that multiplies two numbers
mul = lambda a,b : a*b 
print(mul(4,5))
numbers = [2, 4, 6, 8, 10]
#Use map() to multiply every number by 3.
mul3 = map(lambda i:i*3 , numbers)
print(list(mul3))

numbers = [5, 12, 17, 20, 25, 30, 33]
#Use filter() to select numbers greater than 20
gr20 = filter(lambda i:i>=2 , numbers)
print(list(gr20))