#Check if a number is divisible by 5 and 11.

num = int(input("Enter number : "))

if num % 3 == 0 and num % 5 == 0 :
    print(f"{num} is multiple of both ")
elif num % 5 == 0 :
    print(f"{num} is multiple of 5.")    
elif num % 3 == 0 :
    print(f"{num} is muliple of 3.")
else : 
    print(f"{num} is not multiple of 3, 5")        
