a=set()

# Adding values 
a.add(2)
a.add(3)
a.add(5)
a.add(9)
a.add(2) # set is non repetitive     
a.add((1, 4, 6))  # you can add tuples in the sets.
# a.add({1:3}) # You can't add list and dictionaries  in the set because list and dictionary is changeable while set is not.
print(a)
# a.remove(2) # reomves 5 from the set
# print(a.pop())
# print(a.clear())
# print(len(a))