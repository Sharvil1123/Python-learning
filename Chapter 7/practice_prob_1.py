# Method -1
# a = int(input("Enter a number = "))
# for i in range(1,11):
#     print(str(i*a))

# Method -2
# a = int(input("Enter a number = "))
# for i in range(1,11):
#     print(str(a)+ "X" + str(i)+ "="+ str(a*i))

#method - 3
a = int(input("Enter a number = "))
for i in range(1,11):
    print(f"{a}X{i}={a*i}")    # this is also known as f string.
