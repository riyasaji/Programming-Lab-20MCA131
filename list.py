list1=[]
n=int(input("Enter the number of elements in the lsit 1: "))
for i in range(0,n):
    value=eval(input("Enter the element: "))
    list1.append(value)
print("The First list is :",list1)

list2=[]
n2=int(input("Enter the number of elements in the lsit 2: "))
for i in range(0,n2):
    value2=eval(input("Enter the element: "))
    list2.append(value2)
print("The Second list is :",list2)

if len(list1)==len(list2):
    print("Both the list are of same size!!!")
else:
    print("Both the list are of different size!!!")

