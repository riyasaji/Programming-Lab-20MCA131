# Program to copy odd lines of one file to another
# Opening files for reading and writing data
input_file=open('riya.txt')
output_file=open('WriteData.txt','w')

# Copying /reading contents from read_file to copy_data
copy_data=input_file.readlines()
print("\n Actual file is : ")
print(copy_data,"\n")

for i in range(0,len(copy_data)):
    if i%2==0:
        output_file.write(copy_data[i])
    else:
        pass

# Closing file after writing
output_file.close()

# Opening write file in read mode and printing values
output_file=open('WriteData.txt','r')
print("\n Odd Lines Are : ")
print(output_file.read())

# Closing files
input_file.close()
output_file.close()
