#wap to print all the even numbers from 1 to 100
'''for i in range(1,101):
    if i%2!=0:
        continue
    print(i,end=' ')'''

#extract the uppercase letters from a string using continue statement
'''s=input("Enter your string: ")
for i in s:
    if i!='A' <= i <= 'Z':
        continue
    print(i,end=' ')'''

#wap to find integer from the list using continue statement
'''a=[12,3,'hello',5.6,'a',7,8.9,'b',10]
out=[]
for i in a:
    if type(i)!=int:
        continue
    out+=[i]
print("Integer values are:", out)'''

#wap to find integer from the list using continue statement but integer is pelindrome
'''a=[121,3,'hello',5.6,'a',707,8.9,'b',10]
out=[]
for i in a:
    if not (type(i)==int and str(i)==str(i)[::-1]):
        continue
    out+=[i]
print("Integer pelindrome values are:", out)'''
