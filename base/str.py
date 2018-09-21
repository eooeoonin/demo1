s1="abc"
s2="def"
print(s1+s2)

print ("*"*100)
print(s1*10)

s3="abcabcabcabcabcabcabcabcabcabc"
for i in s3.split("b"):
    print (i)
print(s3[-2])

print (s3.replace("a","o"))
print(s3.upper())

s4="abcDEF"
print(s4.lower())
print(s4.capitalize())

s3="abcabcabcabcabcabcabcabcabcab"
s5="ab"
print(s3.startswith(s5,2,7))
print(s3.endswith(s5,1,2))   #???
'''
print(s5.__len__())

s6="123a"
print(s6.isdigit())

print(s5.join(s6)) #s5是连接符

s7="abcc1234abc5678abccab"
print(s7.strip("abc"))  #移除头尾字符

print(s7.index("1234"))
print(s7.index("abc",5))
'''

s1 = "ABC+-DEF"
s2 = s1[3:5]
print (s2)

str='hello,world!'
str1="llo"
print("find:",str.find(str1))
print("index",str.index(str1))

ls1=[4,3,2,1,5,8,"11","22","aa","bb"]
ls2=["hello",[1,3],["hello"],3.14,"哈哈哈",2.5,3,3.14,2.5,3]
ls1.reverse()
print(ls1)
#print(ls1[::-1])
#print(ls1)
print(ls2[::-1])

str="abcde"
print(str[::-1])
print(str)