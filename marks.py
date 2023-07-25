marks=int(input("enter a number"))
if(marks>=90):
    print("A+")
elif(marks>=80 and marks<90):
    print("A")
elif(marks>=70 and marks<79):
    print("B")
elif(marks>=60 and marks<69):
    print("C")
elif(marks>=50 and marks<59):
    print("D")
else:
    print("Fail")