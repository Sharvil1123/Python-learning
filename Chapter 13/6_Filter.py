def Greaterthan5(num):
    if num>5:
        return True
    else:
        return False
g = lambda num: num>50
l = [1,2,57,69,54,23,29]

print(list(filter(Greaterthan5,l )))
print(list(filter(g,l )))