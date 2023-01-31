from functools import reduce
sum = lambda a,b: a+b
l = [5,2,3]
val = reduce(sum,l)
print(val)