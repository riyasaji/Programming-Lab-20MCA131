num=int(input("Enter 3-digit Number: "))
sum=0
temp=num
for i in range(num):
    digit=num%10
    c=digit*digit*digit
    sum=sum+c
    num=num//10
if temp==sum:
    print("{} is an Armstrong Number".format(temp))
else:
    print("{} is not an Armstrong Number".format(temp))