''' 暴力
直接实现一个普通的队列，查询最大值时遍历计算。
时间复杂度：O(1)O(1)（插入，删除），O(n)O(n)（求最大值）。
插入与删除只需要普通的队列操作，为 O(1)O(1)，求最大值需要遍历当前的整个队列，最坏情况下为 O(n)O(n)。
空间复杂度：O(n)O(n)，需要用队列存储所有插入的元素。
用pop(0)的方法可以弹出list的第一个元素，但这个的时间复杂度是O(n)O(n)，这一点要注意。
Python中的deque可以对pop(0)，就是popleft()实现O(1)O(1)的时间复杂度。

class MaxQueue:

    def __init__(self):
        self.deque = queue.deque()

    def max_value(self) -> int:
        return max(self.deque) if self.deque else -1

    def push_back(self, value: int) -> None:
        self.deque.append(value)

    def pop_front(self) -> int:
        return self.deque.popleft() if self.deque else -1

'''
class MaxQueue:

    def __init__(self):
        from collections import deque
        self.A = deque()   # 原始
        self.B = deque()    # 排序   从大到小

    def max_value(self) -> int:
        if self.B:
            return self.B[0]
        return -1


    def push_back(self, value: int) -> None:
        self.A.append(value)
        while self.B and self.B[-1] < value:
            self.B.pop()
        self.B.append(value)

    def pop_front(self) -> int:
        if not self.A:
            return -1
        res = self.A.popleft()   # 如果A第一个值为最大值，及ab都有
        if res == self.B[0]:
            self.B.popleft()
        return res


if __name__ == '__main__':
    s = MaxQueue()
    print(s.push_back(4))
    print(s.push_back(2))
    print(s.max_value())
    print(s.pop_front())
    print(s.push_back(1))
    print(s.max_value())
    print(s.pop_front())
    print(s.pop_front())
    print(s.pop_front())

