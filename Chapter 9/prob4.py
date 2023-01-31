with open('D:\Python learning\Chapter 9\words.txt','r') as f:
    content = f.read()
content = content.replace("Donkey", "####@@@@###")
with open('D:\Python learning\Chapter 9\words.txt','w') as f:
    f.write(content)