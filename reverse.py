num = int(input("Please provide the number to be reversed: "))
revnum = 0
temp = revnum
remainder= 1
for i in range(0,len(str(num))):
 remainder = num %10
 revnum = (revnum*10) + remainder
 num = num //10
print("Reverse of the provided number is = %d" %revnum)