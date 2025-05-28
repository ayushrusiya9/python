#polymorphishm
class Student:
    def __init__(self):
        print("from 1st constructer")
    
    def __init__(self,x,y,z): #ye method overlod ho rhi hai
        print("From 2nd constructer")

obj = Student(1,2,34)
