class Employee:
    company  = "Visa"
    ecode = 120

class Freelancer:
    company = "Fiver"
    level = 0 

    def upgradeLevel(self):
        self.level = self.level + 1

class Programmer (Employee,Freelancer): #programmer is child attribute and has the attributes of both the parent classes.
    name = "Rohit"

#In programmr class employee ia first so it will hav eemployee attributes first and then freelancer attributes.
#so print(p.company)--> gives "Visa" bcause Employee is first
p = Programmer()
f = Freelancer()
print(p.company)
print(f.company)
print(p.level)
p.upgradeLevel()
print(p.level)

