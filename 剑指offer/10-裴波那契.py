# 0 1 1 2 3 5 8 13 21 34 55

class Solution:
    def Fibonacci(self, n):
        r =[]
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
            for i in range(1, n-1):
                ret = a + b
                r.append(ret)
                a = b
                b = ret
            return [0, 1] + r
            # return ret
        return None


s = Solution()
print(s.Fibonacci(50))
