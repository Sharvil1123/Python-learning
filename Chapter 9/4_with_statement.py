# with the 'with statement we can open and close the file without using the f function.'
with open('D:\Python learning\Chapter 9\ sample.txt','r') as a:
    f = a.read()
print(f)
with open('D:\Python learning\Chapter 9\ sample.txt','w') as b:
    k = b.write('hello world')
print(k)

#In this statement, there is no need to close the statement.