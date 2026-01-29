'''a=int(input("Enter your no: "))
b=int(input("Enter your no: "))
c=int(input("Enter your no: "))
d=int(input("Enter your no: "))
if a>b>c>d:
    print(a)
elif b>c>d:
    print(b)
elif c>d:
    print(c)
else:
    print(d)'''
a,b,c,d=eval(input("Enter the num: "))
if a>b and a>c and a>d:
    print(a)
elif b>c and b>d:
    print(b)
elif c>d:
    print(c)
else:
    print(d)