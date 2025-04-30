
# 7. Convert the following list into a set to remove duplicates: 
#    lst = [10, 20, 20, 30, 40, 40, 50] 

lst = [10, 20, 20, 30, 40, 40, 50]
print(type(lst))
lst = set(lst)


print(lst)
print(type(lst))

# # Given this code: 
#    a = {1, 2, 3} 
#    b = {4, 5, 6} 
#    print(a.isdisjoint(b)) 
#    What will it print and why? 

a = {1, 2, 3} 
b = {4, 5, 6} 
print(a.isdisjoint(b)) 

s = set("banana")
print(s)