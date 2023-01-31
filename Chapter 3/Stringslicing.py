#CONCATENATING TWO STRINGS
Name= "Hello, "  
Greeting= "Good morning."
c=Name+Greeting
print(c)
B= "kaku ne kaki"
S= "ko khana diya"
print(B+S) 
Name= "Hello"
print(Name[0])         #index 2 for l in background it is 0,1,2,3,4 for h,e,l,l,o
print(Name[1])
print(Name[2])
print(Name[3])
print(Name[4])
print(Name[0]+Name[1]+Name[2]+Name[3]+Name[4])
print(Name[0:5])    #including 1st and excluding last index
print(Name[0:1])
print(Name[0:2])
print(Name[0:3])
print(Name[0:4])
print(Name[0:5])
print(Name[:5])  # in blank place it considers as 0 automatically
print(Name[1:])   # same as [1:5]
print(Name[-2])  #hello as -5,-4,-3,-2,-1 == h,e,l,l,o
print(Name[-5:-1]) # same as [0:4]
d= "amazing"
print(len(d))
print(d[1:6:1]) #3 is skip index which means it takes every 3rd value
d= "Harryisgood"
print(d[0::3]) 