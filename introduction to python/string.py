"""
it is anything that is wrapped in either single/double quotes
"""
firstName = "techcamp"
lname = "atinda"


print(type(firstName))
print(type(lname))
#indexing
"""
How to get a character from a string; string indexing;
it usually starts from 0, the first position.
we use the [x] where x is the index you want to get
"""
 #positive indexing; left to right; starting from 0
print(firstName[3:])
 #negative indexing; from right to left; starting from -1
print(firstName[-6])
#slicing; how to get a char in a string; using [x,y] xis the starting point and y is the stopping index and not included


print(firstName[-4:])
# slicing with steps
print(firstName[::-2])# prints the first character and jumps 2 char,until the end of the string.
#string concatenation ; addition of the variables;