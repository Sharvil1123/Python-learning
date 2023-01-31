a = 54 # Global Keyword
def func():
    global a
    print(f"Print statement 1 = {a}")
    a = 8 #Local variable if global keyword is not used
    print(f"Print statement 2 = {a}")

func()
print(f"Print statement 3 = {a}")

    