class RailwayForm:
    FormType= "RailwayForm"
    def printData(self):
        print(f"Name = {self.Name}")
        print(f"Train = {self.Train}") 

App = RailwayForm()
App.Name = "Sharvil"
App.Train = "Rajdhani Express"
App.printData()