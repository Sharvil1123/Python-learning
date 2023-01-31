class ComplexNum:
    def __init__(self,r,i):
        self.real = r
        self.imaginary = i

    def __add__(self,c):
        return ComplexNum(self.real + c.real, self.imaginary + c.imaginary)

    def __mul__(self,c):
        mulReal = self.real*c.real - self.imaginary*c.imaginary
        mulImg = self.real*c.imaginary + self.imaginary*c.real
        return ComplexNum(mulReal,mulImg)

    def __str__(self):
        if self.imaginary<0:
            return f"{self.real}-{-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"
 

c1 = ComplexNum(3,2)
c2 = ComplexNum(1, 7)
print(c1+c2)
print(c1*c2) 