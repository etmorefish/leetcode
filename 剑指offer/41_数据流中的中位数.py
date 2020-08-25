class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []

    def addNum(self, num: int) -> None:  # 从数据流中添加一个整数到数据结构中。
        self.A.append(num)

    def findMedian(self) -> float:  # 返回目前所有元素的中位数。
        self.A.sort()
        n = len(self.A)
        if n == 0:
            return None
        if n & 1 == 1:
            return self.A[n // 2]
        else:
            return (self.A[n // 2] + self.A[n // 2 - 1]) / 2.0

if __name__ == '__main__':
    s = MedianFinder()
    print(s.findMedian())
    print(s.addNum(1))
    print(s.addNum(2))
    print(s.findMedian())
    print(s.addNum(3))
    print(s.findMedian())

