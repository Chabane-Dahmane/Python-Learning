try :
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    x    = input("Enter operator: ")

    if x == "+":
      result = num1 + num2

    elif x == "-":
      result = num1 - num2

    elif x == "*":
      result = num1 * num2

    elif x == "/":
      result = num1 / num2
    else:
        print("Invalid operator")

    if x in ["+", "-", "*", "/"]:
        print("Result =", result)
    
except ValueError :
    print("You must enter a number")

except ZeroDivisionError :
    print("You can't devid  by zero")

finally:
    print("Calculator finished")