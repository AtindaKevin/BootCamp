"""Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No". 
Hint: Use input () to get the persons input"""

def string(a):
    a = 

"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function
"""

def maylist4(a):
    return[a[0], a[-11]]
print(maylist4(5,10,15,20,25))

"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?  """
num = int(input("Enter a number: "))
check = 4

if (num%2)==0:
   print("{0} is even".format(num))
else:
   print("{0} is odd".format(num))
if num % check == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)

"""With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), write a program to print the first half values in one line and the last half values in one line. """

def func_tuple(a_tuple):
    midpoint = int(len(a_tuple)/2)
    firsthalf = a_tuple[:midpoint]
    lasthalf = a_tuple[midpoint:]
    fh_str = str(firsthalf)
    lh_str = str(lasthalf)
    print(fh_str)
    print(lh_str)
    a = fh_str.strip('()')
    b = lh_str.strip('()')
    print(a)
    print(b)

func_tuple((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
"""Write a program that takes the base and height of a triangle and returns its area"""
def triangle_area(base, height):
    return 0.5*base*height
print(triangle_area(3,5))
"""Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.
Input Format
The first line contains n. The second line contains a list x of i integers each separated by a"""
 no_of_students = int(input("Enter number of students:\n"))
scores = input("Enter student scores:\n").split( )[0:no_of_students]# split method splits a string into a list then we slice the list scores to be equivalent to the number of students
new_scores = list(set(scores))#set removes duplicates
new_scores.sort(reverse=True)
print(new_scores[1])