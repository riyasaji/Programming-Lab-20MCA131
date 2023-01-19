start=int(input("Enter the Starting Year: "))
end=int(input("Enter the Ending Year: "))
while start>=end:
    print("Check your input again")
    start = int(input("Enter the Starting Year: "))
    end = int(input("Enter the Ending Year: "))

print("Here is a list of leap year between",str(start),"and",str(end),":")

leapy=[]
while start<=end:
    if start%4==0 and start%100!=0:
        leapy.append(str(start))
    if start%100==0 and start%400==0:
        leapy.append(str(start))
    start+=1

for i in range(0,len(leapy),10):
    print("{0}.".format(",".join(leapy[i:i+10])))