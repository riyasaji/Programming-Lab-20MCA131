# swap first and last character
string=input("Enter the string: ")
x=list(string)
# storing the first character
start = string[0]
# storing the last character
end = string[-1]
swapped_string = end + string[1:-1] + start
print("The original string is PYTHON ")
print("Th e swapped string is :",swapped_string )