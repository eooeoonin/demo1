import random

print("uniform",random.uniform(1,50))
print("randint:",random.randint(1,50))
print(random.random())

print(random.choice((1,2,3,4,5,6,7)))
print(random.choice("china"))
print(random.choice(["a","b","c","d","e","f"]))


print(random.sample("abcdef",3))


a=[1,2,3,4,5,6]
random.shuffle(a)
print(a)