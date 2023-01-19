list=[]
n=int(input("Enter the number of elements in the lsit: "))
for i in range(0,n):
    value=int(input("Enter the Integer: "))
    list.append(value)

list1=[i for i in list if i>0]
print("The Positive Numbers in the list are: ",list1)