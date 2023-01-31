try:
    a=  int(input("Enter the no = "))
    b = 1/a
    print(b)
except Exception as e:
    print(f"The error is {e}")
    exit()

finally:                  #this will print even if we have exited the except program.
    print("We are done")