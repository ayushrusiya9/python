#hybrid inharitance
class A:
    def first(self):
        print("from class A")

class B:
    def first(self):
        print("from class B")

class C(A):
    pass

class D(B):
    pass

class E(D,C):#dedth first algorithm/ oe isi ko mro(method resolution order)
    pass

obj = E()
obj.first()