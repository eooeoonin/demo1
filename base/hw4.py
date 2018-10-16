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


def ChangeInt(v1):
    v1 = 10
    return v1

b = 2
print(ChangeInt(b))
print(b)


def changeL(l1):
    "修改传入的列表"
    l1.append([1, 2, 3, 4])
    print("函数修改后的值: ", l1)
    return l1

l2 = [10, 20, 30]
print(changeL(l2))
print("调用函数以后取的函数外面值: ", l2)


def fc6(v1,v2):
    return(v1,v2)
a=fc6(12,20)
print (a,type(a))

def fc9(i):
    sum = 0
    while i<10:
        sum += i
        i += 1
        print("sum is :",sum)
        return  #return用在函数里，直接终止函数
    print("sum is :",sum)
print(fc9(0))