class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
 
    def display_info(self):
        return f"{self.year} {self.make} {self.model}"
    
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Tesla", "Model S", 2023)
 
print(car1.display_info())
print(car2.display_info())
