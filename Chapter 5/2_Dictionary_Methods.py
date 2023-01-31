a={
    "harry":"Code" ,
    "marks":"100",
    "b":{"sonu":"monu"},
    3: 5
}
# print(a.keys())  #prints in the form of lists.
# print(type(a.keys()))   # prints class as dict keys.
# print(list(a.keys()))
# print(a.values())
# print(a)
newup={
    "sharvil": "Handsome",
}
a.update(newup)
# print(a) 

# print(a.get("sharvil")) # prints value associated with harry
print(a["sharvil"]) # prints value associated with harry
# # the difference between .get and [] syntax in dictionaries.
# print(a.get("sharvil2")) # throws none as sharvil2 is not present in the dictionary
# print(a["sharvil2"])# throws error as sharvil2 is not present in the dictionary




