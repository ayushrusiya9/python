# even number
# num = int(input("Enter numer : "))

# if num % 2 == 0 :
#     print(f'{num} is even. ')
# else : 
#     print(f'{num} is not even. ')



# odd number

# num = int(input("Enter numer : "))

# if num % 2 != 0 :
#     print(f'{num} is odd. ')
# else : 
#     print(f'{num} is not odd. ')


#leap year

# year = int(input("Enter year : "))

# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
#     print(f"{year} is leap year.")
# else :
#     print(f"{year} is not leap year.")    

h = int(input("Enter hindi marks : "))
e = int(input("Enter English marks : "))
m = int(input("Enter Maths marks : "))

if (h >= 0 and h <= 100 and e >= 0 and e <= 100 and m >= 0 and m <= 100) :
   
    avg = h + e + m / 3 
   
    if avg >= 60 :
        print(f"{avg} First division.")
    elif avg >= 45 and avg <= 59 :
        print(f"{avg}  second division.")
    elif avg >= 35 and avg <= 44 :
        print(f"{avg}  third division.") 
    else :
        print(f"Fail!")            
else:
    print(f"you enter invalid marks!")      



# run time ma usr se value lena hai or check krna hai ki konsa data type hai if eslse ke through check krna hai  