class MinStack:
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x):
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]


    def min(self) -> int:
        return self.B[-1]

s = MinStack()
print(s.push(3))
print(s.push(4))
print(s.push(5))
print(s.min())
print(s.pop())
print(s.top())
print(s.min())


# 