import os
import time
import sys
import datetime
import subprocess

class File:
    f=open("C:\\Users\\zhangwei5\\Desktop\\测试信息.txt","r+")
    def pf(self):
        l = File.f.readlines()
        for i in l:
            print(i)
    def wf(self):
        File.f.write("aaaa")
        print("XXXX")
        self.pf()
        print("YYYYYY")
        File.f.flush()
        #self.f.close()

a=File()
a.pf()
a.wf()

print(os.listdir("E:\\迅雷下载\\小甲鱼零基础入门Python（87集全）"))
print(os.getcwd())
print(os.stat("C:\\Users\\zhangwei5\\Desktop\\测试信息.txt"))
print(os.path.join("C:\\Users\\zhangwei5\\Desktop","aaa.txt"))
#os.mkdir("C:\\Users\\zhangwei5\\Desktop\\new")
print(os.path.basename("C:\\Users\\zhangwei5\\Desktop\\测试信息.txt"))

print(time.time())
print(time.localtime())
print(time.gmtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strptime("30 Nov 00", "%d %b %y"))
#print(datetime.timederta("days",1))
'''
l=os.listdir("/tomcat/log/")
now=int(time.time())
for i in l:
    d=os.stat(i)
    then=int(d["st_mtime"])
    if((now-then)>3600):
        os.system("tar -cvf i;mv i.tag.gz /backup")
        1
'''
subprocess.call("dir")