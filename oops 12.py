### Hospital with all 3 class

class hosp:
    hname='GMC'
    hloc='Guwahati'
    
    def __init__(self,pname,pid,pgender,pbill):
        self.pname=pname
        self.pid=pid
        self.pgender=pgender
        self.pbill=pbill
        
    def dis_obj(self):
        print(self.pname,self.pid,self.pgender,self.pbill)
        
    @classmethod
    def dis_cls(cls):
        print(cls.hname,cls.hloc)
        
    def upd_bill(self,amt):
        self.pbill=self.add(self.pbill,amt)
        
    @staticmethod
    def add(a,b):
        return a+b
    
aman=hosp('Aman','A12','M',0)

hosp.dis_cls()
aman.dis_obj()
aman.upd_bill(10000)
print("After update")
aman.dis_obj()
