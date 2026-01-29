'''class person:
    a=10
    b=20
obj=person()
print(obj.a)
print(obj.b)'''

class zoo:
    a='aligator'
    b='bhalu'
    c='cat'
ritika=zoo()
puneet=zoo()

print(zoo.a,zoo.b,zoo.c)
print(ritika.a,ritika.b,ritika.c)
print(puneet.a,puneet.b,puneet.c)
ritika.a='alephant'
print(zoo.a,zoo.b,zoo.c)
print(ritika.a,ritika.b,ritika.c)
print(puneet.a,puneet.b,puneet.c)
puneet.b='bear'
print(zoo.a,zoo.b,zoo.c)
print(ritika.a,ritika.b,ritika.c)
print(puneet.a,puneet.b,puneet.c)
zoo.c='crocodile'
print(ritika.a,ritika.b,ritika.c)
print(puneet.a,puneet.b,puneet.c)


