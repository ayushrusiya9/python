class Sudent:
    school = "shhss"  # declaration inside class body

    def __init__(self, name):  # constructor needs a 'name' argument
        self.n = name
        Sudent.school_code = 101  # inside constructor
        print(Sudent.school)

    def addNew(self):
        Sudent.school_city = 'BHopal'  # inside instance method
        print(Sudent.school_city, Sudent.school_code)

    def Display(self):
        print(Sudent.gread)

Sudent.gread = "10th"  # outside of class

obj = Sudent("Unnamed")  # name argument required
obj.addNew()
obj.Display()

obj1 = Sudent('Ayush')
# obj2 = Sudent('Rahul')

print(Sudent.school)
# print(obj1.school)
# print(obj2.school)
