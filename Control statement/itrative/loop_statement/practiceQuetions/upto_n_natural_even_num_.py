# wap to print upto n natural even number

n = int(input("enter number: "))

i = 1
while i <= n :

    if i % 2 == 0:
        # print(i, end=",")
        if i < (n - 1) :
            print(i, end=",")
        else :
            print(i)    

    i = i + 1    