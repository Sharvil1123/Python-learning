def increment(num):
    try:
        return int(num)
    except:
        raise ValueError("This is invalid value")

a = increment(56)
print(a)