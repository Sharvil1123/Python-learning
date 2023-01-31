# def sum(n):
#     l = (n*(n+1))/2
#     return l
# l = sum(3)
# print(l)


def recursive_sum(n):
   if n <= 1:
       return n
   else:
       return n + recursive_sum(n-1)

print(recursive_sum(7))
