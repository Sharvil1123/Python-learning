class Employee:
    company = "Google"
    salary = 500   #ClassAttribute

sam = Employee()
Lad = Employee()
sam.salary = 100  #InstanceAttribute
Lad.salary = 145616  #InstanceAttribute

print(sam.salary)
print(Lad.salary)
print(sam.company)

Employee.Age = 40
print(sam.Age)

