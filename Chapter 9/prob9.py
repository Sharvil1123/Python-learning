# method - 1
# with open('this.txt') as f:
#     c= f.read()
# with open('copythis.txt') as f:
#     k = f.read()
# if c==k:
#     print("Match found")
# else:
#     print("No match found")

#method - 2
f1 = str(input("f1 = "))
f2 = str(input("f2 = "))

with open(f1) as f:
    f1= f.read()
with open(f2) as f:
    f2 = f.read()
if f1==f2:
    print("Match found")
else:
    print("No match found")