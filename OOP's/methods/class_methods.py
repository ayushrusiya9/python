class Student:
    @staticmethod
    def welcome(name):
        print('Welcome!',name)

    school = "shss"
    gread = "10th"

    def __init__(self, name):
        self.n = name
    
    def show_details(self):
        print(self.n)
        print(Student.school)
        print(Student.gread)
        # print(Student.city)
    
    @classmethod
    def update_gread(cls, update):#update veriable 
        cls.gread =  update
    
    # @classmethod # @staticmethod
    # def add_new(cls, city):#add new veriable
    #     cls.city = city

    @staticmethod
    def add_new(cls, cit):
        print(cls)
        print(cit)
    
    @staticmethod
    def thanks(name):
        print("thankyou",name)


Student.welcome('Ayush')

# obj = Student('ayush')
# obj.show_details()
# # obj.update_gread('11th')
# Student.update_gread('11th')
obj1 = Student('asshuu')
# obj1.show_details()
Student.add_new('BHopal','indore')
obj1.show_details()

Student.thanks("ayush")