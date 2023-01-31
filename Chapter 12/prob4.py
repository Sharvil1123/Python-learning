try:
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    c= a/b
    print(c)
except ZeroDivisionError as e:
    print("Infinite")
finally:
    print("Thank you")