D = {
    "kitab":"Book",
    "Pankha":"Fan",
    "Vastu":"Item",
    "Chand" : "Moon",
    "Fool": "Flower"
}
print("options are", D.keys())
c = input("Enter the word = ")
# print("The meaning is = ",D[c]) this line will show error, to not show error we will us ethe following command
print("The meaning is= ",D.get(c)) #this line will not show error if we input the wrong key.


