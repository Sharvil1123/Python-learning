class Employee:
    company = "Bharat Gas"
    salary = 1000
    Increment = 1.5

    @property               
    def SalaryAfterIncrement(self):   
        return self.salary * self.Increment

    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self, sai):
        self.Increment = sai/self.salary

e = Employee()
print(e.Increment )
e.SalaryAfterIncrement = 2000
print(e.Increment )
