#List comprehension is a way of creating lists
"""x = [2,3,4,5]
new_list = []
for each in x:
    new_list.append(each *2)
print(new_list)


#comprehension
new_list = [x*2 for x in list]
print(new_list)"""

#name = "techcamp"
#name_list = [char for char in name]
#print(name_list)
"""
construct list that have conditional statements
"""
#even numbers
even_num_list = [num for num in range(1,11) if num %2 == 0]
print(even_num_list)
#odd numbers
even_num_list = [num for num in range(90,100) if num %2 == 1]
print(even_num_list)
#if statement
list2 = [x*2 if X%2 == 0 else x*3  for x in range(1,11)]
print(list2)