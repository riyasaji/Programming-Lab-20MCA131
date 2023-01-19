str1=input("Enter the String: ")
count=0
word=str(input("Count of which word in the string: "))
sp=str.split("")
for i in sp:
    if(i==word):
        count=count+1
    print(count)