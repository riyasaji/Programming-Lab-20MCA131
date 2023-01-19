first=int(input("Enter the first number: "))
second=int(input("Enter the second number: "))
third=int(input("Enter the third number: "))
if (first >= second) and (first >= third):
   largest = first
elif (second >= first) and (second >= third):
   largest = second
else:
   largest = third

print("The largest number is", largest)
