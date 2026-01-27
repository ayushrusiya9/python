row = int(input("ENTER NUMBER: "))

for i in range(1, row + 1):
    print(' '*(row - i) + ' *'* i )

def pyramid_pattern(n):
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        for k in range(i + 1):
            print("* ", end="")
        print() 

pyramid_pattern(row)