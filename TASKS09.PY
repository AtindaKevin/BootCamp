import random
# create a program that randomly selects an element from the list below
	#numberList = [111,222,333,444,555]
numberList = [111,222,333,444,555]
print(random.choice(numberList))
 
convertToTuple = tuple([name] for name in numberList)
print(convertToTuple)
print(type(convertToTuple))

