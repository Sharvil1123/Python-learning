#use open function to read a file

f = open('D:\Python learning\Chapter 9\sample.txt',)
#data = f.read()# read all the characters.
data = f.read(5) # read  the first 5 characters.
print(data)
f.close()