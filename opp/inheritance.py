#inheritance
class Person(): #parent class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def output(self):
        return f"{self.name} is {self.age} years old"

#child
class Employees(Person):

    def __init__(self, name, age, dept):
        Person.__init__(self, name, age)
        self.dept = dept
    
    def in_dept(self):
        return f"Is in {self.dept} department"

emp1 =  Employees("kevin", 27, "IT")
print(emp1.output())
print(emp1.in_dept())
