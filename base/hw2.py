import random
'''
class Iff:
    n=input("请输入一个数字：")
    n2=random.randint(1,10)

    try:
        n1=int(n)
        if(n1==n2):
            print("clver!You are right")
        elif(n1>n2):
            print("大了，应该是",n2)
        else:
            print("小了,应该是",n2)
    except:
        print("这不是数字")
'''

class H1:
    i=100
    l=[]
    while(i<250):
        if(i%7==0):
            if(i%5==0):
                l.append(i)
                print("%5 ok")
            print("%7 OK")
        else:
            print(i)
        i+=1
    print(l)

class H2:
    i=0
    while(i<=20):
        if(i%3==0):
            if(i%5==0):
                print(i,"three+five")
                i+=1
                continue
            else:
                print(i,"three")
                i+=1
        elif(i%5==0):
            print(i,"five")
            i+=1
        i+=1

class H3:
    l=[1,2,4,"a"]
    j=0
    for i in l:
        if(isinstance(i,int)):
            j+=i
            print(j)
    print(j)

class H4:
    d={"name":"zhangsan","age":16}
    try:
        print(d.get("grace"))
    except Exception as e:
        print(e)

'''
5. 实现一个不定长参数的函数defflexible(aa, *args, **kwargs):，把传入的参数和值打印出来。比如传入参数是
flexible(aa, 2, 3, x = 4, y = 5, *[1, 2, 3], **{'a':1,'b': 2})
输出结果：(2, 3, 1, 2, 3)，{'a': 1, 'y': 5, 'b': 2, 'x': 4}
'''
class H5:
    def flexible(aa, *args, **kwargs):
        list=[]
        dict={}
        list.append(aa)
        for i in args:
            if(i.isinstance(i))


h=H3()
#iff=Iff()

