with open('D:\Python learning\Chapter 9\poems.txt','r') as f:
    a = f.read()

if "Twinkle" in a:
    print("Present")
else:
    print("Not Present")