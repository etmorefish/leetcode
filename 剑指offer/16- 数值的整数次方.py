"""
实现函数double Power(double base, int exponent)，求base的exponent次方。不得使用库函数，同时不需要考虑大数问题。

"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        res = 1
        if n < 0:
            x, n = 1/x, -n
        # for i in range(n):
        #     res *= x

        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res
s = Solution()
print(s.myPow(2.0, 10))
print(s.myPow(2.0, -10))