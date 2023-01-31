class Person:
    country = "india"
    def TakeBreath(self):
        
        print("I am breathing...")

class Employee(Person):
    company = "Hyundai"
    salary = 1000

    def GetSalary(self):
        print(f"The salary is {self.salary}")

    def TakeBreath(self):
        super().TakeBreath()
        print("I am Employee so I am Breathing...")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        print("Initializing Programmer...\n")

    def GetSalary(self):
        print("No salary for programmers")

    def TakeBreath(self):
        super().TakeBreath
        print("I am programmer, so I am breathing+++")

p = Person()
p.TakeBreath()

e = Employee()
e.TakeBreath()

pr = Programmer()
pr.TakeBreath()
