# class demo:
#     a=10
#     b=20
# obj=demo()
# print(obj.a)
# print(obj.b)

# class zoo:
#     a='alligator'
#     b='bhalu'

# ankit=zoo()

# print(zoo.a,zoo.b)
# print(ankit.a,ankit.b)
# ankit.a='eliphant'
# print(ankit.a,ankit.b)
# zoo.a='cat'
# print(ankit.a,ankit.b)


## WAP to print a class bank with min 3 static members , 2 objects with 5 object members
# class bank:
#     bname='SBI'
#     bloc='Yammuna parr'      ##Static members
#     bIFSC='SBIN345678'

# ankit=bank()    ## Object

# ankit.name='Ankit'
# ankit.DOb='28-08-2002'
# ankit.addr='Karol Bag'          ##object members
# ankit.phno=9876543210

# print(bank.bIFSC,bank.bloc,bank.bname)
# print(ankit.name,ankit.DOb,ankit.addr,ankit.phno)

##WAP to create a class hospital with min 4 static members with 3 object and 7 object members

# class hospital:
#     hname='GMCH'
#     hloc='Guwahati'
#     htype='Government'
#     hbank='SBI'
    
# Patient1=hospital()
# Patient2=hospital()
# Patient3=hospital()

# Patient1.name='P1'
# Patient1.age=34
# Patient1.gender='Male'
# Patient1.room='R1'
# Patient1.PN=1234567890
# Patient1.doc='Dr.Pal'
# Patient1.diagnos='Cancer'

# Patient2.name='P2'
# Patient2.age=44
# Patient2.gender='Female'
# Patient2.room='R5'
# Patient2.PN=1234396890
# Patient2.doc='Dr.Lal'
# Patient2.diagnos='Polio'

# Patient3.name='P3'
# Patient3.age=67
# Patient3.gender='Male'
# Patient3.room='R4'
# Patient3.PN=1234682890
# Patient3.doc='Dr.Chadda'
# Patient3.diagnos='Tumer'

# print(Patient1.name,Patient1.age,Patient1.gender,Patient1.room,Patient1.PN,Patient1.doc,Patient1.diagnos)
# print(Patient2.name,Patient2.age,Patient2.gender,Patient2.room,Patient2.PN,Patient2.doc,Patient2.diagnos)
# print(Patient3.name,Patient3.age,Patient3.gender,Patient3.room,Patient3.PN,Patient3.doc,Patient3.diagnos)


## GENERATOR
## Using Function

# class bank:
#     bname='HDFC'
#     bIFSC='HDFCN354'
#     bloc='Noida'

#     def details(obj,name,phno,email,addr):
#         obj.name=name
#         obj.phno=phno
#         obj.email=email
#         obj.addr=addr

# ankit=bank()
# ankit.details('ankit',1234567,'asdfg@gmail.com','delhi')
# print(ankit.name,ankit.phno,ankit.email,ankit.addr)


# Using __init__ method
# Constructor: To initialize the object members we need to use __init__ to create all the object members in one go.

# class bank:
#     bname='HDFC'
#     bIFSC='HDFCN354'
#     bloc='Noida'

#     def __init__(self,name,phno,email,addr):
#         self.name=name
#         self.phno=phno
#         self.email=email
#         self.addr=addr

# ankit=bank('ankit',1234567,'asdfg@gmail.com','delhi')
# print(ankit.name,ankit.phno,ankit.email,ankit.addr)

# WAP to create a class as rectangle and print the area and perimeter of given rectangle value
# class rectangle:
    
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
    
#     def area(self,len,bre):
#         print(len*bre) 
    
#     def perimeter(self,len,bre):
#         print(2*(len+bre))
    
# r1=rectangle(2,3)
# r2=rectangle(4,5)
# print(r1.l,r1.b)
# r1.perimeter(r1.l,r1.b)
# print(r1.l,r1.b)
# r1.area(r1.l,r1.b)

# Create a class bank:
# class bank:
#     bname='SBI'
#     bloc='Delhi'
#     bifsc='SBIN000'
    
#     def __init__(self,c_name,c_ac,c_pn,c_loc):
#         self.c_name=c_name
#         self.c_ac=c_ac
#         self.c_pn=c_pn
#         self.c_loc=c_loc
    
#     def details(self):
#         print(self.c_name,self.c_ac,self.c_pn,self.c_loc)
        
#     def change_loc(self):
#         self.c_loc=self.get_loc()
        
#     @classmethod
#     def disp_cls(cls):
#         print(cls.bname,cls.bloc,cls.bifsc)
        
#     @staticmethod
#     def get_loc():
#         return input("Enter new location:")
# c1=bank("ankit",12345678,9876543210,"Delhi")
# # c2=bank("c2",1655678,9879842710)
# # c3=bank("c3",4561278,9642443210)
# c1.details()
# # c1.change_loc("Guwahati")
# c1.details()
# bank.disp_cls()
# c1.change_loc()
# c1.details()
# print(c2.c_name,c2.c_ac,c2.c_pn)
# print(c3.c_name,c3.c_ac,c3.c_pn)

# class library:
#     lname='Pustak'
#     lloc='Delhi'

#     def __init__(self,name,book):       ## __init__ method
#         self.name=name
#         self.book=book

#     def dis_obj(self):
#         print(self.name,self.book)

#     def ch_name(self,new):
#         self.name=new

# ankit=library('ankit','Chetak')     ## Can direct pass in class
# # print(ankit.name,ankit.book)
# ankit.dis_obj()
# ankit.ch_name('as')
# ankit.dis_obj()

### WAP to create a class with 3 static members 5 object members and 2 object members can be modified

# class batch:
#     bcode='A12'
#     bteacher='Deepak sir'
#     bcourse='Python'

#     def __init__(self,name,phoneNo,email,addr,mockRating):
#         self.name=name
#         self.phoneNo=phoneNo
#         self.email=email
#         self.addr=addr
#         self.mockRating=mockRating

#     def dis_obj(self):
#         print(self.name,self.phoneNo,self.email,self.addr,self.mockRating)

#     def ch_pn(self,new_pn):
#         self.phoneNo=new_pn

#     def ch_mr(self,new_mr):
#         self.mockRating=new_mr

#     @classmethod
#     def dis_cls(cls):
#         print(cls.bcode,cls.bteacher,cls.bcourse)

#     @classmethod
#     def ch_code(cls,new):
#         cls.bcode=new
        
#     @staticmethod
#     def msg():
#         print("Good Morning")

# ankit=batch('Ankit',9876543210,'ankit@gmail.com','Guwahati',1)
# vikram=batch('Vikram',1234567890,'vikram@gmail.com','Delhi',1)

# batch.dis_cls()
# ankit.dis_obj()
# print('After update')
# batch.ch_code('m16')
# batch.dis_cls()
# ankit.ch_pn(2345678901)
# ankit.ch_mr(2)
# ankit.dis_obj()
# ankit.msg()
# batch.msg()

### ======================STATIC MEMBERS================================================>

## Its a method which dosent belong to any class or object but act as a supportive method.

## To achive static method we have to use decorators '@staticmethod'
## Due to no belonging to any class and object we dont use 'cls' or 'self' in it.


# class batch:
#     bcode='A12'
#     bteacher='Deepak sir'
#     bcourse='Python'

#     def __init__(self,name,phoneNo,email,addr,mockRating,bal):
#         self.name=name
#         self.phoneNo=phoneNo
#         self.email=email
#         self.addr=addr
#         self.mockRating=mockRating
#         self.bal=bal

#     def dis_obj(self):
#         print(self.name,self.phoneNo,self.email,self.addr,self.mockRating,self.bal)

#     def ch_pn(self,new_pn):
#         self.phoneNo=new_pn

#     def ch_mr(self,new_mr):
#         self.mockRating=new_mr

#     @classmethod
#     def dis_cls(cls):
#         print(cls.bcode,cls.bteacher,cls.bcourse)

#     @classmethod
#     def ch_code(cls,new):
#         cls.bcode=new
        
#     def withdraw(self,amt):
#         self.bal=self.sub(self.bal,amt)
        
#     def deposit(self,amt):
#         self.bal=self.add(self.bal,amt)
    
#     @staticmethod
#     def add(a,b):
#         return a+b
    
#     @staticmethod
#     def sub(a,b):
#         return a-b
    
#     @staticmethod
#     def msg():
#         print("Good Morning")

# ankit=batch('Ankit',9876543210,'ankit@gmail.com','Guwahati',1,1234567)
# vikram=batch('Vikram',1234567890,'vikram@gmail.com','Delhi',1,123456)

# batch.dis_cls()
# ankit.dis_obj()
# print('After update')
# batch.ch_code('m16')
# batch.dis_cls()
# ankit.ch_pn(2345678901)
# ankit.ch_mr(2)
# ankit.dis_obj()
# ankit.msg()
# batch.msg()

# batch.dis_cls()
# ankit.dis_obj()
# ankit.withdraw(4567)
# print('after withdraw')
# ankit.dis_obj()
# ankit.deposit(300000)
# print('after deposit')
# ankit.dis_obj()
