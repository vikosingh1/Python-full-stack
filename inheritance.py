# class A:
#     a=10
#     b=20
# class B(A):
#     c=30
#     d=54
# obj1=B()
# print(A.a,A.b)
# print(B.a,B.b)
# print(obj1.a,obj1.d)

# class bank:
#     def __init__(self,name,phno,loc):
#         self.name=name
#         self.phno=phno
#         self.loc=loc
#     def display(self):
#         print(self.name,self.phno,self.loc,end=' ')
# class bank_up(bank):
#     def __init__(self, name, phno, loc,adhar,pan):
#         super().__init__(name, phno, loc)
#         self.adhar=adhar
#         self.pan=pan
#     def display(self):
#         super().display()
#         print(self.adhar,self.pan)

# c1=bank_up('ankit',9876543210,'Guwahati',678923454567,"PAN456")
# c1.display()

# class online:
#     def __init__(self,uname,uno,uemail,ubank):
#         self.uname=uname
#         self.uno=uno
#         self.uemail=uemail
#         self.ubank=ubank
        
#     def disp_data(self):
#         print(self.uname,self.uno,self.uemail,self.ubank) 
    
# class offline(online):
#     def __init__(self, uname, uno, uemail, ubank,uadhar,upan):
#         super().__init__(uname, uno, uemail, ubank)
#         self.uadhar=uadhar
#         self.upan=upan
        
#     def disp_data(self):
#         super().disp_data(self)
#         print(self.uadhar,self.upan)
        
# obj=offline("ankit",234567,"ankit@gmail.com","Pnb",2345678,"PPPsdfg")
# offline.disp_data()

# print(offline.uname,offline.uno,offline.uemail,offline.ubank,offline.uadhar,offline.upan)

# offline.disp_data()

# class ten_th:
#     def __init__(self,trolno,year,sub,marks):
#         self.trolno=trolno
#         self.year=year
#         self.sub=sub
#         self.marks=marks
        
#     def dis_obj(self):
#         print(self.trolno,self.year,self.sub,self.marks,end=" ")
        
# class twl_th(ten_th):
#     def __init__(self,trolno,year,sub,marks,twrolno,twyear,twsub,twmarks):
#         super().__init__(trolno,year,sub,marks)
#         self.twrolno=twrolno
#         self.twyear=twyear
#         self.twsub=twsub
#         self.twmarks=twmarks
         
        
#     def dis_obj(self):
#         super().dis_obj()
#         print(self.twrolno,self.twyear,self.twsub,self.twmarks)
        
         
# class degree(twl_th):
#     def __init__(self, trolno, year, sub, marks, twrolno, twyear, twsub, twmarks,dyear,dtype,dcgpa):
#         super().__init__(trolno, year, sub, marks, twrolno, twyear, twsub, twmarks)
#         self.dyear=dyear
#         self.dtype=dtype
#         self.dcgpa=dcgpa
         
#     def dis_obj(self):
#         super().dis_obj()
#         print(self.dyear,self.dtype,self.dcgpa)
        
# ankit=degree(123,2018,"5 subjects",400,1255,2020,"5 subject",450,2021,"BTECH",8.21)

# ankit.dis_obj()


# class detail:
#     def __init__(self,pname,pno,pemail):
#         self.pname=pname
#         self.pno=pno
#         self.pemail=pemail
        
#     def disp_obj(self):
#         print(self.pname,self.pno,self.pemail)
        
# class seat_det(detail):
#     def __init__(self, pname, pno, pemail,tname,tcoach,tseat,tbirth):
#         super().__init__(pname, pno, pemail)
#         self.tname=tname
#         self.tcoach=tcoach
#         self.tseat=tseat
#         self.tbirth=tbirth
        
#     def disp_obj(self):
#         super().disp_obj()
#         print(self.tname,self.tcoach,self.tseat,self.tbirth)
        
# class confirm(seat_det):
#     def __init__(self, pname, pno, pemail, tname, tcoach, tseat, tbirth,cnf):
#         super().__init__(pname, pno, pemail, tname, tcoach, tseat, tbirth)
#         self.cnf=cnf
        
#     def disp_obj(self):
#         super().disp_obj()
#         print(self.cnf)

# obj1=confirm("Ankit",23456780,"ank@gmail.com","RAJDhani","S1",65,"upper",True)
# obj1.disp_obj()  

### Multiple Inheritance
# class bat:
#     blen="3 feet"
#     bbrand="MRF"

# class ball:
#     bshape="sphere"
#     bwt=150

# class cricket(bat,ball):
#     player=22

# print(cricket.blen)

# class telephone:
#     tuse='Calling'
#     def __init__(self,t_brand):
#         self.t_brand=t_brand
#     def disp(self):
#         print(self.t_brand,end=' | ')
        
# class keypad(telephone):
#     kuse='Messaging'
#     def __init__(self,t_brand,k_brand):
#         super().__init__(t_brand)
#         self.k_brand=k_brand
#     def disp(self):
#         super().disp()
#         print(self.k_brand,end=' | ')
        
# class smartphone(keypad):
#     suse='Video calling'
#     def __init__(self, t_brand, k_brand,s_brand):
#         super().__init__(t_brand, k_brand)
#         self.s_brand=s_brand
#     def disp(self):
#         super().disp()
#         print(self.s_brand)
        
# c1=smartphone("telephone_nokia","keypad_nokia","smartphone_Nothing")
# # c1=smartphone(456,567,56)
# # print(c1.tuse,c1.kuse,c1.suse)
# c1.disp()

# Multiple Ingeritance
# Multiple parents to single child

# WAP to demonstrate multiple inheritance where class A has method display A class b has method display b
# class A:
#     def displayA(self):
#         print("This is class A")
# class B:
#     def displayB(self):
#         print("This is class B")
# class C(A,B):
#     def displayC(self):
#         super().displayA()
#         super().displayB()
#         print("This is class C")
# obj1=C()
# obj1.displayC()

# Hierarcial Inheritance
# class A:
#     a=10
#     b=20
# class B(A):
#     c=30
# class C(A):
#     d=40
# obj1=B()
# print(obj1.c,obj1.a,obj1.b)
# obj2=C()
# print(obj2.d,obj2.a,obj2.b)

# 
# class parent:
#     def showparent(self):
#         print("THis is parent")
# class child1(parent):
#     def showchild1(self):
#         super().showparent()
#         print("This is child 1")
# class child2(parent):
#     def showchild2(self):
#         super().showparent()
#         print("This is child 2")
        
# ch1=child1()
# ch1.showchild1()
# ch2=child2()
# ch2.showchild2()

# Create a class socialmedia in which initialize the object as username password no.of post.
# Inhetrit the socialmedia to new class like instagram and facebook and print all details

# class socialmedia:
#     def __init__(self,uname,upassword,noofpost):
#         self.uname=uname
#         self.upassword=upassword
#         self.noofpost=noofpost
    
#     def disp(self):
#         print(self.uname,self.upassword,self.noofpost)
        
# class insta(socialmedia):
#     def __init__(self, uname, upassword, noofpost):
#         super().__init__(uname, upassword, noofpost)
        
#     def disp(self):
#         super().disp()
#         print('This is instagram')

# class fb(socialmedia):
#     def __init__(self, uname, upassword, noofpost):
#         super().__init__(uname, upassword, noofpost)
        
#     def disp(self):
#         super().disp()
#         print('This is Facebook')
    
# obj1=insta('Ankit',"ANKxxxx",23)
# obj1.disp()
# obj2=fb("ANKIT!@#$%",'wert987654',50)
# obj2.disp()

# HYBRID Inheritnce
# class p1:
#     x=10
# class c1(p1):
#     a=20
# class c2(p1):
#     b=30
# class c3(c2):
#     c=40
# class c4(c3):
#     d=50
# obj1=c4()
# print(obj1.d,obj1.c,obj1.b,obj1.x)