name=str(input("Enter the name: "))
list1 = list(name.strip(" "))
count=0
for i in list1:
    if i=="a":
        count+=1
print("The total count of a in the name is : ",count)

