
a=open(r"C:\Users\zhangwei5\Desktop\test.txt")

print("read:\n",a.read())
a.close()

a=open(r"C:\Users\zhangwei5\Desktop\test.txt")
line=a.readline()
while(line):
    print("readline:",line)
    line=a.readline()
a.close()

a=open(r"C:\Users\zhangwei5\Desktop\test.txt")
for i in a.readlines():
    print("readlines:",i)
a.close()

a=open(r"C:\Users\zhangwei5\Desktop\test.txt","a+")
a.write("5555")
a.close()

b=["aaa","bbb","ccc"]
a=open(r"C:\Users\zhangwei5\Desktop\test.txt","a+")
a.writelines(b)

import  os
import linecache
if(os.path.exists(r"C:\Users\zhangwei5\Desktop\test.txt")):
    c=linecache.getlines(r"C:\Users\zhangwei5\Desktop\test.txt")
    for i in c:
        print("linecache",i)





