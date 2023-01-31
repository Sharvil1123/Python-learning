class Employee:
    company = "Google"

    def __init__(self,name,salary,subunit): #initialised first when program is  
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created")

    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")

#     def GetSalary(self, signature):
#         print(f"The salary for the employee working in the {self.company} is {self.salary}\n\t----{signature}") 

sam = Employee("sam",500,"Apple")
savi = Employee("sharvil", 5000, "contra")
# sam.getDetails()
savi.getDetails()



