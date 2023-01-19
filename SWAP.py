#SWAP FIRST AND LAST CHARACTER
string=input("Ennter the string: ")
x=list(string)
#storing the first character
start=string[0]
#storing the last character
end=string[-1]
swapped_string=end+string[1:-1]+start
print("The original string is:",string)
print("The swapped string is:",swapped_string)