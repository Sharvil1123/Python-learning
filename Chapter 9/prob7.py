c = True
i=1
with open('D:\Python learning\Chapter 9\samplelog.txt') as f:
    while c:
        c= f.readline()  #this lower will convert the txt in lower characters first and then read all.  
        if 'pythons' in c.lower():
            print(c)
            print(f"yes python is present on line no {i}")
        i+=1