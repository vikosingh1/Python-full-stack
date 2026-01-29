#wap to create marksheet
marks=int(input("enter your marks: "))
if marks>=80 and marks<=100:
    print("Grade-A")
elif marks>=60 and marks<=79:
    print("Grade-B")
elif marks>=40 and marks<=59:
    print("Grade-C")
elif marks>=30 and marks<=39:
    print("Grade-D")
elif marks<=29:
    print("Fail")