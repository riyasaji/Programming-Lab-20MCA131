num = int(input("Enter a number: "))
f = 1
i = 1
while i <= num:
    f= f * i
    i = i + 1

print("factorial of ", num, " is ", f)