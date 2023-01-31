for i in range(10):
    print(i)
    if i == 7:        # break statement breaks the loop through the given condition.and the else statement will not be executed because the loop did not end naturally.
        break
else:
    print("done with the loop")