n = int(input("Enter number : "))
new = n
fact = 1
while n > 0 :
    fact = fact * n
    n = n - 1

print(f"Factorial of given no.  {new} is {fact}")