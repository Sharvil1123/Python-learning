#use as a property and not a function!
class Employee:
    company = "Bharat Gas"
    salary = 5600
    salarybonus = 400

    @property               #this uses a property as on line no 19 and it is not a function.
    def totalSalary(self):   #this is also a getter
        return self.salary + self.salarybonus

    @totalSalary.setter
    def totalSalary(self, val):
        self.salarybonus = val- self.salary

e = Employee()
print(e.salary)
print(e.salarybonus)
print(e.totalSalary)
e.totalSalary = 6200
print(e.salary)
print(e.salarybonus)
