#TAKING INPUT FOR FIRST LIST
list1=[]
n=int(input("Enter the number of elements in the lsit 1: "))
for i in range(0,n):
    value=int(input("Enter the integer: "))
    list1.append(value)
print("The First list is :",list1)

#PRINTING THE SUM OF FIRST LIST
Sum=sum(list1)
print("The sum of list 1 is :",Sum)

#TAKING INPUT FOR SECOND LIST
list2=[]
n2=int(input("Enter the number of elements in the lsit 2: "))
for i in range(0,n2):
    value2=int(input("Enter the integer: "))
    list2.append(value2)
print("The Second list is :",list2)

#PRINTING THE SUM OF SECOND LIST
Sum1=sum(list2)
print("The sum of list 2 is :",Sum1)

if Sum==Sum1:
    print("The Sum value is equal")
else:
    print("The sum value is Diffdrent")



