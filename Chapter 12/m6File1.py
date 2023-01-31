def greet(name):
    print(f"Good Morning {name}")

#This will not be imported while importing in the other file.
if __name__ == "__main__":
    n = input("Enter a name = ")
    greet(n)