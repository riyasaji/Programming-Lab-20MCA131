str1=input("Message : ")

list1=list(str1) #convert to list in order to take each character
print(str1)

for i in len(list1):
    list1[i]+=ord(list1[i])+1
prin