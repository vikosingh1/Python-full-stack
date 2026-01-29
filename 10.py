#wap if 10>free, age 55 = 4000, age 56>=/2
'''age=int(input("Enter your age: "))
prize=int(input("Enter prize:"))
if age<=10:
    print("Free")
elif 10<=age<=55:
    print(prize)
elif age>55:
    print(prize/2)'''
#wap to print if the number is divisible by 5 and its even
num=int(input("enter the num: "))
if num%5==0:
    if num%2==0:
        print("even number")
    else:
        print("div but odd")
else:
    print("not div5")