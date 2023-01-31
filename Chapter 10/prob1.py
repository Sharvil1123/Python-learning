# class programmer:
#     comapny = "Microsoft"

# Sam = programmer()
# Ram = programmer()
# Sham = programmer()
# Sonu= programmer()
# print(f"Sam works in {Sam.comapny}")
# print(f"Ram works in {Ram.comapny}")
# print(f"Sham works in {Sham.comapny}")
# print(f"Sonu works in {Sonu.comapny}")



class Programmer:
    company = "MICROSOFT" 

    def __init__(self,name,product):
        self.name = name
        self.product = product
    
    def GetInfo(self):
        print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}")

sam = Programmer("Sam","GitHub")
ram = Programmer("ram","Visual Studio")
sam.GetInfo()
ram.GetInfo()