row = int(input("ENTER NUMBER: "))

for i in range(0, row):
    print("*"*(row-i))

# print(i)


for i in range(i, row +1):
    i = i - 1
    print("*" * (row - i))
    