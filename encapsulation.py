# ENCAPSULATION: 3 types:
# PUBLIC
# PROTECTED: ( _ )
# class bank:
#     bname='PNB'
#     bloc='DELHI'
#     bbranch='Narela'
#     bIFSC='PUNB000'
#     _bwebsite='punb@gmail.com'
    
#     def __init__(self,cname,cbranch,cac,cno,cbal):
#         self.cname=cname
#         self.cbranch=cbranch
#         self.cac=cac
#         self.cno=cno
#         self.cbal=cbal
    
#     def details(self):
#         print(self.cname,self.cbranch,self.cac,self.cno,self.cbal)
        
# c1=bank('C1','Delhi',345678,9876543210,3454)
# c2=bank('C2','GHY',321,65438908,6889)
# c3=bank('C3','Narela',7654,8765432167,100)

# print(bank.bname,bank.bloc,bank.bbranch,bank.bIFSC,bank._bwebsite)
# c1.details()
# c2.details()
# c3.details()

# PRIVATE
# class bank:
#     bname='PNB'
#     bloc='DELHI'
#     bbranch='Narela'
#     bIFSC='PUNB000'
#     __bwebsite='punb@gmail.com'
    
#     def __init__(self,cname,cbranch,cac,cno,cbal):
#         self.cname=cname
#         self.cbranch=cbranch
#         self.cac=cac
#         self.cno=cno
#         self.__cbal=cbal
    
#     def details(self):
#         print(self.cname,self.cbranch,self.cac,self.cno,self.__cbal)
        
# c1=bank('C1','Delhi',345678,9876543210,3454)
# c2=bank('C2','GHY',321,65438908,6889)
# c3=bank('C3','Narela',7654,8765432167,100)

# # print(bank.bname,bank.bloc,bank.bbranch,bank.bIFSC,bank.__bwebsite)
# c1.details()
# c2.details()
# c3.details()

# print(c1._bank__cbal)
# print(c2._bank__cbal)
# print(c3._bank__cbal)
# print(bank._bank__bwebsite)


class student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
        
    def __display(self):
        print(self.__name,self.__age)
        
s1=student("Ankit",21)
s2=student('Student2',32)

# s1.display()
s1._student__display()
s2._student__display()
