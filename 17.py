#nested for loop
'''for i in range(1,10,2):
    #for j in range(2,7,3):
    for j in 'python':
        print(i,j+str(i))'''

#wap a=['How', 'are', 'you', 'all'] to print op=[1,2,2,1]
'''a=['How', 'are', 'you', 'all']
out=[]
for i in a:
    c=0
    for j in i:
        if j in 'aeiouAEIOU':
            c+=1
    out+=[c]
print(out)'''

#wap to print factorial of the number from range 1 to 10 but it stored in list 
'''out=[]
for i in range(1,11):
    f=1
    for j in range(1,i+1):
        f*=j
    out+=[f]
print(out)'''

#print a=[10,'Hai',3+5j,123] then output is op=[1,6]
a=[10,'Hai',3+5j,123]
out=[]
for i in a:
    if type(i)!=int:
         sum=0
    for j in str(i):
        sum+=int(j)
    out+=[sum]
print(out)

#find perfect number from 1 to 100

   
