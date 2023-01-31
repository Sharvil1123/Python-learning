while(True):
    print("Press Q to quit")
    a = input("Enter a no = ")
    if a=='Q':
        break
    try:
        print("Trying...")
        a = int(a)
        if a>6:
            print("You entered a no greater than 6")
    except Exception as e:
        print(f"Your input resulted in an error = {e}")

print("Thanks for playing the game")