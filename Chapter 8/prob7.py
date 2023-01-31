# Strip function removes the extra spaces of the string.print()
def removestrip(string, word):
    new = string.replace(word,"")
    return new.strip()
s = "    my name is anthony    "
k = removestrip(s, "is")
print(k)