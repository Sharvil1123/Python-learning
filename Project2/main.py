import random
randomNum = random.randint(1,25)
print(randomNum)
User = None
GUESS = 0
while User!= randomNum:
    User = int(input("Enter the Guess = "))
    GUESS+=1
    if User==randomNum:
        print("CONGRATULATIONS YOUR GUESS IS CORRECT")
    else:
        if User>randomNum:
            print("OOPS! WRONG GUESS, TRY SMALLER NO")

        else:
           print("OOPS! WRONG GUESS, TRY LARGER NO")


print(f"You Guessed the correct no in {GUESS} Attempts")

with open('Highscore.txt','r') as f:
    Highscore = int(f.read())
if GUESS<Highscore:
    print("You have Just broken the record!")
    with open('Highscore.txt','w') as f:
        f.write(str(GUESS))
    