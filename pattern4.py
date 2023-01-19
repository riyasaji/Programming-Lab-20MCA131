n=int(input("Enter number of rows: "))
i=1
k=n
while i< =n:
    b=1
    while b<=n-i:
      print(" ",end=" ")
      b+=1
    j=n
    while j<=k:
      print("*",end=" ")
      j-=1
    k=k-2
    print()
    i=i-1
