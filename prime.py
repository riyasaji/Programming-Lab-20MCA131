n=int(input("\n Enetr whole number to check: "))
i=2
while i<=(n/2):
    if(n%i)==0:
        flag=1
        break
    i+=1
if n==1:
    print("1 is neither prime nor Composite")
elif flag==0:
    print(n,"is a prime number")
elif flag==1:
    print(n,"is a not a prime number")