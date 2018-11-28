from collections import  OrderedDict
# OrderedDict会保存key插入的顺序，但是会占用两倍的内存。
d = OrderedDict()
d[2]="2"
d[3] = "3"
d[1] = "1"
for key in d.keys():
    print("key" + str(key) +",value:"+ d[key])