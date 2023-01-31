class Train:
    def __init__(self,TID,Seats,Fare):
        self.TID = TID
        self.Seats = Seats
        self.Fare = Fare

    def GetTrainID(self):
        print(f"The Train Id is {self.TID} ")

    def GetSeats(self):
        print(f"The no of seats for {self.TID} is {self.Seats}")

    def GetFare(self):
        print(f"The fare for the {self.TID} is Rs.{self.Fare}")

    def BookTicket(self):
        if (self.Seats>0):
            print(f"Your ticket is booked! your seat no is {self.Seats}")
            self.Seats = self.Seats-1 
        else:
            print("Your Ticket is not booked")

BigCity = Train("Soma Express",3,999)
BigCity.BookTicket()
BigCity.GetSeats()
BigCity.BookTicket()
BigCity.BookTicket()
BigCity.BookTicket()
BigCity.GetSeats()
