def makeBold(fn):
    print("BBBBB"*5)
    def wrapped1():   #注意为了演示结果这里讲wrapped函数，分为wrapped1,wrapped2
        print("bbbbb"*5)
        return "<b>" + fn() + "</b>"
    return wrapped1

def makeItalic(fn):
    print("IIIII"*5)
    def wrapped2():     #注意为了演示结果这里讲wrapped函数，分为wrapped1,wrapped2
        print("iiiiii" *3)
        return "<i>" + fn() + "</i>"
    return wrapped2


@makeBold
@makeItalic

def test_B_I():
    print("test_B_I"*5)
    return "this is the test_B_I"

test_B_I()
print(test_B_I())


generator1 =(x*2 for x in range(10))
for i in generator1:
    print(i)