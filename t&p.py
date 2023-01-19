name=input("Enter the name of the student: ") #nameofstudent
maths=int(input("Enter the marks of Mathematics : ") )#marksofmathematics
eng = int(input("Enter the marks of English : ") )#marksofEnglish
sc = int(input("Enter the marks of Science : ") )#marks0fScience
sst= int(input("Enter the marks of Social Science : ")) #marks of social science
hindi = int(input("Enter the marks of Hindi : ") )#marks of hindi
total=maths+eng+sc+sst+hindi #totalofALLSubject
print("The Total Marks of all subject scored by ",name," : ",total) #printing total of all subjects
percentage=(total/500) *100 #Percentage of all subjects
print("The percentage scored by ",name," :",percentage ,"%") #printing percentage of all sujects

