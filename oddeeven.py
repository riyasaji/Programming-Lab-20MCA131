num = int (input("Enter the number: "))
if (num % 2) == 0:
    print("The number is even")
else:
    print("The number is odd")
    print("checking for positive or negative")
    if num>0:
        print("The number is positive")
    elif num==0:
        print("The number is zero")
    else :
        print("The number is negative")
