with open('this.txt') as f:
    c = f.read()
with open('copythis.txt','w') as f:
    f.write(c)