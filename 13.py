#wap to a = 746 print op = 17
'''a=746
op=17
sum=0
while a!=0:
    Id=a%10
    sum=sum+Id
    a=a//10
    print(sum)'''
#make a table 
'''num=int(input("Enter your number: "))
i=1
while i<=11:
    print(num,'*',i,'=',i*num)
    i+=1'''
#wap a='()((())' op=1
'''a='()((())'
i=0
c=0
c1=0
while i<len(a):
    if a[i]=='(':
        c+=1
    elif a[i]==')':
        c1+=1
        i+=1
print(c-c1)=1 / print(c1-c) -1'''
#wap to check string is pelindrome or not without using indexing
'''a='nitin'
i=len(a)-1
out=''
while i>=0:
    out+=a[i]
    i-=1
if out ==a:
    print('pelindrome')
else:
    print('not pelindrome')'''


#perfect no. is a numbers whose sum of factors itself hisself is equal to the same numbers
#wap to check the number is perfect numbers
num=6
i=1
sum=0
while i<num:
    if num%i==0:
        sum+=i
    i+=1
if sum == num:
    print('perfect')