# 0 1 1 2 3 5 8 13 21 34 55

class Solution:
    def Fibonacci(self, n):
        r = []
        if n == 0:
            # return 0
            r.append(0)
            return r
        if n == 1:
            # return 1
            r.append(1)
            return r
        # if n>1:
        # return self.Fibonacci(n-2) + self.Fibonacci(n-1)
        if n > 1:
            a = 0
            b = 1
            ret = 0
            for i in range( n - 1):
                ret = a + b
                r.append(ret)
                a = b
                b = ret
            return [0, 1] + r
            # return ret
        return None

# 动态规划
    def f2(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a % 1000000007

    def f3(self, n):
        if n > 1:
            a = 0
            b = 1
            for i in range(n - 1):
                ret = a + b
                a = b
                b = ret
            return ret % 1000000007


s = Solution()
print(s.Fibonacci(9))

print([s.f2(i) for i in range(10)])
print([s.f3(i) for i in range(10)])
