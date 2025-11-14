class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def greet(self):
        print(f'Hello my name is {self.name} and age is {self.age}')
    def age1(self):
        print(f'Hello my name is {self.name} and age is {self.age}')


p=person('Govardhan',35)
p.greet()
p.age1()
    
