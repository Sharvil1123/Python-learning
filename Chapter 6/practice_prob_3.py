# First let's give input
text = input("Enter your comment = ")
if("click this " in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
else:
    spam = False

if(spam):
    print("text is spam")
else:
    print("The text is not spam")    


#Using bool we have done this !