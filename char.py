str1=str(input("Enter the String: "))
#replacing the second repeated character
char=str1[0]
str1=str1.replace(char,"$")
str1=char+str1[1:]
print("The changed String is : ",str1)