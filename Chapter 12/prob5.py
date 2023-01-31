a = int(input("Enter the no = "))
b= [a*i for i in range(1,11)]
print(b)
with open('Tables.txt','w') as f:
    f.write(str(b))
    f.write('\n')