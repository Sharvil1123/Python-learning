class Calculator:
    def __init__(self, num):   #Created  a constructed 
        self.num =  num

    def Square(self):   # created functions to perform operations.
        print(f"The square of {self.num} is {self.num**2}")

    def Cube(self):
        print(f"The Cube of {self.num} is {self.num**3}")

    def SquareRoot(self):
        print(f"The SquareRoot of {self.num} is {self.num**0.5}")

a = Calculator(10)
a.Square()
a.SquareRoot()
a.Cube()

        