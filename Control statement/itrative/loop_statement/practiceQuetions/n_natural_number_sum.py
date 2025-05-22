# sum n natural number

n = int(input("Enter number: "))

i = 1
num = 2
sum = 0
while i <= n:

    sum = sum + num
    if i < n:
        print(num, end=" + ")
    else :
        print(num, end=" = ")    

    i = i + 1
    num = num + 2    

print(sum)   