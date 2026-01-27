row = int(input("ENTER NUMBER: "))

for i in range(0, row):
    print('*'*(row-i))

def upper_left_side_triangle(n):
    for i in range(n):
        for j in range(n - i):
            print("*", end=" ")
        print() 
upper_left_side_triangle(row)
