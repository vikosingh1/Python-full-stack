# Map(): Used to loop around a collection
# Syntax: varname=map(fname,range())
# Type casting is required

# num=lambda n:n
# num_seq=map(num,range(1,11))
# print(list(num_seq))

# num=lambda n:n**2
# square=map(num,range(1,51))
# print(list(square))

# l=['Hello','Python','Data','Science']
# length=lambda n:len(n)
# len_sq=map(length,l)
# print(list(len_sq))

# def fact(n):
#     if n==1 or n==0:
#         return 1
#     return n*fact(n-1)
# t=(2,5,3,4)
# factorial=map(fact,t)
# print(tuple(factorial))

# t='online classes join'.split(' ')
# ext= lambda n:n[0]+n[-1]
# loop=map(ext,t)
# print(list(loop))

# ot=lambda n:(n,n**3)
# loop=map(ot,range(1,6))
# print(dict(loop))

# s='programs on map function'.split(' ')
# rev=lambda n: (n,n[::-1])
# loop=map(rev,s)
# print(dict(loop))

# Filter()
# ========
# even=lambda n:n%2==0
# even_sq=filter(even,range(1,21))
# print(list(even_sq)) 

# WAP to extract string data from a tuple if it is starting with lowercase and ending with uppercase

# a=('sdfgB','DFgh','fghjBB')
# ext=lambda n: 'a'<=n[0]<='z' and 'A'<=n[-1]<='Z'
# ext_sq=filter(ext,a)
# print(tuple(ext_sq))

# l=[1,2,3,4,5,6,7,8,9]
# even=lambda n : n**2 if n%2==0 else n
# even_sq=map(even,l)
# print(list(even_sq)) 

# l=[1,2,3,4,5,6,7,8,9]
# even=lambda n:n%2==0
# even_sq=filter(even,l)
# print(map(list(even_sq)),l) 

# prime=lambda n:n%n==1
# prim_ext=map(prime,range(2,101))
# print(list(prim_ext))