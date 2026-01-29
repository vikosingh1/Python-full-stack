#wap a='abcdabc' op='a1b2c3d4a1b2c3' by using ascii
'''a='abcdabc'
op=''
i=0
while i<len(a):
    op+=a[i]+str(ord(a[i])-96)
    i+=1
print(op)'''
#wap a='Hello' b='bye' op='Hbeylelo'
'''a='hello'
b='bye'
out=''
i=0
while i<len(a) or i<len(b):
    if i<len(a):
        out+=a[i]
    if i<len(b):
        out+=b[i]
    i+=1
print(out)'''

#wap a=aaabcbb a=a3b1c1b2
a='aaabcbb'
out=''
i=0
c=1
while i < len(a)-1:
    if a[i] == a[i+1]:
        c += 1
    else:
        out += a[i] + str(c)
        c = 1
    i += 1
out += a[-1] + str(c)
print(out)

#wap a = 'python is programming language' op={'p':['python','programming'],'i':['is'],'l':['language']} using loop only


