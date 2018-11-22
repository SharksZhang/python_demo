import heapq

class PriorityQueue :
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        print (self._queue)
        self._index += 1
    # 在堆中存储的数据并不是按照数组下标递增或递减，所以每次从堆中弹出的时候仍然需要heapq.heappop.
    def pop(self):
        # print (heapq.heappop(self._queue))
        print (self._queue)
        return heapq.heappop(self._queue)[-1]



def test():
    queue = PriorityQueue()
    queue.push("a", 1)
    queue.push("b", 5)
    queue.push("c", 2)
    queue.pop()

test()