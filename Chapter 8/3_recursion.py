# factorial is n! = 5 * 4* 3*2*1
#can be also written as n! = [1*2*3...*(n-1)]*n
# n!= n*(n-1)!

# 1.using for loop


# def factorial_loop(n):
#     fact = 1
#     for i in range(n):
#         fact = fact * (i+1)
#     return fact

# l = factorial_loop(10)
# print(l)

# 2 using recursive function
def factorial_recursion(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recursion(n-1)

p = factorial_recursion(5)
print(p)
