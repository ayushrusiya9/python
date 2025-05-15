# def hello():
#     # pass
#     # return None
#     return "hello"
#     # return ''
#     # print("hello")

# # hello()
# # x = hello()
# print(x)
# print(x)
# print(x)
# print(hello())
def naturalNumber(n):
    sum = 0

    # natural number code for print and sum
    for i in range(1, n+ 1):
        sum = sum + i

    # even number code for print and sum
    # for i in range(2, n+ 1, 2):
    #     sum = sum + i
    
    # odd number code for print and sum
    for i in range(1, n+ 1, 2):
        sum = sum + i

    return sum


x = int(input("Enter number: "))

print("sum of odd number", naturalNumber(x))


