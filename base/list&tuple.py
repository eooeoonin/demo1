from typing import Tuple

l1=["abc","def","ghi","kkk"]
l2=[123,456]

t1=("ABC","DEF","ooo","jjj","fff")
t2=(12,34)

print(l1+l2)
print(t1+t2)    #创建新元组
print(l1*5)
print(t2*5)
print(l1[2])    #索引
print(l1[2:])   #分片
print(t1[-1])
print(t1[::2])  #等步长
print(l1.__len__())
print(t1.__len__())
print(l1.count(123))
print(t1.count("A"))
print(l1.index("kkk"))
print(t1.index("DEF"))

l1.append(l2)  #L2作为1个元素
print(l1)
l1.extend(l2)  #L2展开作为2个元素
print(l1)
l1.insert(1,"hhh")
print(l1)

del(l1[2])
print(l1)
print(l1.pop())
print(l1)
l1.remove(123)
l1.remove([123,456])
print(l1)

l1.reverse()
print(l1)
l1.sort()
print(l1)  #升降序，默认升序,不支持数字
print("-".join(l1))
print("-".join(t1))
print(t1)
