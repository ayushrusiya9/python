#sum of even number upto n natural

n = int(input("Enter number: "))

i = 1
sum = 0
while i <= n:

    if i % 2 == 0 :
        sum = sum + i

        if i < (n - 1):
             print(i, end=" + ")
        else :
            print(i, end=" = ")     

    i = i + 1

print(sum)