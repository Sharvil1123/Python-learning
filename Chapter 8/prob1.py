# Method 1
# def greatest(a,b,c):
#     if (a>b):
#         x = a
#     else:
#         x = b
    
#     if(a>c):
#         y = a
#     else:
#         y = c
    
#     if (x>y):
#         return x
#     else:
#         return y
    
# l = greatest(854,62,98)
# print("The greatest no is "+ str(l))

# Method- 2

def max(n1,n2,n3):
    if(n1>n2):
        if(n1>n3):
            return n1
        else:
            return n3
    else:
        if(n2>n3):
            return n2
        else:
            return n3

l = max(5454, 5466, 4687)
print(f"The greatest no is {l}")