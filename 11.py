#A-a
#chr(ord('A') + 32)
#a-A
#chr(ord('a') - 32)
#print a ='hai hello' and op='HAI HELLO' BY using while loop
#a = 'haihello'
#i=0
#out=''
#while i < len(a):
#    if 'a'<=a[i]<='z':
#        out+=chr(ord(a[i]) - 32)
#    i += 1
#print(out)
'''a = 'hai hello'
i=0
out=''
while i < len(a):
    if 'a'<=a[i]<='z':
        out+=chr(ord(a[i]) - 32)
    else:
        out+=a[i]
    i += 1
print(out)'''
#wap to print a='How are you all' and op='HOW_ARE_YOU_ALL' by using while loop
'''a='how are you all'
out=''
i=0
while i<len(a):
    if a[i]==' ':
        out+='_'
    else:
        out+=a[i]
    i+=1
print(out)'''
#wap to print a='collectionc' and op='{'c','3','0','1','2'}
'''a='collectionc'
out={}
i=0
while i<len(a):
    if a.count(a[i])>1:
        out[a[i]]=a.count(a[i])
    i+=1
print(out)'''
#wap a='Hai Hello' op={'Hai',['iah',6,'Hai3'],'Hello':['oiieH,10,'Hello5']}
a='hai hello'.split()
i=0
out={}
while i<len(a):
    out[a[i]]=[a[i][::-1],len(a[i])*2,a[i]+str(len(a[i]))]
    i+=1
print(out)
