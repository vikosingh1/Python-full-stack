#intermidiate termination of loop
'''for i in range(1,11):
    if i==7 or i==4:
        break
    print(i,end=' ')'''

'''user_name='admin'
while True:
    uid=input("Enter your user id: ")
    if user_name==uid:
        print("Welcome")
        break
    else:
        print("Enter proper user id")'''

#make a cusino game if the lucky number is 7 you win if no. less then 7 try again if no. greater then 7 better luck next time
'''lucky_num=7
while True:
    num=int(input("Enter your lucky number: "))
    if num==lucky_num:
        print("You win")
        break
    elif num<lucky_num:
        print("Try again")
    else:
        print("Better luck next time")'''

#wap to check the number is prime or not
'''num=int(input("Enter your number: "))
for i in range(2,num):
    if num%i==0:
        print("Not a prime number")
        break
else:
    print("Prime number")'''

#check a list it is homegenous or hectrogenous
'''num=eval(input("Enter your collection: "))
for i in num:
    if type(i)!=type(num[0]):
        print("Hectrogenous list")
        break
else:
    print("Homegenous list")'''
