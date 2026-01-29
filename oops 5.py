#encapsulation
'''class college:
    cname="qs"
    cdept="IT"
    _cloc="Delhi"

    def __init__(self,sname,sid,scourse,_sloc):
        self.sname=sname
        self.sid=sid
        self.scourse=scourse
        self.sloc=_sloc

    def _disp_obj(self):
        print(self.sname,self.sid,self.scourse,self.sloc)

    @classmethod
    def disp_cls(cls):
     print(cls.cname,cls.cdept,cls._cloc)

    
    
x=college('y','098','python','delhi')

x._disp_obj()
college.disp_cls()
print(college._cloc)'''


class college:
    cname="qs"
    cdept="IT"
    __cloc="Delhi"

    def __init__(self,sname,sid,scourse,__sloc):
        self.sname=sname
        self.sid=sid
        self.scourse=scourse
        self.sloc=__sloc

    def _disp_obj(self):
        print(self.sname,self.sid,self.scourse,self.sloc)

    @classmethod
    def disp_cls(cls):
     print(cls.cname,cls.cdept)

    
    
x=college('y','098','python','delhi')

x._disp_obj()
college.disp_cls()
#print(college._college__cloc)
print(x._x__sloc)