def game(n):
    return n
score = game(500)
with open('D:\Python learning\Chapter 9\Highscore.txt','r') as f:
    a = f.read()
if f=='':
    with open('D:\Python learning\Chapter 9\Highscore.txt','w') as f:
        f.write(str(score))
elif int(a)<score:
    with open('D:\Python learning\Chapter 9\Highscore.txt','w') as f:
                f.write(str(score))

    
