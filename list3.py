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
list3=[]
for i in list1:
    if i in list2 :
        list3.append(i)
print("The same values are: ",list3)