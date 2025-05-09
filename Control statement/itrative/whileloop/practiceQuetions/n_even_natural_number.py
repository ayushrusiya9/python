#wap to print n even natural number.

n = int(input("Enter number:  "))

i = 1
num = 2
while i <= n:
    
    if i < n:
        print(num, end=',')
    else:
        print(num)    

    num = num + 2
    i = i + 1

