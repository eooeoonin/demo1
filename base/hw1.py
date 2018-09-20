f=2.918
print(int(f))

s="python is popular"
print(s.replace("python","java"))

l=[1,2,3,4,5,6,7,8]
l1=l[1:]
print(l1[::2])

d={"name":"张美丽","sex":"male","province":"山西"}
d["province"]="江苏"
print(d)

s="Python was created in 1989, Python is using in AI, big data, IOT."
print(s.lower())
list=[]
for i in s.split():
    list.append(i)
   # list.append(" ")
print(list)
n=(list.__len__())//2
print(n)
print(list[n])

list1=["python", 5,6, 8]
list2=["python","5", 6, 8,10]
list3=list1+list2
print(list1+list2)
s1=set(list3)
print("s is ",s1)