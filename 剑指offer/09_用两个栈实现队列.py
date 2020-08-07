"""
用两个栈实现一个队列。队列的声明如下，请实现它的两个函数 appendTail 和 deleteHead ，
分别完成在队列尾部插入整数和在队列头部删除整数的功能。(若队列中没有元素，deleteHead 操作返回 -1 )


"""

class CQueue:
    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if self.B: return self.B.pop()
        if not self.A: return -1
        while self.A:
            self.B.append(self.A.pop())
        return self.B.pop()

    def show(self):
        return self.A, self.B

s = CQueue()
s.appendTail(3)
s.appendTail(4)
s.appendTail(5)
print(s.show())
print(s.deleteHead())
print(s.deleteHead())
print(s.deleteHead())
print(s.deleteHead())
print(s.show())
"""
([3, 4, 5], [])
3
4
5
-1
([], [])
"""