
# def sqr(a,out=[],i=0):
#     if i >=len(a):
#         return out
#     if i%2==0 and type(a[i])==int:
#         out+=[a[i]**2]
#     else:
#         out+=[a[i]]
#     return sqr(a,out,i+1)
# print(sqr([12,'hai',15,4,[1,2,3],8]))


# def sub(a,b,op='',count_a=0,count_b=0,i=0):
#     if i>=len(a) and i>=len(b):
#         return op
#     if a[i]=='1':
#         count_a+=1
#     if b[i]=='1':
#         count_b+=1
#     op=count_a-count_b
#     return sub(a,b,op,count_a,count_b,i+1)
# print(sub('1101100010101','0011001101000'))

# a='1101100010101'
# b='0011001101000'
# count_a=0
# count_b=0
# i=0
# while i<len(a) or i<len(b):
#     if a[i]=='1':
#         count_a+=1
#     if b[i]=='1':
#         count_b+=1
#     i+=1
# print(count_a-count_b)
    
a=['four','six','zero']
b=['seven','eight','nine']
# ot=0
# i=0
# num={1='one',2='two',3='three',4='four',5='five',6='six',7='seven',8='eight',9='nine',0='zero'}
# while i<len(a) or i<len(b):
#     if a[i] in num.values():
#         ot+=num.key(a[i])
#     if b[i] in num.values():
#         ot+=num.key(b[i])
#         i+=1
# print(ot)

def get(l):
    num={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
    out=''
    for i in l:
        out+=num[i]
    return int(out)
print(get(a)+get(b))
