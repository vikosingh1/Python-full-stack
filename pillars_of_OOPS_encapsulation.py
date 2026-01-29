# Pillars
# Encaptulation
# Public

# class college:
#     cname="ADBU"
#     cdept="Technology"
#     Cloc="Guwahati"

#     def __init__(self,sname,sid,scourse,sloc):
#         self.sname=sname
#         self.ssid=sid
#         self.scourse=scourse
#         self.sloc=sloc

#     def dis_obj(self):
#         print(self.sname,self.ssid,self.scourse,self.sloc)

#     @classmethod
#     def dis_class(cls):
#         print(cls.cname,cls.cdept,cls.Cloc)

# ankit=college('ankit','DC2021BTE0112','BTECH','Guwahati')

# ankit.dis_obj()
# college.dis_class()

# protector 

# class college:
#     cname="ADBU"
#     cdept="Technology" 
#     _cloc="Guwahati"

#     def __init__(self,sname,sid,scourse,_sloc):
#         self.sname=sname
#         self.ssid=sid
#         self.scourse=scourse
#         self.sloc=_sloc

#     def _dis_obj(self):
#         print(self.sname,self.ssid,self.scourse,self.sloc)

#     @classmethod
#     def dis_class(cls):
#         print(cls.cname,cls.cdept,cls._cloc)

# ankit=college('ankit','DC2021BTE0112','BTECH','Guwahati')

# ankit._dis_obj()
# college.dis_class()
# print(college._cloc)
# college._cloc="Delhi"
# print(college._cloc)



class college:
    cname="ADBU"
    cdept="Technology" 
    __cloc="Guwahati"

    def __init__(self,sname,sid,scourse,__sloc):
        self.sname=sname
        self.ssid=sid
        self.scourse=scourse
        self.sloc=__sloc

    def _dis_obj(self):
        print(self.sname,self.ssid,self.scourse,self.sloc)

    @classmethod
    def dis_class(cls):
        print(cls.cname,cls.cdept,cls.__cloc)

ankit=college('ankit','DC2021BTE0112','BTECH','Guwahati')

ankit._dis_obj()
college.dis_class()
# print(college._college__cloc)