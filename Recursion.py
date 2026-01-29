def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

a=[1,2,3,4,5]
ot=[]
for i in a:
    ot+=[fact(i)]
print(ot)
#import sys
#print(sys.getrecursionlimit())
#sys.setrecursionlimit(2000)
#wap to extract all the uppercase alphabet from a given extract
'''def cap(a, i=0, out=''):
    if i >= len(a):
        return out
    if 'A' <= a[i] <= 'Z':  
        out += a[i]
    return cap(a, i+1, out)
print(cap("PythOn ProGramMing"))'''
