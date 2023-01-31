class Employee:
    company = "Google"
    
    def ShowDetails(self):   #Employee is a parent class
        print("This is an employee")

class Programmer (Employee):
    language = "Python"

    def GetLanguage(self):
        print(f"The Language is {self.language}")  #programmer is a child class.
    
    def ShowDetails(self):
        print("This is an programmer")

e = Employee()
e.ShowDetails() 
p = Programmer()
p.ShowDetails()
p.GetLanguage()
print(e.company)
