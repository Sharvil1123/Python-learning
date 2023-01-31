class Employee:
    company = "Google"

    def GetSalary(self,signature):
        print(f"Salary for this working Employee of {self.company} is {self.salary}\n{signature}")

    # def greet(self):
    #     print("Good Morning, Sir")

    @staticmethod      #Static method is used if we don't want to use "self" parameter.
    def greet():
        print("Good Morning sir!")    

sam = Employee()
sam.salary= 1000
sam.GetSalary("Thankyou very much") #---> #Employtee.GetSalary(sam)
sam.greet()