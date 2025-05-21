class First:
    # " hello "
    # pass
    def __init__(self):#self ke badle kuch bhi likh sakt hai self ek refference veriable hai jo current obj ka addrss hold krega
        print("Constructer called")
        print(id(self))

# obj = First
obj = First()
print(id(obj))
# print(dir(First))
# print(First.__doc__)
# print(id(First))
# obj = First
# obj1 = First()
# print(id(obj))
# print(id(obj1))

# print(First is obj)