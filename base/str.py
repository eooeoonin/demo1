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

s5="ca"
print(s3.startswith(s5,2,7))
print(s3.endswith(s5,2,4))   #???

print(s5.__len__())

s6="123a"
print(s6.isdigit())

print(s5.join(s6)) #s5是连接符

s7="abcc1234abc5678abccab"
print(s7.strip("abc"))  #移除头尾字符

print(s7.index("1234"))
print(s7.index("abc",5))