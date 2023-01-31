class Number:
    def sum(self):
        return self.a + self.b
num = Number()
num.a = 10
num.b = 45
s = (f"The sum of a and b is {num.sum()}")
print(s)