str1 = input("Enter the String: ")

# using set() + count() to get count
# of each element in string
countchar = {i:str1.count(i) for i in set(str1)}

# printing result
print("The count of all characters in string  is :\n "
      + str(countchar))