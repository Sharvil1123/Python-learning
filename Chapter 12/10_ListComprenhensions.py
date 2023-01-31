a = [4,4,64,65,8,78,65,25,74]
# b= []
# for num in a:
#     if num%2==0:
#         b.append(num)
# print(b)

# List Comprenhension
b = [i for i in a if i%2==0]
c = [i for i in a if i%2==1]
print(b)
print(c)

#can also be done in sets and dictionaries
t= [465,3,8,653,84,56,55]
s= {nos for nos in t if nos%2==1} #sets
print(s)