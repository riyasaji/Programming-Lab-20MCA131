nterms=int(input("How many terms?: "))
n1,n2=0,1
count=0
if nterms<=0:
    print("Please eneter a positive Integer")
elif nterms==1:
    print("Fibonacci Sequence of",nterms," terms :")
    print(n1)
else:
    print("Fibonacci Sequence:")
    for count in range(nterms):
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1