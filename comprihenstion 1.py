# #filter
# l=[8,5,2,3]
# even=filter(lambda n:n%2==0,l)
# even_map=map(lambda n:n**2,even)
# print(list(even_map))

def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
prime_iter=filter(isprime,range(2,100))
print(list(prime_iter))
