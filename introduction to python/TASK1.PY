#Question 1
# initializing string 
sentence = "We are learning how to program in python. I find python programming fun"

# using count() method to get count  
python_counter = sentence.count('python')

# printing result  
print ("Python occurs " + str(python_counter) + " times in the sentence.") 

#Question 2; Write a Python function to reverses the word- reven
word = "reven"
reverse = "".join(reversed(word))
print(reverse)

#Question 3; Write a program to check if the letter 'e' is present in the word 'Umbrella'

print("e" in "umbrella")

#Question 4; Write a program that takes your full name as input and displays the abbreviations of the first and middle names except the last name which is displayed as it is. For example, if your name is Robert Brett Roser, then the output should be R.B.Roser.

fName = input("Enter your first name\n")
mName = input("Enter your middle name\n")
lName = input("Enter your last name\n")

print(fName[0]+ "."+ mName[0] + "." +lName)
#Question 5; Write a python program that checks if each letter in a string begins with a capital letter.
a = "apple"
print(a.isupper())
#Question 6; Write a python program to find the index of the first occurrence of a substring in a string below
string = "The worlds fastest plane"
substring = "plane"
index = string.find(substring)
print(index)
#Question 8; Create a sentence from the following variables
print (a+" "+b+" "+c+" "+d+" "+e+" "+f+" "+g+" "+h)
