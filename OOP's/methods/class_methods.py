class Student:
    school = "shss"
    gread = "10th"

    def __init__(self, name):
        self.n = name
    
    def show_details(self):
        print(self.n)
        print(Student.school)
        print(Student.gread)
        print(Student.city)
    
    @classmethod
    def update_gread(cls, update):
        cls.gread =  update
    
    @classmethod
    def add_new(cls, city):
        cls.city = city

# obj = Student('ayush')
# obj.show_details()
# # obj.update_gread('11th')
# Student.update_gread('11th')
obj1 = Student('asshuu')
# obj1.show_details()
Student.add_new('BHopal')
obj1.show_details()