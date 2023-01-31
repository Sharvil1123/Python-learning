a = int(input("Enter the number = "))
prime = True
for i in range(2,a):
    if a%i==0:
        prime = False
        break
if prime:
    print("the number is prime")
else:
    print("The number is composite")



