n = int(input("Enter number : "))

# sum = 0
sum = 1
i = 1;
while i <= n:
    # print(i, end = ",")
    # i = i + 1
    sum = sum * i
    if i <= (n - 1) :
        # print(i, end=',')
        print(i, end='+')
    else :
        print(i, end=" = ")
    i = i + 1        
print(sum)