# normal
my_dict = {}

for i in range(5):
    my_dict[i] = i**2

print(my_dict)

# dict comprehension

my_dict1 = {x:x**2 for x in range(5)}
print(my_dict1)