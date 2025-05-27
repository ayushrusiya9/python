from abc import ABC, abstractmethod

class senior(ABC):
    def add(self,x,y):
        print(x+y)

    def sub(self,x,y):
        print(x-y)

    def multi(self,x,y):
        print(x*y)

    @abstractmethod
    def div(self,x,y):
        pass

class junior(senior):
    def div(self,x,y):
        print(x/y)
    
obj = junior()
obj.div(2,5)
obj.add(10,20)