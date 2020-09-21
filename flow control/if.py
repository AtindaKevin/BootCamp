name=input("Enter your name \n")
Class=input("Enter your class \n")
ClassTeacher=input("Enter class teacher \n")
maths=int(input("Enter maths Mark \n"))
eng=int(input("Enter Eng Mark \n"))
kisw=int(input("Enter kisw Mark \n"))
sci=int(input("Enter sci Mark \n"))
sst=int(input("Enter sst Mark \n"))
average=(maths+eng+kisw+sci+sst)/5
if(average>=80):
    print("Grade: A")
elif(average>=75):
    print("Grade: A-")
elif(average>=70):
    print("Grade: B+")
elif(average>=65):
    print("Grade: B")
elif(average>=60):
    print("Grade: B-")
elif(average>=55):
    print("Grade: C+")
elif(average>=50):
    print("Grade: C")
elif(average>=45):
    print("Grade: C-")
elif(average>=40):
    print("Grade: D+")
elif(average>=35):
    print("Grade: D")
elif(average>=30):
    print("Grade: D-")
else:
    print("Grade: F")

print("NAME: ", name, "CLASS:", Class,"CLASS TEACHER", ClassTeacher, )

print("MATHS:", maths,"ENGLISH:", eng,"KISWAHILI: ", kisw,"SCIENCE: ", sci,"SOCIAL STUDIES", sst )

print("AVERAGE", average)

