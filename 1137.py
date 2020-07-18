"""
1137. 第 N 个泰波那契数
泰波那契序列 Tn 定义如下：

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

"""

class Solution:
    # 1.递归 但会超时
    def tribonacci(self, n: int):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        return self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)

# 2 动态记忆
    def __init__(self):
        self.memo = {}

    def tribonacci2(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        try:
            return self.memo[n]
        except:
            self.memo[n] = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            return self.memo[n]


s = Solution()
print(s.tribonacci(5))
print(s.tribonacci2(5))