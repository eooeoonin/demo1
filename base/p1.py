class MutiArg:
    def persion(self,name,*pinfo,**sinfo):
        print(name,pinfo,sinfo)

    def persion2(self, name, pinfo, sinfo):
        print(name, pinfo, sinfo)

    def prt(self):
        print(name, pinfo, sinfo)

l={10000,"CS"}
d={"城市":"上海","年龄":19,"性别":"男"}
p1=MutiArg()
p1.persion("Lucy",*l,**d)
p1.persion2("Lucy",l,d)
p2=MutiArg()
p2.persion("lili",10020,"CS",城市=d["城市"],年龄=d["年龄"],性别=d["性别"])
p2.persion("lili",10020,"CS",城市="上海",年龄=19,性别="女")


class Test:
    ID = 1
    def __init__(self):
        pass
    def prtID(self):
        print(self.ID)
    def classplusOne(self):
        Test.ID += 1
    def ObjplusOne(self):
        self.ID += 1

t1 = Test()
t2 = Test()
t1.classplusOne()
t1.ObjplusOne()
t1.prtID()
t2.prtID()
