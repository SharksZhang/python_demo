import heapq

a = [5, 2, 9, 4, 1, 23, 88, 75, 66]
# 最大一个
print(max(a))
# 最大n个，远远小于数组长度
print(heapq.nlargest(4, a))
# 最大n个，接近数组长度
print(sorted(a)[1:])
