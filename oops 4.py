#static method
class bank:
    bname='hsbc'
    bloc='karolbagh'
    bifsc='hsbsc4848488'

    def __init__(self,name,phno,email,addr,accno,bal):
        self.name=name
        self.phno=phno
        self.email=email
        self.addr=addr
        self.accno=accno
        self.bal=bal

    def disp_obj(self):
        print(self.name,self.phno,self.email,self.addr,self.accno,self.bal)

    @classmethod
    def disp_cls(cls):
        print(cls.bname,cls.bloc,cls.bifsc)

    def deposit(self,amt):
        self.bal=self.add(self.bal,amt)

    def withdraw(self,amt):
        if amt>self.bal:
            print("insufficent bal.....")
        else:
            self.bal=self.sub(self.bal,amt)

    @staticmethod
    def add(a,b):
        return a+b
    
    @staticmethod
    def sub(a,b):
        return a-b
    
x=bank('x',9875633223,'y@gmail.com','delhi',2637484884,100000000)

bank.disp_cls()
x.disp_obj()
x.withdraw(1000000)
x.disp_obj()
x.deposit(1234)
print("after deposit")
x.disp_obj()

#make a hospital bills using all the class
class hospital:
    hname='qs'
    hloc='delhi'
    
    
