num=int(input("Enter a Number: "))
sum=0
temp=num
for i in range(0,len(str(num))):
    digit=num%10
    sum=sum*10+digit
    num=num//10
if temp==sum:
    print("{} is a Palindrome Number".format(temp))
else:
    print("{} is not a Palindrome  Number".format(temp))