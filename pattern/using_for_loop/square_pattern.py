row = int(input("ENTER NUMBER: "))

for i in range(1, row + 1):
    print(" * " * row)

def square_pattern(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print() 
        
square_pattern(row)