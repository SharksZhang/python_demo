##含n个元素的元组（序列）赋值给多个变量，通用适用于字符串
#长度不符会报错

# 直接赋值
a = (1,2)
a1, a2 = a
print("a1:" + str(a1))
print("a2:" + str(a2))
# 忽略不想要的值
b = (1, 2, 3, (4, 5))
b1, _, b3, b4 = b
print("b1:" + str(b1))
print("b3:" + str(b3))
print("b4:" + str(b4))

#字符串

hello = "hello"

h, e, _,_,o = hello
print(h + e + o)





