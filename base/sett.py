s1={1,2,3,4,5}
s2={1,3,5,7,9}
l=["aa","bb"]
s3=s1.union(s2)
print(s3)
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))

s1.add("a")
print(s1)
s1.update("b")
s1.update(l)
print(s1)

s1.remove(2)
print(s1)

print(s1.pop())
print(s1.pop())
print(s1.__len__())