def percent(marks):
    a = (sum(marks)/400)*100
    return a
marks_1 = [45,78,86,77]
percentage1 = percent(marks_1)
marks_2 = [75,98,88,78]
percentage2 = percent(marks_2)
print(percentage1,"\n",percentage2)