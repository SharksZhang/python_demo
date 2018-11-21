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

```angular2html

```