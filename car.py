class car :
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year

    def show_info(self):
        print("Brand : ",self.brand)
        print("Year : ",self.year)

car1 = car("Toyota", 2022)
car2 = car("BMW", 2025)

car1.show_info()
car2.show_info()                      