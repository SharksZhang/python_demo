from collections import defaultdict

# defaultdict 会给key初始化默认的数据结构类型

d1 = defaultdict(list)
d1["1"].append("aaaaa")
d1["2"].append("bbbbb")

d2 = defaultdict(set)
d2["1"].add(1)
d2["1"].add(2)

print("d1:", d1)
print("d2:", d2)



