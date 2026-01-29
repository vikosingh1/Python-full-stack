# multilevel Inheritance
# class ten_th:
#     def __init__(self,trolno,year,sub,marks):
#         self.trolno=trolno
#         self.year=year
#         self.sub=sub
#         self.marks=marks
#     def dis_obj(self):
#         print(self.trolno,self.year,self.sub,self.marks,end=' ')
# class twel_th(ten_th):
#     def __init__(self,trolno,year,sub,marks,twelrolno,twelyear,twelsub,twelmarks):
#         super().__init__(trolno,year,sub,marks)
#         self.twelrolno=twelrolno
#         self.twelyear=twelyear
#         self.twelsub=twelsub
#         self.twelmarks=twelmarks

#     def dis_obj(self):
#         super().dis_obj()
#         print(self.twelrolno,self.twelyear,self.twelsub,self.twelmarks,end=' ')
# class degree(twel_th):
#     def __init__(self,trolno,year,sub,marks,twelrolno,twelyear,twelsub,twelmarks,drolno,dyear,dsub,dmarks):
#         super().__init__(trolno,year,sub,marks,twelrolno,twelyear,twelsub,twelmarks)
#         self.drolno=drolno
#         self.dyear=dyear
#         self.dsub=dsub
#         self.dmarks=dmarks

#     def dis_obj(self):
#         super().dis_obj()
#         print(self.drolno,self.dyear,self.dsub,self.dmarks,end=' ')

# x=degree(234,2017,"H",390,123,"E",2019,375,321,2024,"b.TECH",400)
# x.dis_obj()

# make a railway reservation system

class tickets:
    def __init__(self,floc,toloc,tname):
        self.floc=floc
        self.toloc=toloc
        self.tname=tname
    def dis_obj(self):
        print("from location",self.floc,"To location",self.toloc,"Train name",self.tname)

class p_details(tickets):
    def __init__(self,floc,toloc,tname,pname,p_age,pgender):
        super().__init__(floc,toloc,tname)
        self.pname=pname
        self.p_age=p_age
        self.pgender=pgender
    
    def dis_obj(self):
        super().dis_obj()
        print("person name",self.pname,"person age",self.p_age,"person Gender",self.pgender)

class cnf(p_details):
    def __init__(self,floc,toloc,tname,pname,p_age,pgender,cnf):
        super().__init__(floc,toloc,tname,pname,p_age,pgender)
        self.cnf=cnf

    def dis_obj(self):
        super().dis_obj()
        print("Tickets Status",self.cnf)

shikha=cnf("jsme","hwh","janstabdi ex","shikha",24,"female","waiting list")
shikha.dis_obj()



