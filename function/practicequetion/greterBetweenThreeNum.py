
def greaterBtwnThree(a, b, c):

    if a > b and a > c:
        print(f"First {a} is graeter then second {b} and third {c}")
    elif b > a and b > c:
        print(f"Second {b} is graeter then first {a} and third {c}")
    else:
        print(f"Third {c} is graeter then first {a} and second {b}")

'''x = int(input("Enter First Number: "))
y = int(input("Enter Second Number: "))
z = int(input("Enter Third Number: "))'''
 
x,y,z = int(input("Enter First Number: ")),int(input("Enter Second Number: ")),int(input("Enter Third Number: "))

greaterBtwnThree(x,y,z)
