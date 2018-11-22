from collections import  deque
# 保留最后有限几个元素的历史记录

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)

