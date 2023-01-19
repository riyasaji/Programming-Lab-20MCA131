list1=[]
n=int(input("Enter the number of elements in the lsit of Integer : "))
for i in range(0,n):
    value=int(input("Enter the integer: "))
    list1.append(value)
print("The First list is :",list1)
list2=[]
for i in list1:
    if i%2!=0:
        list2.append(i)
        print("The list after removing even numbers is : \n",list2)

