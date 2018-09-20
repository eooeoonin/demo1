
class Computer:
    __os="linux"
    def show(self,cpu,mem,disk,os):
        self.cpu=cpu
        self.mem=mem
        self.disk=disk
        self.__os__=os
        print(cpu,"核cpu，",mem,"G内存,",disk,"G磁盘空间,",Computer.__os)

m=Computer()
m.show(8,40,150,"w")

class Price:
    def price(self,cpu,mem,disk):
        self.cpu=cpu
        self.mem=mem
        self.disk=disk
        cprice=cpu*1527.679
        mprice=mem*100.21
        dprice=disk*50.789
        print(round((cprice+mprice+dprice),2))
m=Price()
m.price(1,2,3)




