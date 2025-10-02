from abstract import senior

class junior(senior):
    def div(self, x, y):   # Abstract method implemented
        print(x / y)

obj = junior()
obj.div(2, 5)      # Calls child class method
obj.add(10, 20)    # Inherited method from parent
