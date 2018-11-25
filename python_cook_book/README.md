### notes
python cook 笔记
#### 1.Data Structures and Algorithms
##### 1.1 Unpacking a Sequence into Separate Variables 1
解决问题：含n个元素的元组（序列）赋值给多个变量。
存在问题：长度不符会报错

```
# 直接赋值
a = (1,2)
a1, a2 = a
# 忽略不想要的值
b = (1, 2, 3, (4, 5))
b1, _, b3, b4 = b
```

#####1.2Unpacking Elements from Iterables of Arbitrary Length
解决问题：用*表达式接受不定格式的值

#####1.3Keeping the Last N Items
解决问题：保留最后有限几个元素的历史记录
使用指定长度的deque,当deque达到最大长度时，自动会弹出最初的值。并且时间复杂度时O(1)

#####1.4Finding the Largest or Smallest N Items

解决问题在集合中获得最大或者最小的 N 个元素列表。
分三种情况。
如果只需要一个最大或者最小值，使用min()和max最好。
如果N个元素 N 相对与集合总长度比较小时，使用堆排序，弹出少量的几个比较合适
如果N接近集合的长度，直接排序后选切片个数性能比较好。

#####Implementing a Priority Queue
解决问题：实现优先级队列，每次返回优先级最高的。
使用堆实现，每次pop出最小的。使用index保证优先级相同的情况下保序。
在堆中存储的数据并不是按照数组下标递增或递减，所以每次从堆中弹出的时候仍然需要heapq.heappop.
时间复杂度ologn
用普通的排序算法也可以实现，只不过效率没这个高

#####Mapping Keys to Multiple Values in a Dictionary
解决问题：实现一个键对应多个值的字典
使用defaultdict,defaultdict 会自动初始化每个 key 刚开始对应的值

