"""evensum = 0
for i in range(10,21)
    if i%2==0:
        print(i)
        evensum+=i
print(evensum)
"""

"""create an application that asks for a string input
     if a character is upper case, convert it to lower case"""

app = str(input("Please input a string\n:"))
newelements = ""

for elements in app:
    if elements.islower():
        newelements+= elements.upper()
    elif elements.isupper():
        newelements+=elements.lower()
    else:
        newelements +=elements
print("The new string is",newelements)


string_input  = input("Enter a string input:")
print(string_input.swapcase())

movie_loved= input("Enter The Movie You Love:")
for holly_wood in movie_loved: 
    if (holly_wood.isupper()) == True:
        print = (holly_wood.lower())
    else:
        print = (holly_wood)


# automate the grading system to ensure that it uses a for loop to ask for the five subjects marks

student_name = input("Enter your name:\n")
student_class = input("Enter your class:\n")
clclass_teacher =  input("Enter your class teacher's name:\n")

#scores per subject
total_score = 0
subjects = ["math", "Eng", "Kiswahili", "Science", "Social Studies"]
for i in range(len(subjects)):
  
   marks = int(input("What is your" +" "+ subjects[i] +" "+"score:\n"))
   total_score += 