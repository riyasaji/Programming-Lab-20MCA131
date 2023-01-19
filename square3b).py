list=[]
n=int(input("Enter the number of elements in the lsit: "))
for i in range(0,n):
    value=int(input("Enter the Integer: "))
    list.append(value)

list1=[i*i for i in list]
print("The Squares are :",list1)
