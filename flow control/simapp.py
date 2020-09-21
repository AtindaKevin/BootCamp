"""Create a console application that asks that does the following
 -ask the user to set their pin
 -the user has three attempts to log in
 -if the user enters a wrong pin, he can reenter it and display the number of attempts left
 -if attempts are exhausted, display sim blocked
 """
 set_pin = int(input("Set your pin:"))
i = 3
while i>0:
    pin = int(input("Enter your pin:"))
    
    if pin==set_pin:
        print("login successful")
        break
    elif pin!=set_pin:
        i-=1
        if i==0:
            print("sim blocked")
        else:
            print("You have",i,"attempts left")