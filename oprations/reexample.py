import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(u'你好')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match(u'，世界!')

if match:
    # 使用Match获得分组信息
    print("result:",match.group())
print("*"*100)

m = re.match('hello', 'hello world!')
print(m.group())
print("*"*100)

p = re.compile(r'\d+')
print(p.split('one1two2three3four4'))
print("*"*100)

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'world')

# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = pattern.search('hello world!')

if match:
    # 使用Match获得分组信息
    print(match.group())
print("*"*100)

text = "Example 3: There is 1 date 10/25/95 in here!"
m = re.search("(\d{1,2})/(\d{1,2})/(\d{2,4})", text)
print(m.group())

print(m.group(1), m.group(2), m.group(3))
month, day, year = m.group(1, 2, 3)
print(month, day, year)