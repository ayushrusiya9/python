class Student:
    def __init__(self,name,city):
        self.n = name #inside constructer // instance veriable
        self.c = city
        print(self.n,self.c)#access inside constructer    

    def add(self,phone):
        self.p = phone #inside instance method (decleration)
        print(self.n,self.c,self.school,self.p)#access inside constructer



obj = Student('ayush','Bhopal') 
# obj.add(1232)
# print(obj.n,obj.c,obj.school,obj.p)
obj.school = 'shhs' #out-side of the class(decleration)
# print(obj.n,obj.c,obj.school,obj.p)
obj.add(1232)

print(obj.n,obj.c,obj.school,obj.p)