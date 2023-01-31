with open('D:\Python learning\Chapter 9\samplelog.txt') as f:
    c= f.read().lower()  #this lower will convert the txt in lower characters first and then read all.  
if "Python" in c:
    print("yes")
else:
    print("no")