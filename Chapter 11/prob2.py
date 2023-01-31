class Animals:
    first = "Dog"
    second = "Cat"
    third = "Goat"
    fourth = "Horse"

class Pet(Animals):
    colour = "golden"
    fur = "fluffy"


class Dog(Pet):
    @staticmethod
    def Bark():
        print("Bhaw Bhaw")

a = Animals()
print(a.third)

c= Dog()
c.Bark()