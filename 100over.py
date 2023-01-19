list1=[]
n=int(input("Enter the number of elements in the lsit 1: "))
for i in range(0,n):
    value=eval(input("Enter the element: "))
    list1.append(value)
print("The original  List is :",list1)

for i in range(0, int(len(list1))):
    if list1[i] >= 100:
       list1[i]="over"

print("The edited list is : ")
print(list1)
