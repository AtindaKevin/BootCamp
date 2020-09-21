# they are used when you dont know the number of iterations you intend to make;
#  while loop executes as long as the test expression evaluates to true
#after each iteration it has to check it again
sum = 0
i = 10
while i>=1:
    print(i)
    sum= i + sum
    i-=1
    print(sum)