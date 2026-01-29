#wap to find factorial between 1 to 10 inside list using recursion
'''def fact(n):
    if  n==0 or n==1:
        return 1
    return n*fact(n-1)
def ex_fact():
    out=[]
    for i in range (1,11):
        out+=[fact(i)]
    return out
print(ex_fact())'''

'''def kill():
    print('hello')
    yield 1
    print("hiee")
    yield 2
    print("bye")
    yield 3
print(list(kill()))'''

#wap to extract all the numbers from a given list
'''def ex_int(a):
    out=[]
    for i in a:
        if type(i)==int:
            out+=[i]
    return out
print(ex_int([1,2,3,24,'hrllo']))

def ext_int(a):
    for i in a:
        if type(i)==int:
            yield i
print(list(ext_int([1,2,3,34,'hello',56])))'''

#a=[12,'Hello',7777,[1,2,3],313] then print op=[[7777,4],[313,3]]
'''def new():
    a=[12,'Hello',7777,[1,2,3],313] 
    for i in a:
        if type(i)==int and str(i)==str(i)[::-1]:
            yield (i,len(str(i)))
print(list(new()))'''

#wap to find prime number 1 to 1000
'''def prime(num):
    for i in range(2,num):
        if num%i==0:
            return 'not prime'
    return 'prime'
def is_prime():
    for i in range (1,1001):
        if prime(i)=='prime':
            yield i
print(list(is_prime()))'''

#wap to find perfect no. between 1 to 1000
'''def perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return 'perfect'
    return 'not perfect'
def ex_perfect():
    for i in range (1,1001):
        if perfect(i)=='perfect':
            yield i
print(list(ex_perfect()))'''


    