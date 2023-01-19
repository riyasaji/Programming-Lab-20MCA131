num=int(input("Enter 3-digit Number: "))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit*digit*digit
    temp=temp//10
if sum==num:
    print("It is an Armstrong Number")
else:
    print("It is not an Armstrong Number")