def square(num):
    return num*num

l = [1,2,4,5,6]
#method 1
l2=[]
for item in l:
    l2.append(square(item))
print(l2)

#method-2 MAP
print(list(map(square,l)))