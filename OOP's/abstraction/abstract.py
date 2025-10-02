from abc import ABC, abstractmethod # abs stands for Abstract Base Class

# Abstract Class
class senior(ABC):
    
    # Normal concrete methods (implemented methods)
    def add(self, x, y):
        print(x + y)

    def sub(self, x, y):
        print(x - y)

    def multi(self, x, y):
        print(x * y)

    # Abstract method (no implementation here)
    @abstractmethod
    def div(self, x, y):
        pass


# Child class (must implement abstract methods)
class junior(senior):
    def div(self, x, y):   # Abstract method implemented
        print(x / y)


# Object creation
obj = junior()
obj.div(2, 5)      # Calls child class method
obj.add(10, 20)    # Inherited method from parent
