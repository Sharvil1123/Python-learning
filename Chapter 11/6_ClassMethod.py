class Employee:
    company = "camel"
    salary = 100
    location = "Delhi"

    # def ChangeSalary(self, sal):
    #     self.__class__.salary = sal

    @classmethod  #this class method will change the class attribute and we not need to create 
                  # an instance attribute.
    def ChangeSalary(cls, sal):
        cls.salary = sal

e = Employee()
print(e.salary)
e.ChangeSalary(200)
print(e.salary)