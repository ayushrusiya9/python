#multilevel inharitance
class grandParent:
    def car(self):
        print('Car from dada jii....')

class Parent(grandParent):
    x = 10
    def __init__(self, name):
        self.name = name
        print(id(self))
    
    def home(self):
        print('Home from parent class')
    
class Child(Parent):
    
    def home(self):
        print("Home from child") #this method is known as methid over riding or ye python supported hai
        super().home()

    

obj = Child('Ayush')
print(id(obj))
print(obj.x)
print(obj.name)
obj.home()
obj.car()