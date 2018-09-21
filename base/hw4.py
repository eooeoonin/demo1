v1 =3
v2=v1
print("v1在内存的地址：%d,v2在内存中地址:%d"%(id(v1),id(v2)))
print("v2:",v2)
v1 += 2
print("v1在内存的地址：%d,v2在内存中地址:%d"%(id(v1),id(v2)))
print("v1:",v1)
print("v2:",v2)


l1 = [1,2,3]
l2 =l1
print("l1在内存的地址：%d,l2在内存中地址:%d"%(id(l1),id(l2)))
print(l2)
l1.append(4)
print("l1在内存的地址：%d,l2在内存中地址:%d"%(id(l1),id(l2)))
print(l1)
print(l2)

s1 = {1,2,3}
s2 =s1
print("s1在内存的地址：%d,s2在内存中地址:%d"%(id(s1),id(s2)))
print(s2)
s1.add(4)
print("s1在内存的地址：%d,s2在内存中地址:%d"%(id(s1),id(s2)))
print(s1)
print(s2)