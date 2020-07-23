# 0 1 1 2 3 5 8 13 21 34 55

class Solution:
    def Fibonacci(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        # if n>1:
        # return self.Fibonacci(n-2) + self.Fibonacci(n-1)
        if n > 1:
            a = 0
            b = 1
            for i in range(0, n-1):
                ret = a + b
                a = b
                b = ret
            return ret
        return None


s = Solution()
print(s.Fibonacci(100))
