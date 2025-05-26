#heararchical inheritance
class Parent:
    x = 10
    def __init__(self, name):
        self.name = name
        print(id(self))
    
    def home(self):
        print('Home from parent2 class')
    
class Child(Parent):
    
    def home(self):
        print("Home from child") #this method is known as methid over riding or ye python supported hai
        super().home()

class child2(Parent):
    pass
    

obj = Child('Ayush')
print(id(obj))
print(obj.x)
print(obj.name)
obj.home()

obj2 = child2('Ayush')