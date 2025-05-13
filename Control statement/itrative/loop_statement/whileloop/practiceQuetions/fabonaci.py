n = int(input("Enter number: "))

x,y,i = 0, 1, 1

while i <= n :

    z = x + y
    x, y = y, z
    if i < n :
        print(z, end=",")
    else:
        print(z)    
    i = i + 1 