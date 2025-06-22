# normal 
square = set()
for i in range(10):
    square.add(i**2)

print(square)

# set comprehension

square = {x**2 for x in range(10)}
print(square)