class Employee:
    company = "Google"
    salary = 500   #ClassAttribute

sam = Employee()
sam.salary = 100  #InstanceAttribute

print(sam.salary)
print(sam.company)

Employee.Age = 40
print(sam.Age)

