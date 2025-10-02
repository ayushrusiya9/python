# ye class ma pdha tha 
# #encapsulation
# class P:
#     # x = 10 #public veriable

#     # def show(self):#public method
#     #     print('from p class')

#     # _x = 10 #protected veriable

#     # def _show(self):#protected method
#     #     print('from p class')

#     __x = 10 #prIVATE veriable

#     def __show(self):#private method
#         print('from p class')

# class C(P):
#     # print(P.__x)    
#     pass

# # obj = C()
# # print(obj.__x)
# # obj.__show()
# print(dir(C))
# obj = C()
# print(obj._P__show())


# ye revision ma pdha tha 
# Encapsulation Example in Python
class P:
    # ---- Public Member ----
    x = 10   # Public variable
    
    def show(self):   # Public method
        print("Public Method: from P class")
    
    # ---- Protected Member ----
    _y = 20   # Protected variable
    
    def _show(self):  # Protected method
        print("Protected Method: from P class")
    
    # ---- Private Member ----
    __z = 30   # Private variable
    
    def __display(self):  # Private method
        print("Private Method: from P class")


class C(P):
    pass


# Object Creation
obj = C()

# --- Public Access ---
print(obj.x)        # Accessible everywhere
obj.show()

# --- Protected Access ---
print(obj._y)       # Accessible (but should be treated as internal use only)
obj._show()

# --- Private Access (Direct:  Error) ---
# print(obj.__z)        #  AttributeError
# obj.__display()       #  AttributeError

# --- Private Access (Indirect: via Name Mangling) ---
print(obj._P__z)        # Accessing private variable
obj._P__display()       # Accessing private method

# obj = C() 
#  print(obj.__x)
#  obj.__show() 
print(dir(C)) 
obj = C() 


