str1=input("Enter the String: ")
if str1[-3:] == 'ing':
      str1+='ly'
else:
      str1 += 'ing'
print("The Convereted string is : ",str1)