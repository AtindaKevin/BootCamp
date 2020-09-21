"""class HumanBeing():
    #Initialization of class
    def __init__(self,name, colour, height,weight, age):
        self.name = name
        self.colour = colour
        self.height = height
        self.weight = weight
        self.age = age
        self.bmi = 0
    #creating methods - functions that are related

    def get_results(self):
        return f"{self.name} is of {self.colour} colour, {self.height} height, {self.age} age"
    
    def calculate_bmi(self):
        height_meters = self.height/100
        self.bmi = self.weight/(height_meters*height_meters)
        return self.bmi


    def mbi_advise(self):
        if self.bmi >= 30 and self.bmi<=39.9:
            return f"you're in the obese range"
        elif self.bmi >= 25 and self.bmi<=29.9:
            return f"you're in the overweight range"
        elif self.bmi >= 18.5 and self.bmi<=24.9:
            return f"you're in the healthy weight range"
        else:
            return f"you're in the underweight range"

#Instatiation
person1 = HumanBeing("Tech","Black", 150,109, 25)
#person2 = HumanBeing("White", 130,29)

result1 = person1.get_results()
print(result1)
result1bmi = person1.calculate_bmi()
print(result1bmi)
new_advise = person1.mbi_advise()
print(new_advise)
#result2 = person1.get_results()
#print(result2)""""
""" 
Create a class called Payroll whose major task is to calculate an individual’s Net Salary(Net-Pay) by 
getting the inputs basic-salary and benefits. Create 5 different class methods which will calculate 
the payee (i.e. Tax), NHIFContribution, NSSFContributions, grossSalary and netSalary.
NB: Use KRA, NHIF and NSSF values provided in the link below.
https://www.aren.co.ke/payroll/taxrates.htm
"""
class PayRoll():

    def __init__(self, basic_salary):
        self.basic_salary = basic_salary
        self.nssf_contribtuion = 400
        self.benefits = 0
        self.nhif_contribution = 0
        self.taxable_income = 0
        

    def NHIFContribution(self):
        if self.basic_salary >= 100000:
            return self.nhif_contribution = 1700
        elif self.basic_salary >= 90000 and self.nhif_contribution < 100000:
            return self.nhif_contribution = 1600
        elif self.basic_salary >= 80000 and self.nhif_contribution < 90000:
            return self.nhif_contribution = 1500
        elif self.basic_salary >= 70000 and self.nhif_contribution < 80000:
            return self.nhif_contribution = 1400
        elif self.basic_salary >= 60000 and self.nhif_contribution < 70000:
            return self.nhif_contribution = 1300
        elif self.basic_salary >= 50000 and self.nhif_contribution < 60000:
            return self.nhif_contribution = 1200
        elif self.basic_salary >= 45000 and self.nhif_contribution < 50000:
            return self.nhif_contribution = 1100
        elif self.basic_salary >= 40000 and self.nhif_contribution < 50000:
            return self.nhif_contribution = 1000
        elif self.basic_salary >= 35000 and self.nhif_contribution < 40000:
            return self.nhif_contribution = 950
        elif self.basic_salary >= 30000 and self.nhif_contribution < 35000:
            self.nhif_contribution = 900
        elif self.basic_salary >= 25000 and self.nhif_contribution < 30000:
            return self.nhif_contribution = 850
        elif self.basic_salary >= 20000 and self.nhif_contribution < 25000:
           return self.nhif_contribution = 750
        elif self.basic_salary >= 15000 and self.nhif_contribution < 20000:
           return self.nhif_contribution = 600
        elif self.basic_salary >= 12000 and self.nhif_contribution < 15000:
            return self.nhif_contribution = 500
        elif self.basic_salary >= 8000 and self.nhif_contribution < 12000:
            return self.nhif_contribution = 400
        elif self.basic_salary >= 6000 and self.nhif_contribution < 8000:
            return self.nhif_contribution = 300
        else:
            return self,nhif_contribution = 150

    def NSSFContributions(self):


    def EmployeeBenefits(self):
        self.benefits = 2400 + 5000 + 20000 + 8000 + 9000 + 25000 

    def TotalTaxableIncome(self):
    self.taxable_income = self.basic_salary + self.benefits
    return self.taxable_income

    def paye(self):
        if self.taxable_income



person1 = PayRoll(30000)


    	




