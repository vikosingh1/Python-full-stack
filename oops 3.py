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
    
    def disp_obj(self):
        print(self.name,self.phno,self.email,self.addr,self.accno)

    def ch_phno(self,new):
        self.phno=new

anushka=bank('Anushka',9877655432,'anu@gmail.com','noida',35668796796)

print(bank.bname,bank.bloc,bank.bifsc)
#print(anushka.name,anushka.phno,anushka.email,anushka.addr,anushka.accno)
anushka.disp_obj()
anushka.ch_phno(9786754321)
anushka.disp_obj()'''

#create a class to your batchcode with 3 static member and 5 object members with modifying 2 object members
class batch:
    bcode='A12'
    bteacher='Deepak sir'
    bcourse='python'

    def __init__(self, name,phno,email,loc,mrate):
        self.name=name
        self.phno=phno
        self.email=email
        self.loc=loc
        self.mrate=mrate

    def disp_obj(self):
        print(self.name,self.phno,self.email,self.loc,self.mrate)

    def ch_phno(self,new):
        self.phno=new

    def ch_mrate(self,new):
        self.mrate=new
    
    @classmethod
    def disp_cls(cls):
        print(cls.bcode,cls.bteacher,cls.bcourse)#display class

    @classmethod
    def ch_bcourse(cls,new):#modify class
        cls.bcourse=new
    
    @staticmethod
    def msg():
        print("good morning")

x=batch('D',9877655432,'D@gmail.com','noida',1)
y=batch('B',7877655432,'D@gmail.com','noida',1)
x.disp_obj()
batch.ch_bcourse('java')
batch.disp_cls()
x.ch_phno(8890765680)
x.disp_obj()
x.ch_mrate(3)
x.disp_obj()
y.ch_phno(667890655)
y.disp_obj()
x.msg()
batch.msg()

        