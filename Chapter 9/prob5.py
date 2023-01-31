words= ["Donkey","Idiot","Stupid"]



with open('D:\Python learning\Chapter 9\words.txt','r') as f:
    content = f.read()

for word in words:
    content = content.replace(word ,"####@@@@###")
with open('D:\Python learning\Chapter 9\words.txt','w') as f:
    f.write(content)