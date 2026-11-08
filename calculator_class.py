class calculator :
    #Create an instance method called multiply(a, b) that returns the multiplication.
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def multiply(self):
        return self.a*self.b
    
    #Create a static method called add(a, b) that returns the addition
    @staticmethod
    def add(a,b):
        return a+b
     
    #Create a class attribute called calculator_name = "My Calculator".
    #Create a class method called change_name(cls, new_name) to change the calculator name.
    calculator_name = "My Calculator"
    @classmethod
    def change_name(cls,new_name):
        cls.calculator_name = new_name

calc = calculator(3, 5)
print(calc.multiply())

print(calculator.add(3,5)) 
calculator.change_name("adv calclulator")
print(calculator.calculator_name)    
        