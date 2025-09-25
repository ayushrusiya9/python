# import functools # most imp because reduce functool ke ander likha hai
# 1st way functools.reduce(fun_name, collection)


from functools import reduce # using pattern 

# reduce(func_name, collection)



# def max_n0(x,y):
#     if x > y:
#         return x
#     else:
#         return y    

# def min_no(x,y):
#     if x < y:
#         return x
#     else:
#         return y    

# m = l[0]
# for i in l:

l = [1,2,3,4,5,6,7,8,9,10]
l2 = [1,2,3,4,5,6,7,8,9,10]

def totalSum(x,y):
    return x + y



j = reduce(totalSum, list(map(totalSum, l)))
print(j)

# print(m)    


# x = reduce(max_n0, l)
# x = reduce(min_no, l)
# x = reduce(max, l)

# print(x)