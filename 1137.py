"""


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