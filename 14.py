#for loop
'''for i in range(5):
    print(i, end=' ')'''
#for loop in string
'''for i in 'hello':
    print(i, end=' ')'''
#for loop in list
'''for i in [1, 2, 3, 4, 5]:
    print(i, end=' ')'''
#for loop in tuple
'''for i in (1, 2, 3, 4, 5):
    print(i, end=' ')'''
#for loop in set
'''for i in {1, 2, 3, 4, 5}:
    print(i, end=' ')'''
#for loop in dictionary
'''for i in {'a': 1, 'b': 2, 'c': 3}.values():
    print(i, end=' ')'''
#wap to print first 10 natural numbers
'''for i in range(1, 11):
    print(i, end=' ')'''
#wap to find the length of the collection without using length function
'''a=eval(input("Enter your collection: "))
c=0
for i in a:
    c+=1
print("Length of the collection is:", c)'''
#wap to print number which is divisible by 3 & 5 in between 1 to 50
'''for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=' ')'''
#wap to print number which is divisible by 3 & 5 in between 1 to 50 if number is even print cube of it if odd square of it
'''for i in range(1, 51):
        if i % 2 == 0:
            print(i**3, end=' ')
        else:
            print(i**2, end=' ')'''
#wap to extract all the upper alphabates from a given strings
'''a='ABCDEFabbbb'
out=''
for i in a:
    if 'A' <= i <= 'Z':
        out+=i
print("Upper case letters are:", out)'''

'''a='ABCDEFabbbb'
out=''
for i in range(0,len(a)):
    if 'A' <= a[i] <= 'Z':
        out+=a[i]
print("Upper case letters are:", out)'''

#wap to extract all the integer from a given set
a=eval(input("Enter your collection: "))
out=set()
for i in a:
    if type(i) == int:
        out.add(i)
print("Integer values are:", out)
