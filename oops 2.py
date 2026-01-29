#wap to print a class bank with minimum three static member, 2 objects with 5 objects members
'''class bank:
    bname='sbi'
    bloc='burari'
    bifsc='sbin0003456'
piyush=bank()
samarth=bank()
piyush.name='piyush'
piyush.dob='27-02-2005'
piyush.addr='jamunapar'
piyush.phno='9876543210'
piyush.gender='male'

samarth.name='samarth'
samarth.dob='12-01-2001'
samarth.addr='yamunapar'
samarth.phno='92345678933'
samarth.gender='male'

print(bank.bname,bank.bloc,bank.bifsc)
print(piyush.name,piyush.dob,piyush.addr,piyush.phno,piyush.gender)'''

#wap to create a class hospital with minimum 4 static member and with 3 objects and 7 object members.

'''class Hospital:
    hname='Qspider'
    hloc='karolbagh'
    htype='private'
    hbank='sbi'
patient1=Hospital()
patient2=Hospital()
patient3=Hospital()

patient1.name='Dinga'
patient1.age='44'
patient1.addr='karolbagh'
patient1.gender='male'
patient1.pno='9876543210'
patient1.doc='Dipak sir'
patient1.status='Death'

patient2.name='Dingi'
patient2.age='41'
patient2.addr='noida'
patient2.gender='female'
patient2.pno='9876543299'
patient2.doc='x'
patient2.status='alive'

patient3.name='Tinga'
patient3.age='45'
patient3.addr='Benglore'
patient3.gender='male'
patient3.pno='9876543298'
patient3.doc='y'
patient3.status='Death'

print(patient1.name,patient1.age,patient1.addr,patient1.gender,patient1.pno,patient1.doc,patient1.status)'''

#with functions
'''class bank:
    bname='hdfc'
    bloc='noida'
    bifsc='hdfcn0000345'

    def det(obj,name,phno,email,addr,accno):
        obj.name=name
        obj.phno=phno
        obj.email=email
        obj.addr=addr
        obj.accno=accno

anushka=bank()
bond=bank()
anushka.det('Anushka',9877655432,'anu@gmail.com','noida',35668796796)

print(bank.bname,bank.bloc,bank.bifsc)
print(anushka.name,anushka.phno,anushka.email,anushka.addr,anushka.accno)'''

#with __init__ methods
'''class bank:
    bname='hdfc'
    bloc='noida'
    bifsc='hdfcn0000345'

    def __init__(self,name,phno,email,addr,accno):
        self.name=name
        self.phno=phno
        self.email=email
        self.addr=addr
        self.accno=accno

anushka=bank('Anushka',9877655432,'anu@gmail.com','noida',35668796796)
#bond=bank()
#anushka.det('Anushka',9877655432,'anu@gmail.com','noida',35668796796)

print(bank.bname,bank.bloc,bank.bifsc)
print(anushka.name,anushka.phno,anushka.email,anushka.addr,anushka.accno)'''

class library:
    lname='pustak'
    lloc='delhi'

    def __init__(self,name,book,idate):
        self.name=name
        self.book=book
        self.idate=idate
x=library('x','y','12-12-2024')
print(x.name,x.book,x.idate)




