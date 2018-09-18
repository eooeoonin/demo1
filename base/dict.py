d1={"aaa":111,"bbb":222,"ccc":333}
d2={"J":"jj","K":"kk"}
d3={"aaa":555}

d1.update(d2)
print(d1)
d1.update(d3)
print(d1)
print(d1.get("bbb"))

d1["bbb"]=666
print(d1)

del d1["K"]
print(d1)
print(d1.pop("bbb"))

print(d1.__contains__("aaa2"))  #取代has——key
print(d1.keys())
print(d1.values())

print(d1.items())