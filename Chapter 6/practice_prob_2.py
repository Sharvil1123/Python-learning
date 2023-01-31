sub1 = int(input("Enter marks for subject 1 = "))
sub2 = int(input("Enter marks for subject 2 = "))
sub3 = int(input("Enter marks for subject 3 = "))
if(sub1<33 or sub2<33 or sub3<33):
    print("Yor are failed because you have less than 33% marks")
elif(sub1+sub2+sub3/3 < 40):
    print("You are failed ")
else:
    print("Congrats! You have successfully passed the exam.")