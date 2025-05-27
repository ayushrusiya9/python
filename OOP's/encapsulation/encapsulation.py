#encapsulation
class P:
    # x = 10 #public veriable

    # def show(self):#public method
    #     print('from p class')

    # _x = 10 #protected veriable

    # def _show(self):#protected method
    #     print('from p class')

    __x = 10 #prIVATE veriable

    def __show(self):#private method
        print('from p class')

class C(P):
    # print(P.__x)    
    pass

# obj = C()
# print(obj.__x)
# obj.__show()
print(dir(C))
obj = C()
print(obj._P__show())