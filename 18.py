#a='python' print op= 'Python' using functions
'''def cap():
    a='python'
    out=''
    for i in a:
        if i==0 and 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
    print(out)
cap()'''

'''a='python'
print(a.capitalize())'''

#wap a='1011100$01!001' then print op= '010011#10#110' 
'''def replace():
    a='1011100$01!001'
    out=''
    for i in a:
        if i=='1':
            out+='0'
        elif i=='0':
            out+='1'
        else:
            out+='#'
    print(out)
replace()'''
#wap to print sum of two numbers
'''def sum(a,b):
    print(a+b)
sum(10,20)
sum(int(input('enter a:')),int(input('enter b:')))'''
#wap to extract all the integers at even index inside a list
'''def even_index():
   a=[10,20,30,40,50,'hello',60,70,80]
    out=[]
    for i in range(len(a)):
        if i%2==0 and type(a[i])==int:
            out+=[a[i]]
    print(out)
even_index()'''

##wap to extract all the integers at even index inside a list check number is pelindrome or not
def even_index():
    a=[121,20,30,44,50,'hello',60,77,88]
    out=[]
    for i in range(len(a)):
        if i%2==0 and type(a[i])==int:
            s=str(a[i])
            if s==s[::-1]:
                out+=[a[i]]
    print(out)
even_index()
