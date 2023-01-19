def factorial(num):
    f=1
    for i in range(1, num+1):
        f=f*i
    print(f,end=" ")

num1=int(input("Enter a number: "))
print("Factorial of ",num1,"is :")
factorial(num1)
