def psq(num):
    for i in range(num):
        if i*i==num :
            print(num,end=" ")

num1=int(input("Enter the number: "))
print("The even perfect squares are: ")
psq(num1)