"""list1 = [1,2,3,4,5]
#map(function, list) - >
new_list = list(map(lambda  number: number*2,list1))
print(new_list)

list1 = [1,-1,2,3,4,-3,-4,-5,-6]
negative_numbs = list(filter(lambda number : number<0, list1))
"""
from functools import reduce
ls = [1,2,3,4,5]

#reduce function apllies rolling comprehension 
product = reduce(lambda a,b: a*b,ls )
print(product)


