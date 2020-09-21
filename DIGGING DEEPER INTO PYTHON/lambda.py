"""have a key word lambda
   instead of using a return aspect

 takes only two arguments
   
syntax: only one expression
"""
to_upper = lambda str : str.upper()
print(to_upper("kevin"))

def even_odd(number:int) ->str:
    if number%2 == 0:
        return "even"
    else:
        return "odd"

even_odd = lambda num: "even" if num%2 == 2 else "odd"
print(even_odd(2))