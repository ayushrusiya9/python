#multiple inharitance
class Parent1:
    def car(self):
        print('Car from parent1....')

class Parent2:
    x = 10
    def __init__(self, name):
        self.name = name
        print(id(self))
    
    def home(self):
        print('Home from parent2 class')
    
class Child(Parent1, Parent2):
    
    def home(self):
        print("Home from child") #this method is known as methid over riding or ye python supported hai
        super().home()

    

obj = Child('Ayush')
print(id(obj))
print(obj.x)
print(obj.name)
obj.home()
obj.car()