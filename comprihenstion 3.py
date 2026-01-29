#Genrator yield
# def gn_sq():
#     for i in range (1,11):
#         yield i**2
# print(list(gn_sq()))

#wap to extract all the string from the list collection only if it is pelindrome.
# l=[96,'aba','hello',89,6.3,'uganda','nayan']
# def fn():
#     for i in l:
#         if i==i[::-1] and type(i)==str:
#             yield i
# print(list(l))

#wap to get the following output
# out={'A':65,'B':66,'C':67....'Z':90}
# def fn():
#     for i in range(65,91):
#         yield (chr(i),i)
# print(dict(fn()))

#wap to extract all thwe prime numbers between the range of 2 to 100
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def prime_seq(m,n):
    for i in range(m,n+1):
        if is_prime(i)==True:
            yield i
print(list(prime_seq(2,100)))